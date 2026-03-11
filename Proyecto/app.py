from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# TSS rates 2025
TSS_EMPLEADO_SFS = 0.0304   # Seguro Familiar de Salud
TSS_EMPLEADO_SVDS = 0.0287  # Seguro de Vejez, Discapacidad y Sobrevivencia
TSS_EMPRESA_SFS = 0.0709
TSS_EMPRESA_SVDS = 0.0710
TSS_EMPRESA_SRL_MIN = 0.011
TSS_EMPRESA_SRL_MAX = 0.013

# ISR 2025 annual scale
ISR_TRAMOS = [
    (416_220.00, 0, 0, 0),          # Exento
    (624_329.00, 416_220.01, 0.15, 0),
    (867_123.00, 624_329.01, 0.20, 31_216.00),
    (float('inf'), 867_123.01, 0.25, 79_776.00),
]

def calcular_isr_anual(salario_anual: float) -> float:
    if salario_anual <= 416_220.00:
        return 0.0
    elif salario_anual <= 624_329.00:
        return (salario_anual - 416_220.01) * 0.15
    elif salario_anual <= 867_123.00:
        return 31_216.00 + (salario_anual - 624_329.01) * 0.20
    else:
        return 79_776.00 + (salario_anual - 867_123.01) * 0.25

def calcular(salario_bruto_mensual: float, usar_srl_max: bool = False):
    srl = TSS_EMPRESA_SRL_MAX if usar_srl_max else TSS_EMPRESA_SRL_MIN

    # TSS empleado
    tss_sfs = salario_bruto_mensual * TSS_EMPLEADO_SFS
    tss_svds = salario_bruto_mensual * TSS_EMPLEADO_SVDS
    tss_empleado_total = tss_sfs + tss_svds

    # ISR (basado en salario bruto anual)
    salario_anual = salario_bruto_mensual * 12
    isr_anual = calcular_isr_anual(salario_anual)
    isr_mensual = isr_anual / 12

    # Salario neto
    salario_neto = salario_bruto_mensual - tss_empleado_total - isr_mensual

    # TSS empresa (informativo)
    empresa_sfs = salario_bruto_mensual * TSS_EMPRESA_SFS
    empresa_svds = salario_bruto_mensual * TSS_EMPRESA_SVDS
    empresa_srl = salario_bruto_mensual * srl
    tss_empresa_total = empresa_sfs + empresa_svds + empresa_srl

    costo_total_empresa = salario_bruto_mensual + tss_empresa_total

    return {
        "salario_bruto": salario_bruto_mensual,
        "tss_sfs": tss_sfs,
        "tss_svds": tss_svds,
        "tss_empleado_total": tss_empleado_total,
        "isr_mensual": isr_mensual,
        "isr_anual": isr_anual,
        "salario_neto": salario_neto,
        "empresa_sfs": empresa_sfs,
        "empresa_svds": empresa_svds,
        "empresa_srl": empresa_srl,
        "tss_empresa_total": tss_empresa_total,
        "costo_total_empresa": costo_total_empresa,
        "tasa_isr": (isr_mensual / salario_bruto_mensual * 100) if salario_bruto_mensual > 0 else 0,
        "tasa_tss_empleado": (TSS_EMPLEADO_SFS + TSS_EMPLEADO_SVDS) * 100,
        "tasa_tss_empresa": (TSS_EMPRESA_SFS + TSS_EMPRESA_SVDS + srl) * 100,
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular_endpoint():
    data = request.get_json()
    salario = float(data.get("salario", 0))
    usar_srl_max = data.get("srl_max", False)
    if salario <= 0:
        return jsonify({"error": "Salario inválido"}), 400
    resultado = calcular(salario, usar_srl_max)
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

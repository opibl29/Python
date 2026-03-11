import os
import json

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich import box
from rich.align import Align

console = Console()

ARCHIVO = "platos.json"


def cargar_platos() -> dict:
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as f:
            json.dump({}, f)
        return {}
    with open(ARCHIVO, "r") as f:
        return json.load(f)


def guardar_platos(platos: dict):
    with open(ARCHIVO, "w") as f:
        json.dump(platos, f, indent=2)


def mostrar_menu():
    console.clear()
    titulo = Text("  GESTIÓN DE PLATOS", style="bold white on dark_red", justify="center")
    menu = Table.grid(padding=(0, 2))
    menu.add_column(style="bold yellow")
    menu.add_column(style="white")
    menu.add_row("[ 1 ]", "Agregar plato")
    menu.add_row("[ 2 ]", "Ver todos los platos")
    menu.add_row("[ 3 ]", "Actualizar plato")
    menu.add_row("[ 4 ]", "Eliminar plato")
    menu.add_row("[ 5 ]", "Salir")

    console.print(Panel(Align(titulo, align="center"), style="dark_red"))
    console.print(Panel(menu, title="[bold]Menú Principal[/bold]", border_style="dim red", padding=(1, 4)))


def tabla_platos(platos: dict) -> Table:
    tabla = Table(
        title=" Lista de Platos",
        box=box.ROUNDED,
        border_style="red",
        header_style="bold white on dark_red",
        show_lines=True,
    )
    tabla.add_column("ID", style="bold yellow", justify="center")
    tabla.add_column("Nombre", style="bold white")
    tabla.add_column("Precio", style="green", justify="right")
    tabla.add_column("Ingredientes", style="dim white")

    for id_, datos in platos.items():
        tabla.add_row(
            id_,
            datos["nombre"],
            f"${datos['precio']:,}",
            datos["ingredientes"],
        )
    return tabla


def crear_plato(platos: dict):
    console.clear()
    console.print(Panel("[bold yellow] Agregar nuevo plato[/bold yellow]", border_style="yellow"))

    id_ = Prompt.ask("[yellow]ID del plato[/yellow]").strip()
    if not id_:
        console.print("[red] El ID no puede estar vacío.[/red]")
        Prompt.ask("\nPresione Enter para continuar")
        return

    if id_ in platos:
        console.print(f"[red]Ya existe un plato con el ID '[bold]{id_}[/bold]'.[/red]")
        Prompt.ask("\nPresione Enter para continuar")
        return

    nombre = Prompt.ask("[yellow]Nombre[/yellow]").strip()
    if not nombre:
        console.print("[red] El nombre no puede estar vacío.[/red]")
        Prompt.ask("\nPresione Enter para continuar")
        return

    precio = IntPrompt.ask("[yellow]Precio[/yellow]")
    if precio < 1:
        console.print("[red] El precio debe ser mayor a 0.[/red]")
        Prompt.ask("\nPresione Enter para continuar")
        return

    ingredientes = Prompt.ask("[yellow]Ingredientes[/yellow]").strip()
    if not ingredientes:
        console.print("[red] Los ingredientes no pueden estar vacíos.[/red]")
        Prompt.ask("\nPresione Enter para continuar")
        return

    platos[id_] = {"nombre": nombre, "precio": precio, "ingredientes": ingredientes}
    guardar_platos(platos)
    console.print(f"\n[bold green] Plato '[/bold green][bold white]{nombre}[/bold white][bold green]' agregado correctamente.[/bold green]")
    Prompt.ask("\nPresione Enter para continuar")


def leer_platos(platos: dict):
    console.clear()
    if not platos:
        console.print(Panel("[bold red]No hay platos registrados aún.[/bold red]", border_style="red"))
    else:
        console.print(tabla_platos(platos))
    Prompt.ask("\nPresione Enter para continuar")


def actualizar_plato(platos: dict):
    console.clear()
    console.print(Panel("[bold cyan] Actualizar plato[/bold cyan]", border_style="cyan"))

    if not platos:
        console.print("[red] No hay platos para modificar.[/red]")
        Prompt.ask("\nPresione Enter para continuar")
        return

    console.print(tabla_platos(platos))

    id_ = Prompt.ask("\n[cyan]ID del plato a actualizar[/cyan]").strip()
    if id_ not in platos:
        console.print(f"[red] No existe un plato con el ID '[bold]{id_}[/bold]'.[/red]")
        Prompt.ask("\nPresione Enter para continuar")
        return

    actual = platos[id_]
    console.print(f"\nDatos actuales: [dim]{actual['nombre']} | ${actual['precio']} | {actual['ingredientes']}[/dim]")
    console.print("[dim](Deje en blanco para conservar el valor actual)[/dim]\n")

    nombre = Prompt.ask(f"[cyan]Nombre[/cyan] [dim][{actual['nombre']}][/dim]").strip() or actual["nombre"]
    precio_str = Prompt.ask(f"[cyan]Precio[/cyan] [dim][{actual['precio']}][/dim]").strip()
    precio = int(precio_str) if precio_str.isdigit() and int(precio_str) >= 1 else actual["precio"]
    ingredientes = Prompt.ask(f"[cyan]Ingredientes[/cyan] [dim][{actual['ingredientes']}][/dim]").strip() or actual["ingredientes"]

    platos[id_] = {"nombre": nombre, "precio": precio, "ingredientes": ingredientes}
    guardar_platos(platos)
    console.print(f"\n[bold green] Plato '[bold white]{nombre}[/bold white]' actualizado correctamente.[/bold green]")
    Prompt.ask("\nPresione Enter para continuar")


def eliminar_plato(platos: dict):
    console.clear()
    console.print(Panel("[bold red]  Eliminar plato[/bold red]", border_style="red"))

    if not platos:
        console.print("[red] No hay platos para eliminar.[/red]")
        Prompt.ask("\nPresione Enter para continuar")
        return

    console.print(tabla_platos(platos))

    id_ = Prompt.ask("\n[red]ID del plato a eliminar[/red]").strip()
    if id_ not in platos:
        console.print(f"[red] No existe un plato con el ID '[bold]{id_}[/bold]'.[/red]")
        Prompt.ask("\nPresione Enter para continuar")
        return

    nombre = platos[id_]["nombre"]
    confirmacion = Prompt.ask(f"[bold red]¿Seguro que deseas eliminar '[white]{nombre}[/white]'? (s/n)[/bold red]").strip().lower()
    if confirmacion == "s":
        del platos[id_]
        guardar_platos(platos)
        console.print(f"\n[bold green] Plato '[bold white]{nombre}[/bold white]' eliminado correctamente.[/bold green]")
    else:
        console.print("[yellow]  Operación cancelada.[/yellow]")

    Prompt.ask("\nPresione Enter para continuar")


def main():
    platos = cargar_platos()

    while True:
        mostrar_menu()
        opcion = Prompt.ask("[bold yellow]Elige una opción[/bold yellow]", choices=["1", "2", "3", "4", "5"])

        if opcion == "1":
            crear_plato(platos)
        elif opcion == "2":
            leer_platos(platos)
        elif opcion == "3":
            actualizar_plato(platos)
        elif opcion == "4":
            eliminar_plato(platos)
        elif opcion == "5":
            console.clear()
            console.print(Panel(
                Align("[bold white] ¡Gracias por usar el sistema de platos![/bold white]", align="center"),
                border_style="dark_red",
                padding=(1, 4),
            ))
            break


if __name__ == "__main__":
    main()

import flet as ft
from flet import View
from classApp.WidgetClass import Button, ViewClass, Field, Text, Alert, ButtonAlert, Modal, FieldArray, Select, FieldMatriz
from flet import RouteChangeEvent, ViewPopEvent
from classApp.Methods.createTxt import createTXT
import yaml
import traceback
from classApp.Methods.Trabajo import Trabajo  # Import the Trabajo class

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# VARIABLES GLOBALES
ALIGN_VERT = ft.MainAxisAlignment.CENTER
ALIGN_HOR = ft.CrossAxisAlignment.CENTER
WIDTH = config['size']['width']
HEIGHT = config['size']['height']
COLOR_PRIMARY = config['colors']['primary']
COLOR_SECOND = config['colors']['second']

# ASIGNACION de Clases

def main(page: ft.Page) -> None:
    page.title = "Calculadora Programacion Entera"
    page.window.height = HEIGHT
    page.window.width = WIDTH
    page.window.center()
    page.window.resizable = False

    alert = Alert([ButtonAlert("Close", lambda _: page.close(alert))])
    modal = Modal()

    def router_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        # Home --> Menu
        page.views.append(
            ViewClass('/', 
                [
                    ft.Column([Text("Bienvenido a Calculadora Dinamica", 20, "w150"), Text("Menú", 40, "w800")], 
                    spacing=0, horizontal_alignment=ALIGN_HOR),
                    ft.Row([Button("Trabajo", lambda _: page.go('/trabajo'))], 
                    spacing=10, alignment=ALIGN_VERT),
                    ft.Row([ ], 
                    spacing=10, alignment=ALIGN_VERT)
                ])
        )
        
        # Trabajo
        if page.route == '/trabajo': 
            n_semanas_field = Field("Número de semanas", "n_semanas")
            trabajadores_requeridos_field = FieldArray("Trabajadores requeridos por semana", "trabajadores_requeridos")
            costo_excedente_field = Field("Costo excedente", "costo_excedente")
            costo_contratacion_field = Field("Costo de contratación", "costo_contratacion")
            costo_contratacion_ex_field = Field("Costo de contratación extra", "costo_contratacion_ex")

            def calcular_trabajo(e):
                try:
                    n_semanas = int(n_semanas_field.getValue())
                    trabajadores_requeridos = list(map(int, trabajadores_requeridos_field.getValue().split(',')))
                    costo_excedente = int(costo_excedente_field.getValue())
                    costo_contratacion = int(costo_contratacion_field.getValue())
                    costo_contratacion_ex = int(costo_contratacion_ex_field.getValue())

                    trabajo = Trabajo(n_semanas, trabajadores_requeridos, costo_excedente, costo_contratacion, costo_contratacion_ex)
                    resultado = trabajo.optimize_workforce()
                    page.dialog = Alert([Text(f"Resultado: {resultado}")])
                    page.dialog.open = True
                    modal.openModal(page, "Resultado", [ft.Text(f"Resultado: {resultado}", color=COLOR_SECOND), Button("Cerrar", lambda _: page.close(modal))])
                    createTXT(resultado, "Trabajo")
                    page.update()
                except ValueError:
                    alert.openAlert(page, "Error: Por favor, ingrese valores numéricos válidos.")
                except TypeError:
                    alert.openAlert(page, "Error: Tipo de dato incorrecto.")
                except AttributeError:
                    alert.openAlert(page, "Error: Atributo no encontrado.")
                except Exception as ex:
                    alert.openAlert(page, f"Error inesperado: {str(ex)}")
            

            page.views.append(
                ViewClass('/trabajo', 
                [
                    Text("Trabajo", 35, "w800"),
                    n_semanas_field,
                    trabajadores_requeridos_field,
                    costo_excedente_field,
                    costo_contratacion_field,
                    costo_contratacion_ex_field,
                    Button("Calcular", calcular_trabajo),
                    Button("Go to Home", lambda _: page.go('/'))
                ])
            )

        page.update()
    
    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = router_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()

if __name__ == "__main__":
    ft.app(main)
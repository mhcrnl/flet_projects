import flet as ft

class HelpMenu:
    def __init__(self, page: ft.Page):
        self.page = page
        self.dialog = ft.AlertDialog(
            title=ft.Text("Centru de Ajutor"),
            content=ft.Text("Aceasta este o structură modulară:\n\n"
                            "- Fiecare clasă are fișierul ei.\n"
                            "- Codul este ușor de testat."),
            actions=[
                ft.TextButton("Închide", on_click=self.close_help)
            ],
        )

    def show_help(self, e):
        self.page.overlay.append(self.dialog) # Recomandat în versiunile noi Flet
        self.dialog.open = True
        self.page.update()

    def close_help(self, e):
        self.dialog.open = False
        self.page.update()

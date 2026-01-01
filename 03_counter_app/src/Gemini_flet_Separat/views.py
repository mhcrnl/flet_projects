import flet as ft

class MainView:
    def __init__(self, page: ft.Page):
        self.page = page
        
    def build_app_bar(self):
        # Creăm AppBar-ul separat pentru claritate
        return ft.AppBar(
            leading=ft.Icon(ft.Icons.PALETTE),
            leading_width=40,
            title=ft.Text("Aplicația Mea Flet"),
            center_title=False,
            bgcolor=ft.Colors.SURFACE,
            actions=[
                ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.Icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Setări"),
                        ft.PopupMenuItem(text="Ieșire"),
                    ]
                ),
            ],
        )

    def get_content(self):
        # Returnăm conținutul principal al paginii
        return ft.Column(
            [
                ft.Text("Bine ai venit!", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Aceasta este o structură bazată pe clase."),
                ft.ElevatedButton("Apasă-mă", on_click=lambda _: print("Buton apăsat!"))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

import flet as ft

class MainView:
    def __init__(self, page: ft.Page):
        self.page = page
        # Păstrăm referința la butonul de theme pentru a-i schimba iconița ulterior
        self.theme_button = ft.IconButton(
            icon=ft.Icons.WB_SUNNY_OUTLINED, 
            tooltip="Schimbă tema",
            on_click=self.toggle_theme
        )

    def toggle_theme(self, e):
        # Logica de schimbare a temei
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.theme_button.icon = ft.Icons.DARK_MODE_OUTLINED
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.theme_button.icon = ft.Icons.WB_SUNNY_OUTLINED
        
        self.page.update()

    def build_app_bar(self):
        return ft.AppBar(
            leading=ft.Icon(ft.Icons.PALETTE),
            title=ft.Text("Aplicația Mea Flet"),
            center_title=False,
            bgcolor=ft.Colors.SURFACE,
            actions=[
                self.theme_button, # Folosim butonul definit în __init__
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Setări"),
                    ]
                ),
            ],
        )

    def get_content(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Mod Vizualizare", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Apasă pe iconița din colțul dreapta sus pentru a schimba tema."),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.center
        )

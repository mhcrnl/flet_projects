import flet as ft
from help_menu import HelpMenu

class MainView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.help_component = HelpMenu(page)
        
        # Elementul pentru temă
        self.theme_icon = ft.IconButton(
            icon=ft.Icons.WB_SUNNY_OUTLINED,
            on_click=self.toggle_theme
        )

    def toggle_theme(self, e):
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.theme_icon.icon = ft.Icons.DARK_MODE_OUTLINED
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.theme_icon.icon = ft.Icons.WB_SUNNY_OUTLINED
        self.page.update()

    def build_app_bar(self):
        return ft.AppBar(
            title=ft.Text("Flet Multi-File App"),
            bgcolor=ft.Colors.SURFACE,
            actions=[
                self.theme_icon,
                ft.IconButton(
                    icon=ft.Icons.HELP_OUTLINE, 
                    on_click=self.help_component.show_help
                ),
            ],
        )

    def get_body(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Aplicație Organizată pe Fișiere", size=20, weight="bold"),
                    ft.Icon(ft.Icons.FOLDER_OPEN, size=100, color=ft.Colors.AMBER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

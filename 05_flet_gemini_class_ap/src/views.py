import flet as ft

class HelpMenu:
    def __init__(self, page: ft.Page):
        self.page = page
        # Creăm dialogul de ajutor
        self.dialog = ft.AlertDialog(
            title=ft.Text("Centru de Ajutor"),
            content=ft.Text("Aceasta este o aplicație demonstrativă Flet.\n\n"
                            "1. Folosește butonul soare/lună pentru temă.\n"
                            "2. Meniul lateral oferă opțiuni extra."),
            actions=[
                ft.TextButton("Am înțeles", on_click=self.close_help)
            ],
        )

    def show_help(self, e):
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def close_help(self, e):
        self.dialog.open = False
        self.page.update()

class MainView:
    def __init__(self, page: ft.Page):
        self.page = page
        # Instanțiem meniul de help
        self.help_menu = HelpMenu(page)
        
        self.theme_button = ft.IconButton(
            icon=ft.Icons.WB_SUNNY_OUTLINED, 
            on_click=self.toggle_theme
        )

    def toggle_theme(self, e):
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
            title=ft.Text("Aplicație Modulară"),
            bgcolor=ft.Colors.SURFACE,
            actions=[
                self.theme_button,
                # Butonul care deschide clasa HelpMenu
                ft.IconButton(
                    icon=ft.Icons.HELP_OUTLINE, 
                    on_click=self.help_menu.show_help
                ),
                ft.PopupMenuButton(
                    items=[ft.PopupMenuItem(text="Setări")]
                ),
            ],
        )

    def get_content(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.ROCKET_LAUNCH, size=50, color=ft.Colors.BLUE),
                    ft.Text("Structură cu Clase Separate", size=25, weight="bold"),
                    ft.Text("Apasă pe butonul '?' pentru ajutor"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.center
        )

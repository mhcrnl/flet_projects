import flet as ft

# ---------------------------------------------------
# 1. Help Menu avansat cu pagini multiple
# ---------------------------------------------------
class HelpMenu:
    def __init__(self, page: ft.Page):
        self.page = page
        self.dialog = None

    def open(self, e):
        # Tab-urile din Help
        tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Introducere",
                    content=ft.Text(
                        "Aceasta este pagina de introducere.\n\n"
                        "Aici explici scopul aplicației și cum funcționează."
                    )
                ),
                ft.Tab(
                    text="Funcționalități",
                    content=ft.Text(
                        "Funcționalități disponibile:\n"
                        "- Navigare\n"
                        "- Setări\n"
                        "- Export\n"
                        "- Sincronizare"
                    )
                ),
                ft.Tab(
                    text="FAQ",
                    content=ft.Text(
                        "Întrebări frecvente:\n\n"
                        "1. Cum schimb tema?\n"
                        "   → Folosește butonul din AppBar.\n\n"
                        "2. Cum accesez Help?\n"
                        "   → Apasă iconița Help."
                    )
                ),
                ft.Tab(
                    text="Contact",
                    content=ft.Text(
                        "Pentru suport:\n"
                        "support@aplicatia-ta.ro\n"
                        "sau vizitează site-ul oficial."
                    )
                ),
            ],
            expand=True
        )

        # IMPORTANT: Tabs trebuie puse într-un Container expandabil
        content_container = ft.Container(
            content=tabs,
            width=500,
            height=350
        )

        # Dialogul Help
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Centru de Ajutor"),
            content=content_container,
            actions=[
                ft.TextButton("Închide", on_click=self.close)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

        # IMPORTANT: trebuie setat înainte de open=True
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def close(self, e):
        self.dialog.open = False
        self.page.update()


# ---------------------------------------------------
# 2. AppBar cu temă dinamică + Help avansat
# ---------------------------------------------------
class ThemedAppBar:
    def __init__(self, page: ft.Page):
        self.page = page
        self.help_menu = HelpMenu(page)

    def toggle_theme(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.page.update()

    def build(self):
        return ft.AppBar(
            title=ft.Text("AppBar cu Temă Dinamică + Help Avansat"),
            center_title=True,
            bgcolor=ft.Colors.BLUE,
            actions=[
                ft.IconButton(
                    ft.Icons.HELP_OUTLINE,
                    tooltip="Deschide Help",
                    on_click=self.help_menu.open
                ),
                ft.IconButton(
                    ft.Icons.DARK_MODE,
                    tooltip="Schimbă tema",
                    on_click=self.toggle_theme
                )
            ]
        )


# ---------------------------------------------------
# 3. Main App
# ---------------------------------------------------
def main(page: ft.Page):
    page.title = "Exemplu AppBar cu Help Avansat"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.appbar = ThemedAppBar(page).build()

    page.add(
        ft.Text(
            "Apasă iconița Help pentru a deschide meniul avansat cu pagini multiple.",
            size=20
        )
    )


ft.app(target=main)

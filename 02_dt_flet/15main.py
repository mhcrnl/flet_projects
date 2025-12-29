import flet as ft

# ---------------------------------------------------
# 1. Clasă pentru Help Menu avansat (cu pagini multiple)
# ---------------------------------------------------
class HelpMenu:
    def __init__(self, page: ft.Page):
        self.page = page

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
                        "Aici poți explica scopul aplicației, cum funcționează, "
                        "și ce poate face utilizatorul."
                    )
                ),
                ft.Tab(
                    text="Funcționalități",
                    content=ft.Text(
                        "Aici poți lista funcționalitățile aplicației:\n"
                        "- Navigare\n"
                        "- Setări\n"
                        "- Export\n"
                        "- Sincronizare\n"
                        "- Orice altceva ai nevoie"
                    )
                ),
                ft.Tab(
                    text="FAQ",
                    content=ft.Text(
                        "Întrebări frecvente:\n\n"
                        "1. Cum schimb tema?\n"
                        "   → Folosește butonul din AppBar.\n\n"
                        "2. Cum accesez Help?\n"
                        "   → Apasă iconița Help.\n\n"
                        "3. Pot salva setările?\n"
                        "   → Da, în versiunea completă."
                    )
                ),
                ft.Tab(
                    text="Contact",
                    content=ft.Text(
                        "Ai nevoie de ajutor suplimentar?\n\n"
                        "Trimite un mesaj la:\n"
                        "support@aplicatia-ta.ro\n\n"
                        "sau vizitează pagina noastră oficială."
                    )
                ),
            ],
            expand=True
        )

        # Dialogul Help
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Centru de Ajutor"),
            content=tabs,
            actions=[
                ft.TextButton("Închide", on_click=self.close)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            open=True
        )

        self.page.dialog = self.dialog
        self.page.update()

    def close(self, e):
        self.dialog.open = False
        self.page.update()


# ---------------------------------------------------
# 2. Clasă pentru AppBar cu temă dinamică + Help avansat
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

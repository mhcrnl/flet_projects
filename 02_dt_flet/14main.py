import flet as ft

# ---------------------------------------------------
# 1. Clasă pentru AppBar cu temă dinamică + Help
# ---------------------------------------------------
class ThemedAppBar:
    def __init__(self, page: ft.Page):
        self.page = page

    # schimbă tema între dark/light
    def toggle_theme(self, e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.page.update()

    # deschide meniul Help
    def open_help(self, e):
        help_dialog = ft.AlertDialog(
            title=ft.Text("Ajutor"),
            content=ft.Text(
                "Acesta este meniul de Help.\n\n"
                "Aici poți pune instrucțiuni, informații, documentație,\n"
                "sau orice alt text util pentru utilizator."
            ),
            actions=[
                ft.TextButton("Închide", on_click=lambda _: self.close_help(help_dialog))
            ],
            modal=True
        )
        self.page.dialog = help_dialog
        help_dialog.open = True
        self.page.update()

    # închide dialogul Help
    def close_help(self, dialog):
        dialog.open = False
        self.page.update()

    # construiește AppBar-ul
    def build(self):
        return ft.AppBar(
            title=ft.Text("AppBar cu temă dinamică + Help"),
            center_title=True,
            bgcolor=ft.Colors.BLUE,
            actions=[
                ft.IconButton(
                    ft.Icons.HELP_OUTLINE,
                    tooltip="Ajutor",
                    on_click=self.open_help
                ),
                ft.IconButton(
                    ft.Icons.DARK_MODE,
                    tooltip="Schimbă tema",
                    on_click=self.toggle_theme
                )
            ]
        )


# ---------------------------------------------------
# 2. Main App
# ---------------------------------------------------
def main(page: ft.Page):
    page.title = "Exemplu AppBar cu Dark/Light + Help"
    page.theme_mode = ft.ThemeMode.LIGHT  # tema inițială

    # setăm appbar-ul din clasă
    page.appbar = ThemedAppBar(page).build()

    # conținutul paginii
    page.add(
        ft.Text("Apasă iconițele din AppBar pentru a schimba tema sau a deschide Help.", size=20)
    )


ft.app(target=main)

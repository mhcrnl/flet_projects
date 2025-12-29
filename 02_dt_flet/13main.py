import flet as ft

# ---------------------------------------------------
# 1. Clasă pentru AppBar cu temă dinamică
# ---------------------------------------------------
class ThemedAppBar:
    def __init__(self, page: ft.Page):
        self.page = page

    def toggle_theme(self, e):
        # schimbăm tema
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.page.update()

    def build(self):
        return ft.AppBar(
            title=ft.Text("AppBar cu temă dinamică"),
            center_title=True,
            bgcolor=ft.Colors.BLUE,
            actions=[
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
    page.title = "Exemplu AppBar cu Dark/Light Theme"
    page.theme_mode = ft.ThemeMode.LIGHT  # tema inițială

    # setăm appbar-ul din clasă
    page.appbar = ThemedAppBar(page).build()

    # conținutul paginii
    page.add(
        ft.Text("Apasă iconița din AppBar pentru a schimba tema!", size=20)
    )


ft.app(target=main)

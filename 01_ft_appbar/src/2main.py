import flet as ft

def main(page: ft.Page):
    page.title = "Dark / Light Mode"
    page.theme_mode = "light"  # default
    page.update()

    def toggle_theme(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()

    page.add(
        ft.Text("Schimbă tema aplicației"),
        ft.Switch(label="Dark mode", on_change=toggle_theme)
    )

ft.app(target=main)

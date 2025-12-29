import flet as ft

def main(page: ft.Page):
    light_theme = ft.Theme(
        color_scheme_seed="blue",
        brightness=ft.Brightness.LIGHT
    )

    dark_theme = ft.Theme(
        color_scheme_seed="blue",
        brightness=ft.Brightness.DARK
    )

    page.theme = light_theme

    def toggle_theme(e):
        page.theme = dark_theme if page.theme == light_theme else light_theme
        page.update()

    page.add(
        ft.Text("Custom theme switch"),
        ft.Switch(label="Dark mode", on_change=toggle_theme)
    )

ft.app(target=main)

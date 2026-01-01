import flet as ft
from views import MainView

def main(page: ft.Page):
    page.title = "Flet App cu Clase"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Instanțiem clasa noastră
    app_view = MainView(page)
    
    # Setăm AppBar-ul și conținutul
    page.appbar = app_view.build_app_bar()
    page.add(app_view.get_content())
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

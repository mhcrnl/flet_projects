import flet as ft
from views import MainView

def main(page: ft.Page):
    page.title = "Flet Theme Switcher"
    
    # Setăm tema inițială explicit
    page.theme_mode = ft.ThemeMode.DARK
    
    app_view = MainView(page)
    
    page.appbar = app_view.build_app_bar()
    page.add(app_view.get_content())
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

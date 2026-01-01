import flet as ft
from main_view import MainView

def main(page: ft.Page):
    page.title = "Modular Flet App"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 600
    
    # Inițializăm vizualizarea
    app_layout = MainView(page)
    
    # Adăugăm componentele în pagină
    page.appbar = app_layout.build_app_bar()
    page.add(app_layout.get_body())
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

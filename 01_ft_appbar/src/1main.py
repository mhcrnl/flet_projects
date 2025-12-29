import flet as ft

def main(page: ft.Page):
    page.title = "Exemplo Light/Dark Mode"
    
    # Define o modo inicial (LIGHT, DARK ou SYSTEM)
    page.theme_mode = ft.ThemeMode.LIGHT

    def toggle_theme_mode(e):
        # Lógica de troca
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            btn_theme.icon = ft.Icons.WBM_SUNNY_OUTLINED
            btn_theme.text = "Mudar para Light Mode"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_theme.icon = ft.Icons.DARK_MODE_OUTLINED
            btn_theme.text = "Mudar para Dark Mode"
        
        page.update()

    # Botão para alternar o tema
    btn_theme = ft.ElevatedButton(
        text="Mudar para Dark Mode",
        icon=ft.Icons.DARK_MODE_OUTLINED,
        on_click=toggle_theme_mode
    )

    page.add(
        ft.Text("Olá! Este é um exemplo de tema no Flet.", size=25),
        btn_theme
    )

ft.app(target=main)

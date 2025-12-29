import flet as ft

def main(page: ft.Page):

    def open_dialog(e):
        page.dialog = dialog
        dialog.open = True
        page.update()

    dialog = ft.AlertDialog(
        title=ft.Text("Salut!"),
        content=ft.Text("Acesta este un AlertDialog."),
        actions=[
            ft.TextButton("OK", on_click=lambda e: close_dialog())
        ],
    )

    def close_dialog():
        dialog.open = False
        page.update()

    page.add(
        ft.ElevatedButton("Deschide dialog", on_click=open_dialog)
    )

ft.app(target=main)

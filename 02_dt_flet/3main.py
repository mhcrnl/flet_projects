import flet as ft

def create_dialog(page, title, message, on_confirm=None, on_cancel=None):
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(title),
        content=ft.Text(message),
        actions=[
            ft.TextButton("Cancel", on_click=lambda e: close_dialog(dialog, page, on_cancel)),
            ft.FilledButton("OK", on_click=lambda e: close_dialog(dialog, page, on_confirm)),
        ],
    )
    return dialog

def close_dialog(dialog, page, callback=None):
    dialog.open = False
    page.update()
    if callback:
        callback()

def main(page: ft.Page):

    def open_reusable_dialog(e):
        dlg = create_dialog(
            page,
            "Confirmare",
            "Ești sigur că vrei să continui?",
            on_confirm=lambda: print("Confirmat!"),
            on_cancel=lambda: print("Anulat!")
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Deschide dialog reutilizabil", on_click=open_reusable_dialog)
    )

ft.app(target=main)

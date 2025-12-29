import flet as ft

class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.Colors.ORANGE_300
        self.color = ft.Colors.GREEN_800
        self.text = text
        self.on_click = on_click

def main(page: ft.Page):

    page.title = "MY page"
    page.theme_mode = "light"
    page.update()

    def toggle_theme(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    def help(e):
        #page.dialog = a_dlg
        page.open(a_dlg) #open=True
        page.update()

    a_dlg = ft.AlertDialog(
        title=ft.Text("Hello"),
        content = ft.Text("Acesta este un AlertDialog."),
        actions=[
            ft.TextButton("OK", on_click=lambda e: close_dialog)
            ],
        )

    def close_dialog(e):
        page.dialog = a_dlg
        a_dlg.open=False
        page.update()

    def ok_clicked(e):
        print("OK clicked")
    
    def cancel_clicked(e):
        print("Cancel clicked")

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBAR Ex"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED, on_click=toggle_theme),
            ft.IconButton(ft.Icons.FILTER_4),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item1"),
                    ft.PopupMenuItem("Help", on_click=help),
                    ft.PopupMenuItem(), #divider
                    ft.PopupMenuItem(text="Checked item", checked=False,
                                     on_click=check_item_clicked),

                    ]

                )

            ]

        )

    page.add(
        MyButton(text="OK", on_click=ok_clicked),
        MyButton(text="Cancel", on_click=cancel_clicked),
    )

ft.app(main)

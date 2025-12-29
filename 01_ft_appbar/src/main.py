import flet as ft


def main(page: ft.Page):
    page.title = "AppBar Example"
    page.theme_mode = "light"
    page.update()

    def toggle_theme(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        page.update()

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    def help(e):
        print("HELP!")
        page.open(a_dlg)
        page.update()

    a_dlg = ft.AlertDialog(title=ft.Text("HELLO!"))

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED, on_click=toggle_theme),
            ft.IconButton(ft.Icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem("Help", on_click=help),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    page.add(ft.Text("Body!"))


ft.app(target=main)

import flet as ft

# ---------------------------------------------------
# 1. Clasă simplă pentru AppBar
# ---------------------------------------------------
class MyAppBar:
    def __init__(self, title: str):
        self.title = title

    def build(self):
        return ft.AppBar(
            title=ft.Text(self.title),
            bgcolor=ft.Colors.BLUE,
            center_title=True,
            leading=ft.Icon(ft.Icons.MENU),
            actions=[
                ft.IconButton(ft.Icons.SEARCH),
                ft.IconButton(ft.Icons.MORE_VERT),
            ]
        )


# ---------------------------------------------------
# 2. Main App
# ---------------------------------------------------
def main(page: ft.Page):
    page.title = "Exemplu AppBar în clasă"
    page.appbar = MyAppBar("Bun venit, Mihai!").build()

    page.add(
        ft.Text("Conținutul paginii începe aici...", size=20)
    )


ft.app(target=main)

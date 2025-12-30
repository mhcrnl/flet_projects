import flet as ft


class CounterApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Counter App"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # Theme mode
        self.is_dark = False
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # AppBar
        self.theme_button = ft.IconButton(
            icon=ft.Icons.DARK_MODE,
            tooltip="Dark mode",
            on_click=self.toggle_theme
        )

        self.page.appbar = ft.AppBar(
            title=ft.Text("Counter App"),
            center_title=True,
            actions=[
                self.theme_button,
                ft.IconButton(
                    icon=ft.Icons.REFRESH,
                    tooltip="Reset counter",
                    on_click=self.reset
                )
            ],
        )

        self.counter = 0

        self.counter_text = ft.Text(
            value=str(self.counter),
            size=40,
            weight=ft.FontWeight.BOLD
        )

        self.page.add(
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.counter_text,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton("-", on_click=self.decrement),
                            ft.ElevatedButton("+", on_click=self.increment),
                        ],
                    ),
                ],
            )
        )

    def toggle_theme(self, e):
        self.is_dark = not self.is_dark
        self.page.theme_mode = (
            ft.ThemeMode.DARK if self.is_dark else ft.ThemeMode.LIGHT
        )
        self.theme_button.icon = (
            ft.Icons.LIGHT_MODE if self.is_dark else ft.icons.DARK_MODE
        )
        self.page.update()

    def increment(self, e):
        self.counter += 1
        self.update_counter()

    def decrement(self, e):
        self.counter -= 1
        self.update_counter()

    def reset(self, e):
        self.counter = 0
        self.update_counter()

    def update_counter(self):
        self.counter_text.value = str(self.counter)
        self.page.update()


def main(page: ft.Page):
    CounterApp(page)


ft.app(target=main)

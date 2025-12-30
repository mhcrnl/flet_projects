import flet as ft


class CounterApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Counter App (Flet - OOP)"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

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
                            ft.ElevatedButton(
                                "-",
                                on_click=self.decrement
                            ),
                            ft.ElevatedButton(
                                "+",
                                on_click=self.increment
                            ),
                        ],
                    ),
                ],
            )
        )

    def increment(self, e):
        self.counter += 1
        self.update_counter()

    def decrement(self, e):
        self.counter -= 1
        self.update_counter()

    def update_counter(self):
        self.counter_text.value = str(self.counter)
        self.page.update()


def main(page: ft.Page):
    CounterApp(page)


ft.app(target=main)

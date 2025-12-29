import flet as ft

# ---------------------------------------------------
# 1. Clasa de logică (fără UI)
# ---------------------------------------------------
class CounterLogic:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1


# ---------------------------------------------------
# 2. Clasa UI (folosește logica)
# ---------------------------------------------------
class CounterView:
    def __init__(self):
        self.logic = CounterLogic()
        self.text = ft.Text(str(self.logic.value))

    def build(self):
        return ft.Row(
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=self.minus),
                self.text,
                ft.IconButton(ft.Icons.ADD, on_click=self.plus),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    def plus(self, e):
        self.logic.increment()
        self.text.value = str(self.logic.value)
        self.text.update()

    def minus(self, e):
        self.logic.decrement()
        self.text.value = str(self.logic.value)
        self.text.update()


# ---------------------------------------------------
# 3. Main App
# ---------------------------------------------------
def main(page: ft.Page):
    page.title = "Counter App cu Clase"

    counter = CounterView()

    page.add(
        ft.Text("Counter App implementată cu clase", size=22, weight="bold"),
        counter.build()
    )


ft.app(target=main)

import flet as ft
import os

# ---------------------------------------------------
# 1. Clasa de logică cu salvare automată
# ---------------------------------------------------
class CounterLogic:
    def __init__(self, save_file="counter.txt"):
        self.save_file = save_file
        self.value = self.load_value()

    def load_value(self):
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, "r") as f:
                    return int(f.read().strip())
            except:
                return 0
        return 0

    def save_value(self):
        with open(self.save_file, "w") as f:
            f.write(str(self.value))

    def increment(self):
        self.value += 1
        self.save_value()

    def decrement(self):
        self.value -= 1
        self.save_value()


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
    page.title = "Counter cu Salvare Automată"

    counter = CounterView()

    page.add(
        ft.Text("Counter cu salvare automată", size=22, weight="bold"),
        counter.build()
    )


ft.app(target=main)

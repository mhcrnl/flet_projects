import flet as ft

# -------------------------------
# 1. Clasa de logică (fără UI)
# -------------------------------
class CounterLogic:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1


# -------------------------------
# 2. Clasa UI care moștenește Control
# -------------------------------
class CounterView(ft.Control):
    def __init__(self):
        super().__init__()
        self.logic = CounterLogic()
        self.text = ft.Text(str(self.logic.value))

    # obligatoriu pentru orice Control custom
    def _get_control_name(self):
        return "counter_view"

    # UI-ul controlului
    def _build(self):
        return ft.Row(
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=self.minus),
                self.text,
                ft.IconButton(ft.Icons.ADD, on_click=self.plus),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    # metodele de acțiune
    def plus(self, e):
        self.logic.increment()
        self.text.value = str(self.logic.value)
        self.update()

    def minus(self, e):
        self.logic.decrement()
        self.text.value = str(self.logic.value)
        self.update()


# -------------------------------
# 3. Main App
# -------------------------------
def main(page: ft.Page):
    page.title = "Exemplu Flet cu clase în același fișier"
    page.add(CounterView())


ft.app(target=main)

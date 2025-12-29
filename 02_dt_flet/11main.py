import flet as ft

# ---------------------------------------------------
# 1. Clasă simplă pentru un buton "logic + UI"
# ---------------------------------------------------
class SimpleButton:
    def __init__(self, text, color="blue", on_click=None):
        self.text = text
        self.color = color
        self.on_click = on_click

    def build(self):
        return ft.ElevatedButton(
            text=self.text,
            bgcolor=self.color,
            color="white",
            on_click=self.on_click
        )


# ---------------------------------------------------
# 2. Alt exemplu: buton cu icon
# ---------------------------------------------------
class IconButtonSimple:
    def __init__(self, text, icon, on_click=None):
        self.text = text
        self.icon = icon
        self.on_click = on_click

    def build(self):
        return ft.FilledButton(
            text=self.text,
            icon=self.icon,
            on_click=self.on_click
        )


# ---------------------------------------------------
# 3. Exemplu: buton cu stare internă (counter)
# ---------------------------------------------------
class CounterButton:
    def __init__(self):
        self.value = 0
        self.text_control = ft.Text("0")

    def increment(self, e):
        self.value += 1
        self.text_control.value = str(self.value)
        self.text_control.update()

    def build(self):
        return ft.Row([
            ft.ElevatedButton("Add", on_click=self.increment),
            self.text_control
        ])


# ---------------------------------------------------
# 4. Main App
# ---------------------------------------------------
def main(page: ft.Page):

    def hello(e):
        print("Salut, Mihai!")

    # instanțiem clasele
    btn1 = SimpleButton("Apasă-mă", color="green", on_click=hello)
    btn2 = IconButtonSimple("Like", ft.Icons.THUMB_UP, on_click=hello)
    counter = CounterButton()

    # adăugăm controalele construite
    page.add(
        btn1.build(),
        btn2.build(),
        counter.build()
    )


ft.app(target=main)

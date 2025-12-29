import flet as ft

class AnimatedButton(ft.Control):
    def __init__(self, text, on_click=None, color="blue"):
        super().__init__()
        self.text = text
        self.on_click = on_click
        self.color = color

        # stare internă
        self.hovered = False

    def _build(self):
        # stil în funcție de hover
        scale = 1.1 if self.hovered else 1.0
        bgcolor = ft.Colors.BLUE_700 if self.hovered else self.color

        return ft.Container(
            padding=12,
            bgcolor=bgcolor,
            border_radius=10,
            alignment=ft.alignment.center,
            animate=ft.animation.Animation(200, "easeOut"),
            animate_scale=ft.animation.Animation(150, "easeOut"),
            scale=scale,
            on_click=self.on_click,
            on_hover=self._on_hover,
            content=ft.Text(self.text, color="white", size=16, weight="bold"),
        )

    def _on_hover(self, e):
        self.hovered = e.data == "true"
        self.update()


def main(page: ft.Page):

    def pressed(e):
        print("Ai apăsat butonul animat!")

    btn = AnimatedButton("Apasă-mă", on_click=pressed, color=ft.Colors.BLUE)

    page.add(
        ft.Text("Buton animat cu Control", size=22, weight="bold"),
        btn
    )

ft.app(target=main)

import flet as ft

class Badge(ft.Control):
    def __init__(self, text, color="blue", size=30):
        super().__init__()
        self.text = text
        self.color = color
        self.size = size

    def _build(self):
        return ft.Container(
            width=self.size,
            height=self.size,
            bgcolor=self.color,
            border_radius=self.size / 2,
            alignment=ft.alignment.center,
            content=ft.Text(self.text, color="white", size=self.size * 0.4),
        )
    
def main(page: ft.Page):
    page.add(
        Badge("5", color="red", size=40),
        Badge("A", color="green", size=50),
    )

ft.run(main)

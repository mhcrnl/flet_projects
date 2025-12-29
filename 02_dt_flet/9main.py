import flet as ft

class CustomElevatedButton(ft.Control):
    def __init__(self, text, on_click=None, icon=None,
                 bgcolor=ft.Colors.BLUE, color="white"):
        super().__init__()
        self.text = text
        self.on_click = on_click
        self.icon = icon
        self.bgcolor = bgcolor
        self.color = color
        self.hovered = False

    # OBLIGATORIU pentru orice Control custom
    def _get_control_name(self):
        return "custom_elevated_button"

    def _build(self):
        # Efect de hover
        elevation = 8 if self.hovered else 2
        bg = ft.colors.with_opacity(0.90, self.bgcolor) if self.hovered else self.bgcolor

        # Construim lista de controale FĂRĂ None
        controls = []
        if self.icon:
            controls.append(ft.Icon(self.icon, color=self.color))
        controls.append(ft.Text(self.text, color=self.color, weight="bold"))

        content = ft.Row(
            controls=controls,
            spacing=8,
            alignment=ft.MainAxisAlignment.CENTER
        )

        return ft.Container(
            padding=12,
            bgcolor=bg,
            border_radius=8,
            alignment=ft.alignment.center,
            content=content,
            ink=True,
            shadow=ft.BoxShadow(
                blur_radius=elevation,
                spread_radius=0,
                color=ft.colors.with_opacity(0.3, "black")
            ),
            on_click=self.on_click,
            on_hover=self._on_hover,
            animate=ft.animation.Animation(150, "easeOut"),
        )

    def _on_hover(self, e):
        self.hovered = e.data == "true"
        self.update()


def main(page: ft.Page):

    def pressed(e):
        print("Ai apăsat butonul custom!")

    btn = CustomElevatedButton(
        "Apasă-mă",
        icon=ft.Icons.TOUCH_APP,
        bgcolor=ft.Colors.BLUE,
        color="white",
        on_click=pressed
    )

    page.add(
        ft.Text("ElevatedButton implementat cu Control", size=22, weight="bold"),
        btn
    )

ft.app(target=main)

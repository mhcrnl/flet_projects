import flet as ft

class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click=None, **kwargs):
        # apelăm constructorul original al ElevatedButton
        super().__init__(text=text, on_click=self._handle_click, **kwargs)

        # salvăm callback-ul real
        self._user_callback = on_click

        # stare internă
        self.click_count = 0

    def _handle_click(self, e):
        # comportament nou: numărăm click-urile
        self.click_count += 1
        print(f"Butonul a fost apăsat de {self.click_count} ori")

        # dacă utilizatorul a dat un callback, îl apelăm
        if self._user_callback:
            self._user_callback(e)


def main(page: ft.Page):

    def user_pressed(e):
        print("Callback-ul utilizatorului a fost apelat")

    btn = MyButton(
        "Apasă-mă",
        on_click=user_pressed,
        bgcolor=ft.Colors.BLUE,
        color="white",
        icon=ft.Icons.TOUCH_APP
    )

    page.add(
        ft.Text("Buton personalizat care moștenește TOT din ElevatedButton"),
        btn
    )

ft.app(target=main)

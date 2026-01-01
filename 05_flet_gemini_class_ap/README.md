# 05FletGeminiClassAp app

Pentru a păstra codul organizat, vom crea o clasă separată numită `HelpMenu`. Aceasta va gestiona fereastra de tip dialog (sau un "BottomSheet") care oferă informații utilizatorului.

Iată cum structurăm codul în două fișiere, adăugând componenta de Help:

### 1. `views.py` (Actualizat cu clasa HelpMenu)

Am adăugat clasa `HelpMenu` și am integrat-o în `MainView` printr-un buton în `AppBar`.

```python
import flet as ft

class HelpMenu:
    def __init__(self, page: ft.Page):
        self.page = page
        # Creăm dialogul de ajutor
        self.dialog = ft.AlertDialog(
            title=ft.Text("Centru de Ajutor"),
            content=ft.Text("Aceasta este o aplicație demonstrativă Flet.\n\n"
                            "1. Folosește butonul soare/lună pentru temă.\n"
                            "2. Meniul lateral oferă opțiuni extra."),
            actions=[
                ft.TextButton("Am înțeles", on_click=self.close_help)
            ],
        )

    def show_help(self, e):
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def close_help(self, e):
        self.dialog.open = False
        self.page.update()

class MainView:
    def __init__(self, page: ft.Page):
        self.page = page
        # Instanțiem meniul de help
        self.help_menu = HelpMenu(page)
        
        self.theme_button = ft.IconButton(
            icon=ft.icons.WB_SUNNY_OUTLINED, 
            on_click=self.toggle_theme
        )

    def toggle_theme(self, e):
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.theme_button.icon = ft.icons.DARK_MODE_OUTLINED
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.theme_button.icon = ft.icons.WB_SUNNY_OUTLINED
        self.page.update()

    def build_app_bar(self):
        return ft.AppBar(
            leading=ft.Icon(ft.icons.PALETTE),
            title=ft.Text("Aplicație Modulară"),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                self.theme_button,
                # Butonul care deschide clasa HelpMenu
                ft.IconButton(
                    icon=ft.icons.HELP_OUTLINE, 
                    on_click=self.help_menu.show_help
                ),
                ft.PopupMenuButton(
                    items=[ft.PopupMenuItem(text="Setări")]
                ),
            ],
        )

    def get_content(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.icons.ROCKET_LAUNCH, size=50, color=ft.colors.BLUE),
                    ft.Text("Structură cu Clase Separate", size=25, weight="bold"),
                    ft.Text("Apasă pe butonul '?' pentru ajutor"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.center
        )

```

---

### 2. `main.py` (Rămâne neschimbat)

Punctul de intrare rămâne curat, deoarece logica nouă este încapsulată în clase.

```python
import flet as ft
from views import MainView

def main(page: ft.Page):
    page.title = "Flet App - Help & Theme"
    page.theme_mode = ft.ThemeMode.DARK
    
    app_view = MainView(page)
    
    page.appbar = app_view.build_app_bar()
    page.add(app_view.get_content())
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

```

---

### Avantajele acestei abordări:

* **Responsabilitate unică:** Clasa `HelpMenu` se ocupă doar de textul de ajutor și de controlul dialogului. Dacă vrei să schimbi conținutul ajutorului, știi exact unde să mergi.
* **Reutilizare:** Poți folosi aceeași clasă `HelpMenu` pe mai multe pagini diferite fără a rescrie codul.
* **Curățenie în AppBar:** În loc să avem 20 de linii de cod pentru un dialog în interiorul funcției de construire a barei, avem doar un apel: `self.help_menu.show_help`.

Dorești să adăugăm și un **Navigation Drawer** (meniu lateral care glisează din stânga) pentru a naviga între diferite secțiuni ale aplicației?

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).
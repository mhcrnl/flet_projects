# 04FletGemini app

Pentru a implementa comutarea între **Light Mode** și **Dark Mode** într-o structură pe clase, cel mai bine este să adăugăm o metodă în clasa noastră care să gestioneze această logică și să actualizeze iconița butonului.

Iată cum modificăm cele două fișiere:

### 1. Modificări în `views.py`

Vom adăuga o metodă `toggle_theme` și vom actualiza butonul din `AppBar`.

```python
import flet as ft

class MainView:
    def __init__(self, page: ft.Page):
        self.page = page
        # Păstrăm referința la butonul de theme pentru a-i schimba iconița ulterior
        self.theme_button = ft.IconButton(
            icon=ft.icons.WB_SUNNY_OUTLINED, 
            tooltip="Schimbă tema",
            on_click=self.toggle_theme
        )

    def toggle_theme(self, e):
        # Logica de schimbare a temei
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
            title=ft.Text("Aplicația Mea Flet"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                self.theme_button, # Folosim butonul definit în __init__
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Setări"),
                    ]
                ),
            ],
        )

    def get_content(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Mod Vizualizare", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Apasă pe iconița din colțul dreapta sus pentru a schimba tema."),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.center
        )

```

### 2. Modificări în `main.py`

Aici trebuie doar să ne asigurăm că setăm o temă inițială (de exemplu, `DARK`) pentru ca metoda de toggle să știe de unde să înceapă.

```python
import flet as ft
from views import MainView

def main(page: ft.Page):
    page.title = "Flet Theme Switcher"
    
    # Setăm tema inițială explicit
    page.theme_mode = ft.ThemeMode.DARK
    
    app_view = MainView(page)
    
    page.appbar = app_view.build_app_bar()
    page.add(app_view.get_content())
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

```

### Ce s-a schimbat?

1. **Starea Butonului:** Am mutat definirea butonului de temă în `__init__` ca `self.theme_button`. Astfel, putem accesa proprietatea `.icon` oricând pentru a o schimba (din soare în lună și invers).
2. **Funcția `toggle_theme`:** Această funcție verifică valoarea actuală a `page.theme_mode` și o inversează.
3. **Update vizual:** După ce schimbăm tema, apelăm `self.page.update()` pentru ca utilizatorul să vadă schimbarea instantaneu.

Acum, când apeși pe iconița de lângă meniu, întreaga aplicație își va schimba culorile automat (fundalul, textele și AppBar-ul).

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
# 07FletDsApi app

Voi crea o aplicație Flet care integrează API-ul DeepSeek. Iată o implementare completă cu interfață pentru chat:

```python
import flet as ft
import httpx
import json
import asyncio
from datetime import datetime

class DeepSeekApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.api_key = ""
        self.chat_history = []
        self.setup_page()
        
    def setup_page(self):
        """Configurează pagina principală"""
        self.page.title = "DeepSeek AI Chat"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        self.page.bgcolor = ft.colors.GREY_50
        
        # Header
        self.header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.icons.ROCKET_LAUNCH, color=ft.colors.BLUE_600, size=30),
                    ft.Text("DeepSeek AI Assistant", 
                           size=28, 
                           weight=ft.FontWeight.BOLD,
                           color=ft.colors.BLUE_800),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.only(bottom=30)
        )
        
        # Câmp pentru API Key
        self.api_key_field = ft.TextField(
            label="API Key DeepSeek",
            password=True,
            can_reveal_password=True,
            hint_text="Introdu cheia ta API de la platform.deepseek.com",
            width=400,
            border_color=ft.colors.BLUE_400,
            on_submit=self.set_api_key
        )
        
        # Buton pentru setarea API Key
        self.api_key_button = ft.ElevatedButton(
            text="Setare API Key",
            icon=ft.icons.KEY,
            on_click=self.set_api_key,
            bgcolor=ft.colors.BLUE_600,
            color=ft.colors.WHITE
        )
        
        # Container pentru istoricul chat-ului
        self.chat_container = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=10,
        )
        
        # Câmp pentru mesaje noi
        self.message_field = ft.TextField(
            label="Scrie mesajul tău...",
            multiline=True,
            min_lines=1,
            max_lines=5,
            expand=True,
            border_color=ft.colors.BLUE_300,
            filled=True,
            fill_color=ft.colors.WHITE,
            on_submit=self.send_message
        )
        
        # Buton pentru trimitere mesaj
        self.send_button = ft.IconButton(
            icon=ft.icons.SEND,
            icon_color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_600,
            on_click=self.send_message,
            tooltip="Trimite mesaj"
        )
        
        # Rând pentru input
        input_row = ft.Row(
            controls=[
                self.message_field,
                self.send_button
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.END
        )
        
        # Buton pentru ștergerea istoricului
        self.clear_button = ft.ElevatedButton(
            text="Șterge Istoric",
            icon=ft.icons.DELETE,
            on_click=self.clear_chat,
            bgcolor=ft.colors.RED_400,
            color=ft.colors.WHITE
        )
        
        # Indicator de încărcare
        self.loading_indicator = ft.ProgressRing(
            visible=False,
            width=20,
            height=20
        )
        
        # Stare de conexiune
        self.status_text = ft.Text("Introdu cheia API pentru a începe", 
                                  color=ft.colors.GREY_600,
                                  italic=True)
        
        # Asamblează interfața
        self.page.add(
            self.header,
            ft.Row(
                controls=[
                    self.api_key_field,
                    self.api_key_button,
                    self.loading_indicator,
                    self.status_text
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Divider(height=20, color=ft.colors.TRANSPARENT),
            ft.Container(
                content=self.chat_container,
                expand=True,
                border=ft.border.all(1, ft.colors.BLUE_100),
                border_radius=10,
                padding=15,
                bgcolor=ft.colors.WHITE
            ),
            ft.Divider(height=10),
            input_row,
            ft.Row(
                controls=[self.clear_button],
                alignment=ft.MainAxisAlignment.END
            )
        )
        
    async def set_api_key(self, e):
        """Setează cheia API"""
        self.api_key = self.api_key_field.value.strip()
        if self.api_key:
            self.status_text.value = "API Key setat cu succes!"
            self.status_text.color = ft.colors.GREEN_600
            self.api_key_field.border_color = ft.colors.GREEN_400
            await self.add_message("system", "Bună! Sunt asistentul DeepSeek AI. Cu ce te pot ajuta?")
        else:
            self.status_text.value = "Introdu o cheie API validă"
            self.status_text.color = ft.colors.RED_600
        self.page.update()
    
    async def send_message(self, e):
        """Trimite mesajul către API-ul DeepSeek"""
        message = self.message_field.value.strip()
        if not message or not self.api_key:
            if not self.api_key:
                self.status_text.value = "Setează mai întâi API Key!"
                self.status_text.color = ft.colors.RED_600
            return
        
        # Adaugă mesajul utilizatorului
        await self.add_message("user", message)
        self.message_field.value = ""
        
        # Afișează indicatorul de încărcare
        self.loading_indicator.visible = True
        self.status_text.value = "Se procesează..."
        self.page.update()
        
        try:
            # Pregătește istoricul pentru API
            messages = [
                {"role": "system", "content": "Ești un asistent AI util, prietenos și detaliat."}
            ]
            
            # Adaugă istoricul conversației (ultimele 10 mesaje pentru context)
            for msg in self.chat_history[-10:]:
                messages.append({"role": msg["role"], "content": msg["content"]})
            
            # Adaugă mesajul curent
            messages.append({"role": "user", "content": message})
            
            # Face cererea către API-ul DeepSeek
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    "https://api.deepseek.com/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "deepseek-chat",
                        "messages": messages,
                        "stream": False,
                        "max_tokens": 2000
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    ai_response = data["choices"][0]["message"]["content"]
                    
                    # Adaugă răspunsul AI
                    await self.add_message("assistant", ai_response)
                    
                    self.status_text.value = "Gata!"
                    self.status_text.color = ft.colors.GREEN_600
                    
                else:
                    error_msg = f"Eroare API: {response.status_code}"
                    if response.text:
                        try:
                            error_data = response.json()
                            error_msg = f"Eroare: {error_data.get('error', {}).get('message', error_msg)}"
                        except:
                            error_msg = f"Eroare: {response.text[:100]}"
                    
                    await self.add_message("system", f"❌ {error_msg}")
                    self.status_text.value = "Eroare la conexiune"
                    self.status_text.color = ft.colors.RED_600
                    
        except httpx.TimeoutException:
            await self.add_message("system", "⏰ Timeout: Cererea a durat prea mult")
            self.status_text.value = "Timeout"
            self.status_text.color = ft.colors.RED_600
            
        except Exception as ex:
            await self.add_message("system", f"❌ Eroare neașteptată: {str(ex)}")
            self.status_text.value = "Eroare"
            self.status_text.color = ft.colors.RED_600
            
        finally:
            # Ascunde indicatorul de încărcare
            self.loading_indicator.visible = False
            self.page.update()
    
    async def add_message(self, role: str, content: str):
        """Adaugă un mesaj în chat"""
        timestamp = datetime.now().strftime("%H:%M")
        
        # Stochează în istoric
        self.chat_history.append({
            "role": role,
            "content": content,
            "time": timestamp
        })
        
        # Creează container pentru mesaj
        if role == "user":
            message_card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.icons.PERSON, color=ft.colors.BLUE_600, size=16),
                        ft.Text("Tu", weight=ft.FontWeight.BOLD, size=12),
                        ft.Text(timestamp, size=10, color=ft.colors.GREY_500)
                    ]),
                    ft.Text(content, color=ft.colors.BLUE_900)
                ]),
                padding=10,
                border_radius=10,
                bgcolor=ft.colors.BLUE_50,
                border=ft.border.all(1, ft.colors.BLUE_100),
                margin=ft.margin.only(left=60, bottom=5)
            )
        elif role == "assistant":
            message_card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.icons.SMART_TOY, color=ft.colors.GREEN_600, size=16),
                        ft.Text("DeepSeek AI", weight=ft.FontWeight.BOLD, size=12),
                        ft.Text(timestamp, size=10, color=ft.colors.GREY_500)
                    ]),
                    ft.Text(content, color=ft.colors.GREY_900)
                ]),
                padding=10,
                border_radius=10,
                bgcolor=ft.colors.GREEN_50,
                border=ft.border.all(1, ft.colors.GREEN_100),
                margin=ft.margin.only(right=60, bottom=5)
            )
        else:  # system messages
            message_card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.icons.INFO, color=ft.colors.ORANGE_600, size=16),
                        ft.Text("Sistem", weight=ft.FontWeight.BOLD, size=12),
                        ft.Text(timestamp, size=10, color=ft.colors.GREY_500)
                    ]),
                    ft.Text(content, color=ft.colors.ORANGE_800, italic=True)
                ]),
                padding=10,
                border_radius=10,
                bgcolor=ft.colors.ORANGE_50,
                border=ft.border.all(1, ft.colors.ORANGE_100),
                alignment=ft.alignment.center
            )
        
        # Adaugă mesajul în container
        self.chat_container.controls.append(message_card)
        
        # Derulează la ultimul mesaj
        self.page.update()
        await self.page.scroll_to_async(offset=-1, duration=300)
    
    async def clear_chat(self, e):
        """Șterge istoricul conversației"""
        self.chat_container.controls.clear()
        self.chat_history.clear()
        await self.add_message("system", "Conversația a fost ștearsă. Cu ce te pot ajuta?")
        self.page.update()

async def main(page: ft.Page):
    """Funcția principală a aplicației"""
    app = DeepSeekApp(page)

if __name__ == "__main__":
    ft.app(target=main)
```

## Instrucțiuni de instalare și utilizare:

### 1. **Instalare dependențe**:
```bash
pip install flet httpx
```

### 2. **Obținere API Key**:
- Vizitează [platform.deepseek.com](https://platform.deepseek.com/)
- Creează un cont (dacă nu ai deja)
- Mergi la secțiunea "API Keys" și generează o cheie nouă
- Copiază cheia API

### 3. **Funcționalități ale aplicației**:

- **Interfață prietenoasă** cu design modern
- **Istoric conversații** cu marcaje de timp
- **Indicator de încărcare** pentru feedback vizual
- **Management erori** cu mesaje informative
- **Securitate**: API Key este ascuns (password field)
- **Ștergere istoric** cu un singur click
- **Suport pentru mesaje lungi** cu scroll

### 4. **Caracteristici tehnice**:

- Folosește API-ul oficial DeepSeek Chat
- Model: `deepseek-chat`
- Timeout: 30 secunde pentru răspunsuri
- Limită: 2000 tokeni per răspuns
- Păstrează ultimele 10 mesaje pentru context

### 5. **Rulare aplicație**:
```bash
python deepseek_app.py
```

### 6. **Notă importantă**:
Aplicația folosește planul gratuit de la DeepSeek (dacă este disponibil). Verifică limitările și costurile pe platforma DeepSeek pentru utilizarea API-ului.

### 7. **Personalizare**:
Poți modifica următoarele aspecte în cod:
- Schimbă `max_tokens` pentru răspunsuri mai lungi/scurte
- Modifică culorile în secțiunile `ft.colors`
- Adaugă mai multe modele dacă ai acces (schimbă `deepseek-chat`)

Aplicația este gata de utilizare și oferă o experiență completă de chat cu AI-ul DeepSeek!

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
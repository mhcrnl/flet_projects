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
        self.page.bgcolor = ft.Colors.GREY_50
        
        # Header
        self.header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.ROCKET_LAUNCH, color=ft.Colors.BLUE_600, size=30),
                    ft.Text("DeepSeek AI Assistant", 
                           size=28, 
                           weight=ft.FontWeight.BOLD,
                           color=ft.Colors.BLUE_800),
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
            border_color=ft.Colors.BLUE_400,
            on_submit=self.set_api_key
        )
        
        # Buton pentru setarea API Key
        self.api_key_button = ft.ElevatedButton(
            text="Setare API Key",
            icon=ft.Icons.KEY,
            on_click=self.set_api_key,
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE
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
            border_color=ft.Colors.BLUE_300,
            filled=True,
            fill_color=ft.Colors.WHITE,
            on_submit=self.send_message
        )
        
        # Buton pentru trimitere mesaj
        self.send_button = ft.IconButton(
            icon=ft.Icons.SEND,
            icon_color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE_600,
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
            icon=ft.Icons.DELETE,
            on_click=self.clear_chat,
            bgcolor=ft.Colors.RED_400,
            color=ft.Colors.WHITE
        )
        
        # Indicator de încărcare
        self.loading_indicator = ft.ProgressRing(
            visible=False,
            width=20,
            height=20
        )
        
        # Stare de conexiune
        self.status_text = ft.Text("Introdu cheia API pentru a începe", 
                                  color=ft.Colors.GREY_600,
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
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Container(
                content=self.chat_container,
                expand=True,
                border=ft.border.all(1, ft.Colors.BLUE_100),
                border_radius=10,
                padding=15,
                bgcolor=ft.Colors.WHITE
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
            self.status_text.color = ft.Colors.GREEN_600
            self.api_key_field.border_color = ft.Colors.GREEN_400
            await self.add_message("system", "Bună! Sunt asistentul DeepSeek AI. Cu ce te pot ajuta?")
        else:
            self.status_text.value = "Introdu o cheie API validă"
            self.status_text.color = ft.Colors.RED_600
        self.page.update()
    
    async def send_message(self, e):
        """Trimite mesajul către API-ul DeepSeek"""
        message = self.message_field.value.strip()
        if not message or not self.api_key:
            if not self.api_key:
                self.status_text.value = "Setează mai întâi API Key!"
                self.status_text.color = ft.Colors.RED_600
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
                    self.status_text.color = ft.Colors.GREEN_600
                    
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
                    self.status_text.color = ft.Colors.RED_600
                    
        except httpx.TimeoutException:
            await self.add_message("system", "⏰ Timeout: Cererea a durat prea mult")
            self.status_text.value = "Timeout"
            self.status_text.color = ft.Colors.RED_600
            
        except Exception as ex:
            await self.add_message("system", f"❌ Eroare neașteptată: {str(ex)}")
            self.status_text.value = "Eroare"
            self.status_text.color = ft.Colors.RED_600
            
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
                        ft.Icon(ft.Icons.PERSON, color=ft.Colors.BLUE_600, size=16),
                        ft.Text("Tu", weight=ft.FontWeight.BOLD, size=12),
                        ft.Text(timestamp, size=10, color=ft.Colors.GREY_500)
                    ]),
                    ft.Text(content, color=ft.Colors.BLUE_900)
                ]),
                padding=10,
                border_radius=10,
                bgcolor=ft.Colors.BLUE_50,
                border=ft.border.all(1, ft.Colors.BLUE_100),
                margin=ft.margin.only(left=60, bottom=5)
            )
        elif role == "assistant":
            message_card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.SMART_TOY, color=ft.Colors.GREEN_600, size=16),
                        ft.Text("DeepSeek AI", weight=ft.FontWeight.BOLD, size=12),
                        ft.Text(timestamp, size=10, color=ft.Colors.GREY_500)
                    ]),
                    ft.Text(content, color=ft.Colors.GREY_900)
                ]),
                padding=10,
                border_radius=10,
                bgcolor=ft.colors.GREEN_50,
                border=ft.border.all(1, ft.Colors.GREEN_100),
                margin=ft.margin.only(right=60, bottom=5)
            )
        else:  # system messages
            message_card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.INFO, color=ft.Colors.ORANGE_600, size=16),
                        ft.Text("Sistem", weight=ft.FontWeight.BOLD, size=12),
                        ft.Text(timestamp, size=10, color=ft.Colors.GREY_500)
                    ]),
                    ft.Text(content, color=ft.Colors.ORANGE_800, italic=True)
                ]),
                padding=10,
                border_radius=10,
                bgcolor=ft.Colors.ORANGE_50,
                border=ft.border.all(1, ft.Colors.ORANGE_100),
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

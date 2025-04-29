import flet as ft

def main(page: ft.Page):
    page.title = "Окно без кнопки"


    page.add(ft.Text("Кнопки нет!"))  # Добавляем текст на экран




ft.app(target=main)
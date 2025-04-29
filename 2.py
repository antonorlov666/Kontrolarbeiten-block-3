import flet as ft

def main(page: ft.Page):
    page.title = "Окно с кнопкой"

    def on_click(e):  # Функция, вызываемая при нажатии
        page.add(ft.Text("Кнопка есть!"))  # Добавляем текст на экран

    page.add(ft.Text("Кнопки нет!"))  # Добавляем текст на экран
    button = ft.ElevatedButton("Нажми меня", on_click=on_click)

    page.add(button)  # Добавляем кнопку на страницу

ft.app(target=main)
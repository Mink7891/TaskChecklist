# pip install flet

import flet as ft


def main(page: ft.Page):
    page.title = "Чек-лист задач"
    page.vertical_alignment = ft.MainAxisAlignment.START

    tasks = []
    text = ''

    text_error = ft.Text(color='#FF0000', size=20)

    task_input = ft.TextField(
        hint_text="Добавьте задачу...",
        width=300,
    )

    def add_task(e):
        if task_input.value:
            if len(task_input.value) <= 30:
                text_error.value = ""
                task = ft.Row(
                    [
                        ft.Text(task_input.value),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=lambda e: remove_task(task),
                        ),
                    ]
                )
                tasks.append(task)
                task_list.controls.append(task)
                task_input.value = ""
            else:
                text_error.value = "Слишком длинная задача"
            page.update()

    def remove_task(task):
        task_list.controls.remove(task)
        page.update()

    add_button = ft.FloatingActionButton(
        text="Добавить",
        on_click=add_task,
        width=150
    )

    task_list = ft.Column()

    page.add(
        ft.Row([text_error], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([task_input, add_button],
               alignment=ft.MainAxisAlignment.CENTER),
        task_list,
    )


ft.app(target=main)

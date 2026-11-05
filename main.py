"""
AI Applications Using Python — AI 04 Matplotlib Homework
Главный исполняемый скрипт для запуска всех 3 заданий.
"""

from tasks.task1_temperature import run_task1
from tasks.task2_languages import run_task2
from tasks.task3_students_scatter import run_task3


def main():
    print("\n" + "#" * 65)
    print("#  КУРС: AI Applications Using Python")
    print("#  МОДУЛЬ: AI 04 — Matplotlib Домашние задания")
    print("#" * 65 + "\n")

    # 1. Задание 1
    run_task1(save_path="output/task1_temperature.png", show=False)
    print("\n" + "-" * 60 + "\n")

    # 2. Задание 2
    run_task2(
        save_path_horizontal="output/task2_languages_horizontal.png",
        save_path_vertical="output/task2_languages_vertical.png",
        show=False,
    )
    print("\n" + "-" * 60 + "\n")

    # 3. Задание 3
    run_task3(save_path="output/task3_students_scatter.png", show=False)
    print("\n" + "#" * 65)
    print("#  Все 3 задания успешно выполнены!")
    print("#  Сгенерированные графики сохранены в папке output/")
    print("#" * 65 + "\n")


if __name__ == "__main__":
    main()

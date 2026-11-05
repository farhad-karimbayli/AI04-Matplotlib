"""
Домашнее задание 2: Сравнение языков программирования
- Покажите количество студентов по языкам программирования на горизонтальной столбчатой диаграмме.
- Данные:
    languages = ["Python", "JavaScript", "Java", "C#", "C++"]
    students = [35, 28, 22, 18, 15]
- Требования:
    • Создайте горизонтальную столбчатую диаграмму с помощью barh()
    • Используйте отдельный цвет для каждого столбца.
    • Подпишите оси X и Y и добавьте заголовок.
    • В конце каждого столбца покажите количество студентов с помощью plt.text()
    • Визуально выделите язык с наибольшим числом студентов.
    • Измените размер графика с помощью figsize.
- Дополнительно:
    • Также покажите эти данные на отдельной вертикальной столбчатой диаграмме с помощью plt.bar()
"""

from pathlib import Path
import matplotlib.pyplot as plt


def run_task2(
    save_path_horizontal: str = "output/task2_languages_horizontal.png",
    save_path_vertical: str = "output/task2_languages_vertical.png",
    show: bool = False,
):
    print("=" * 60)
    print("ЗАДАНИЕ 2: Столбчатые диаграммы «Сравнение языков программирования»")
    print("=" * 60)

    # Исходные данные
    languages = ["Python", "JavaScript", "Java", "C#", "C++"]
    students = [35, 28, 22, 18, 15]

    # Для горизонтальной диаграммы развернем порядок, чтобы самый популярный язык был вверху
    langs_h = languages[::-1]
    studs_h = students[::-1]

    # Цветовая палитра: отдельный цвет для каждого столбца,
    # а лидер (Python) визуально выделен акцентным цветом и рамкой
    max_val = max(studs_h)
    colors_h = [
        "#ff9f1c" if val == max_val else "#4361ee"
        for val in studs_h
    ]
    edge_colors = [
        "#b25900" if val == max_val else "none"
        for val in studs_h
    ]
    line_widths = [2.5 if val == max_val else 0 for val in studs_h]

    # -------------------------------------------------------------
    # 1. Горизонтальная столбчатая диаграмма (plt.barh)
    # -------------------------------------------------------------
    fig_h, ax_h = plt.subplots(figsize=(10, 6))

    bars = ax_h.barh(
        langs_h,
        studs_h,
        color=colors_h,
        edgecolor=edge_colors,
        linewidth=line_widths,
        height=0.65,
    )

    # Подписи осей и заголовок
    ax_h.set_title("Популярность языков программирования среди студентов (barh)", fontsize=14, fontweight="bold", pad=15)
    ax_h.set_xlabel("Количество студентов", fontsize=12, labelpad=10)
    ax_h.set_ylabel("Языки программирования", fontsize=12, labelpad=10)

    # Запас по оси X для текстовых меток справа
    ax_h.set_xlim(0, max_val + 5)

    # Сетка по оси X
    ax_h.grid(axis="x", linestyle="--", alpha=0.5)

    # Отображение значений в конце каждого столбца через plt.text()
    for i, val in enumerate(studs_h):
        is_leader = (val == max_val)
        label_text = f"{val} студ. (Лидер)" if is_leader else f"{val}"
        ax_h.text(
            x=val + 0.6,
            y=i,
            s=label_text,
            va="center",
            fontsize=10,
            fontweight="bold" if is_leader else "normal",
            color="#b25900" if is_leader else "#222222",
        )

    if save_path_horizontal:
        out_h = Path(save_path_horizontal)
        out_h.parent.mkdir(parents=True, exist_ok=True)
        fig_h.savefig(out_h, dpi=300, bbox_inches="tight")
        print(f"Горизонтальная диаграмма сохранена: {out_h.resolve()}")

    if show:
        plt.show()
    plt.close(fig_h)

    # -------------------------------------------------------------
    # 2. Дополнительно: Вертикальная столбчатая диаграмма (plt.bar)
    # -------------------------------------------------------------
    fig_v, ax_v = plt.subplots(figsize=(10, 6))

    # Палитра для вертикальной диаграммы (исходный порядок)
    colors_v = ["#ff9f1c", "#4361ee", "#3a0ca3", "#7209b7", "#f72585"]

    bars_v = ax_v.bar(
        languages,
        students,
        color=colors_v,
        edgecolor="black",
        linewidth=1.2,
        width=0.55,
    )

    # Выделение столбца Python более жирной золотой рамкой
    bars_v[0].set_linewidth(2.8)
    bars_v[0].set_edgecolor("#b25900")

    ax_v.set_title("Сравнение языков программирования (вертикальная диаграмма bar)", fontsize=14, fontweight="bold", pad=15)
    ax_v.set_xlabel("Языки программирования", fontsize=12, labelpad=10)
    ax_v.set_ylabel("Количество студентов", fontsize=12, labelpad=10)
    ax_v.set_ylim(0, max(students) + 6)
    ax_v.grid(axis="y", linestyle="--", alpha=0.5)

    # Подписи значений над каждым столбцом через plt.text()
    for i, val in enumerate(students):
        ax_v.text(
            x=i,
            y=val + 0.8,
            s=f"{val}",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
            color="#222222",
        )

    if save_path_vertical:
        out_v = Path(save_path_vertical)
        out_v.parent.mkdir(parents=True, exist_ok=True)
        fig_v.savefig(out_v, dpi=300, bbox_inches="tight")
        print(f"Вертикальная диаграмма сохранена: {out_v.resolve()}")

    if show:
        plt.show()
    plt.close(fig_v)


if __name__ == "__main__":
    run_task2(show=False)

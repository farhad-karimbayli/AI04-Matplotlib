"""
Домашнее задание 3: Анализ результатов студентов
- Проанализируйте часы учёбы, результаты экзамена и возраст на диаграмме рассеяния.
- Данные:
    study_hours = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8]
    scores = [45, 50, 55, 60, 65, 70, 74, 80, 88, 95]
    ages = [18, 19, 18, 20, 21, 19, 22, 20, 23, 21]
- Требования:
    • Используйте fig = plt.figure() и fig.add_axes(...)
    • Создайте диаграмму рассеяния для study_hours и scores.
    • Цвет точек должен зависеть от ages; используйте cmap.
    • Используйте параметры marker и s.
    • Добавьте colorbar с подписью Age.
    • Подпишите ось X: Study Hours, ось Y: Exam Score.
    • Добавьте сетку и подходящий заголовок.
    • Отдельно отметьте точку с наивысшим результатом.
- Дополнительно:
    • В той же Figure создайте вторую небольшую область Axes и
      покажите данные scores в виде столбчатой диаграммы.
"""

from pathlib import Path
import matplotlib.pyplot as plt


def run_task3(save_path: str = "output/task3_students_scatter.png", show: bool = False):
    print("=" * 60)
    print("ЗАДАНИЕ 3: Диаграмма рассеяния «Анализ результатов студентов»")
    print("=" * 60)

    # Исходные данные
    study_hours = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8]
    scores = [45, 50, 55, 60, 65, 70, 74, 80, 88, 95]
    ages = [18, 19, 18, 20, 21, 19, 22, 20, 23, 21]

    # 1. Создаем объект Figure
    fig = plt.figure(figsize=(11, 7))

    # 2. Основная область Axes через add_axes: [left, bottom, width, height]
    ax_main = fig.add_axes((0.1, 0.12, 0.75, 0.78))

    # 3. Диаграмма рассеяния:
    # - study_hours по оси X, scores по оси Y
    # - цвет c=ages, цветовая карта cmap='plasma'
    # - размер s=140, маркер marker='o'
    scatter = ax_main.scatter(
        study_hours,
        scores,
        c=ages,
        cmap="plasma",
        s=140,
        marker="o",
        edgecolors="black",
        linewidths=1.2,
        alpha=0.9,
    )

    # 4. Colorbar с подписью Age
    cbar = fig.colorbar(scatter, ax=ax_main, fraction=0.046, pad=0.04)
    cbar.set_label("Возраст студента (Age)", fontsize=11, labelpad=10)

    # 5. Подписи осей и заголовок
    ax_main.set_title("Зависимость балла на экзамене от часов подготовки", fontsize=14, fontweight="bold", pad=15)
    ax_main.set_xlabel("Study Hours (Часы подготовки)", fontsize=12, labelpad=10)
    ax_main.set_ylabel("Exam Score (Балл экзамена)", fontsize=12, labelpad=10)

    # Настройки пределов и сетки
    ax_main.set_xlim(0, 9)
    ax_main.set_ylim(40, 102)
    ax_main.grid(True, linestyle="--", alpha=0.5)

    # 6. Отдельно отмечаем точку с наивысшим результатом
    max_score = max(scores)
    max_idx = scores.index(max_score)
    top_x = study_hours[max_idx]
    top_y = scores[max_idx]

    # Выделяем точку золотой звездой
    ax_main.scatter(
        top_x,
        top_y,
        color="#ffd700",
        s=280,
        marker="*",
        edgecolors="black",
        linewidths=1.5,
        zorder=5,
        label=f"Максимум: {max_score} баллов",
    )

    # Добавляем аннотирующую стрелку к наивысшему результату
    ax_main.annotate(
        f"Наивысший балл!\nScore: {max_score}, Hours: {top_x}",
        xy=(top_x, top_y),
        xytext=(top_x - 3.2, top_y - 2),
        arrowprops=dict(
            facecolor="black",
            shrink=0.08,
            width=1.5,
            headwidth=8,
        ),
        fontsize=10,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff3cd", edgecolor="#ffeeba", alpha=0.9),
    )
    ax_main.legend(loc="lower right", frameon=True)

    # -------------------------------------------------------------
    # 7. ДОПОЛНИТЕЛЬНО: Вторая область Axes внутри той же Figure
    #    для отображения столбчатой диаграммы баллов
    # -------------------------------------------------------------
    ax_inset = fig.add_axes((0.17, 0.58, 0.28, 0.26))
    student_ids = [f"S{i+1}" for i in range(len(scores))]

    # Цвета столбиков для inset диаграммы
    bar_colors = ["#4cc9f0" if s != max_score else "#ffd700" for s in scores]
    ax_inset.bar(student_ids, scores, color=bar_colors, edgecolor="black", linewidth=0.8)
    ax_inset.set_title("Баллы по студентам (Scores)", fontsize=9, fontweight="bold")
    ax_inset.set_xlabel("Студент", fontsize=8)
    ax_inset.set_ylabel("Балл", fontsize=8)
    ax_inset.tick_params(axis="both", labelsize=7)
    ax_inset.set_ylim(0, 110)
    ax_inset.grid(axis="y", linestyle=":", alpha=0.5)

    # Сохранение графика
    if save_path:
        out_file = Path(save_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_file, dpi=300, bbox_inches="tight")
        print(f"Диаграмма рассеяния сохранена: {out_file.resolve()}")

    if show:
        plt.show()

    plt.close(fig)


if __name__ == "__main__":
    run_task3(show=False)

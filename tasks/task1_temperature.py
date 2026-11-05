"""
Домашнее задание 1: Температура за неделю
- Постройте линейный график на основе данных о температуре за 7 дней.
- Данные:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    temperature = [18, 20, 22, 21, 24, 26, 23]
- Требования:
    • Постройте график с помощью plt.plot()
    • По оси X покажите дни, по оси Y - температуру.
    • Добавьте заголовок графика.
    • Используйте marker и измените стиль линии.
    • Добавьте сетку (grid).
    • Над каждой точкой покажите значение температуры.
    • Измените размер графика с помощью figsize.
"""

from pathlib import Path
import matplotlib.pyplot as plt


def run_task1(save_path: str = "output/task1_temperature.png", show: bool = False):
    print("=" * 60)
    print("ЗАДАНИЕ 1: Линейный график «Температура за неделю»")
    print("=" * 60)

    # Исходные данные
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    temperature = [18, 20, 22, 21, 24, 26, 23]

    # Настройка размера графика с помощью figsize
    fig, ax = plt.subplots(figsize=(10, 6))

    # Построение графика: линия пунктиром, стильный маркер круга, толщина линии
    ax.plot(
        days,
        temperature,
        color="#2b5c8f",
        linestyle="--",
        linewidth=2.5,
        marker="o",
        markersize=9,
        markerfacecolor="#ff7f0e",
        markeredgecolor="#2b5c8f",
        markeredgewidth=2,
        label="Дневная температура",
    )

    # Подписи осей и заголовок
    ax.set_title("Динамика температуры за неделю", fontsize=15, fontweight="bold", pad=15)
    ax.set_xlabel("Дни недели", fontsize=12, labelpad=10)
    ax.set_ylabel("Температура (°C)", fontsize=12, labelpad=10)

    # Настройка пределов оси Y с запасом для текстовых меток сверху
    ax.set_ylim(min(temperature) - 3, max(temperature) + 3)

    # Добавление сетки
    ax.grid(True, linestyle=":", alpha=0.6, color="gray")

    # Отображение значения температуры над каждой точкой
    for day, temp in zip(days, temperature):
        ax.text(
            x=day,
            y=temp + 0.45,
            s=f"{temp}°C",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
            color="#1f3b5c",
        )

    # Легенда
    ax.legend(loc="upper left", frameon=True)

    # Сохранение результата
    if save_path:
        out_file = Path(save_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(out_file, dpi=300, bbox_inches="tight")
        print(f"График успешно сохранен: {out_file.resolve()}")

    if show:
        plt.show()

    plt.close(fig)


if __name__ == "__main__":
    run_task1(show=False)

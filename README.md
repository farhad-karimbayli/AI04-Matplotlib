# Практические задания по визуализации данных с Matplotlib (AI 04)

Репозиторий учебного курса: [AI-Applications-Using-Python-FSDE_Oct_24_3_ru](https://github.com/Zamanof/AI-Applications-Using-Python-FSDE_Oct_24_3_ru)  
Модуль: **AI 04 — Matplotlib**  
Задания: [AI_04_Matplotlib_Domashnie_Zadaniya_RU.pdf](docs/AI_04_Matplotlib.pdf)

---

## 📁 Структура проекта

```text
AI04/
├── docs/
│   └── AI_04_Matplotlib.pdf         # Исходный PDF с заданием от IT Step
├── tasks/
│   ├── __init__.py
│   ├── task1_temperature.py         # Задание 1: Линейный график температуры за неделю
│   ├── task2_languages.py           # Задание 2: Столбчатые диаграммы языков программирования (barh + bar)
│   └── task3_students_scatter.py    # Задание 3: Scatter plot (study_hours vs scores) + вложенный Axes
├── output/
│   ├── task1_temperature.png        # Экспортированный график температуры
│   ├── task2_languages_horizontal.png # Горизонтальная диаграмма языков
│   ├── task2_languages_vertical.png   # Вертикальная диаграмма языков
│   └── task3_students_scatter.png   # Диаграмма рассеяния со вложенным графиком
├── main.py                          # Общий запускаемый скрипт для всех заданий
├── solutions.ipynb                  # Интерактивный Jupyter Notebook с решениями
├── requirements.txt                 # Зависимости проекта (matplotlib, numpy)
└── README.md                        # Описание и разбор решений
```

---

## 🚀 Установка и запуск

### 1. Виртуальное окружение
С помощью `uv`:
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```
Либо через стандартный `python3 -m venv`:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Запуск скриптов
- **Запуск всех заданий сразу (с сохранением картинок в `output/`):**
  ```bash
  python main.py
  ```
- **Запуск любого отдельного задания:**
  ```bash
  python tasks/task1_temperature.py
  python tasks/task2_languages.py
  python tasks/task3_students_scatter.py
  ```
- **Интерактивный Jupyter Notebook:**
  ```bash
  jupyter notebook solutions.ipynb
  ```

---

## 🎨 Подробный разбор каждого задания

### Задание 1: Линейный график «Температура за неделю»
- **Исходные данные:**
  - `days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]`
  - `temperature = [18, 20, 22, 21, 24, 26, 23]`
- **Реализованные требования:**
  - Построение линии через `plt.plot(days, temperature)`.
  - Маркеры точек (`marker='o'`) с индивидуальным цветом заливки и окантовки.
  - Кастомизация стиля линии: пунктир (`linestyle='--'`) и увеличенная толщина (`linewidth=2.5`).
  - Отображение сетки `plt.grid(True, linestyle=':', alpha=0.6)`.
  - Вывод числового значения температуры над каждой вершиной графика с помощью `plt.text(day, temp + 0.45, f"{temp}°C", ha='center')`.
  - Управление размером полотна через `figsize=(10, 6)`.
  - Настройка подписей осей X, Y, заголовка и легенды.

### Задание 2: Сравнение языков программирования
- **Исходные данные:**
  - `languages = ["Python", "JavaScript", "Java", "C#", "C++"]`
  - `students = [35, 28, 22, 18, 15]`
- **Реализованные требования:**
  - Горизонтальная столбчатая диаграмма с помощью `plt.barh()`.
  - Индивидуальная цветовая палитра для каждого столбца.
  - Визуальное выделение языка-лидера (Python): акцентный золотисто-оранжевый цвет и утолщенная рамка.
  - Подписи значений студентов на концах столбцов с помощью `plt.text(val + 0.6, i, str(val), va='center')`.
  - **Дополнительно:** Построена вертикальная диаграмма `plt.bar()` с подписями над столбцами и выделением лидера.

### Задание 3: Анализ результатов студентов
- **Исходные данные:**
  - `study_hours = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8]`
  - `scores = [45, 50, 55, 60, 65, 70, 74, 80, 88, 95]`
  - `ages = [18, 19, 18, 20, 21, 19, 22, 20, 23, 21]`
- **Реализованные требования:**
  - Использование объектно-ориентированного API Matplotlib: `fig = plt.figure()` и `fig.add_axes([left, bottom, width, height])`.
  - Диаграмма рассеяния `ax.scatter(study_hours, scores, c=ages, cmap='plasma', s=140, marker='o')`.
  - Цветовая шкала `colorbar` с подписью `'Age'`.
  - Выделение студента с максимальным баллом (95) отдельным маркером-звездой (`marker='*'`) и аннотирующей стрелкой (`ax.annotate(...)`).
  - **Дополнительно:** Создана вторая вложенная область Axes (`ax_inset = fig.add_axes([0.17, 0.58, 0.28, 0.26])`) со столбчатой диаграммой распределения баллов студентов.

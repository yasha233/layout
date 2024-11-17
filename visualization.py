import matplotlib.pyplot as plt
import os


def draw_histogram(name, data):
    """
    Рисует гистограмму на основе переданных данных.

    Параметры:
    name (str): Название гистограммы, которое будет отображено в заголовке.
    data (dict): Словарь, где ключи - это метки (например, названия пальцев),
                 а значения - это количество нажатий (например, количество нажатий каждым пальцем).

    Возвращает:
    None
    """
    dict1 = data[0]
    dict2 = data[1]
    keys = list(dict1.keys())
    values1 = list(dict1.values())
    values2 = list(dict2.values())
    width = 0.35  # Ширина баров
    x = range(len(keys))  # Позиции по оси X
    file_size = os.path.getsize(name)
    file_name = os.path.basename(name)
    # создание гистограммы
    fig, ax = plt.subplots()

    # Рисуем бары для первого словаря
    rects1 = ax.barh([pos - width / 2 for pos in x], values1, width, label='йцукен', color='black')

    # Рисуем бары для второго словаря
    rects2 = ax.barh([pos + width / 2 for pos in x], values2, width, label='diktor', color='orange')
    # Настройка осей
    for i in range(len(keys)):
        if values1[i] != 0:
            xpos = values1[i]
        else:
            xpos = values2[i]
        ax.text(xpos + 0.1, x[i] - width / 2 - 0.1, str(abs(values1[i] - values2[i])), ha='center', va='bottom')
    ax.set_yticks(x)
    ax.set_yticklabels(keys)
    ax.set_xlabel('Количество нажатий')
    ax.set_title(str(file_name) + '    ' + str(file_size) + ' MB')
    ax.legend()
    plt.show()

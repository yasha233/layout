import matplotlib.pyplot as plt
import os


def draw_histogram(path, data):
    """
    Рисует гистограмму на основе переданных данных.

    Параметры:
    path (str): Путь к файлу, из которого берутся данные.
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
    width = 0.2  # Ширина баров
    x = range(len(keys))  # Позиции по оси X
    file_size = os.path.getsize(path)
    file_name = os.path.basename(path)
    # создание гистограммы
    fig, ax = plt.subplots(figsize=(16, 8))

    # Рисуем бары для первого словаря
    rects1 = ax.barh([pos + width / 2 for pos in x], values1, width, label='йцукен', color='red')

    # Рисуем бары для второго словаря
    rects2 = ax.barh([pos - width / 2 for pos in x], values2, width, label='diktor', color='green')
    # Настройка осей
    for i in range(len(keys)):
        if values1[i] != 0:
            xpos = values1[i]
        else:
            xpos = values2[i]
        ax.text(xpos + 0.1, x[i] - width / 2, str(abs(values1[i] - values2[i])), ha='center', va='bottom')
        # ax.bar_label(rects1, str(abs(values1[i] - values2[i])))
    ax.set_yticks(x)
    ax.set_yticklabels(keys)
    ax.set_ylabel('Пальцы')
    ax.set_xlabel('Количество нажатий')
    ax.set_title(str(file_name) + '    ' + str(file_size) + ' MB')
    ax.legend()

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.show()

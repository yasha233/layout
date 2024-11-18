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
    dict3 = data[2]
    keys = list(dict1.keys())
    values1 = list(dict1.values())
    values2 = list(dict2.values())
    values3 = list(dict3.values())
    width = 0.2  # Ширина баров
    x = range(len(keys))  # Позиции по оси X
    file_size = round(os.path.getsize(path) / (1024*1024), 2)
    file_name = os.path.basename(path)
    # создание гистограммы
    fig, ax = plt.subplots(figsize=(16, 8))

    # Рисуем бары для первого словаря
    ax.barh([pos + width for pos in x], values1, width, label='йцукен', color='red')
    ax.barh([pos for pos in x], values2, width, label='diktor', color='blue')
    ax.barh([pos - width for pos in x], values3, width, label='zubachew', color='grey')
    for i in range(len(keys)):
        if values1[i] + values2[i] > 0:  # Избегаем деления на ноль
            diff1 = abs(values2[i] - values1[i]) / values1[i] * 100
            if values1[i] > values2[i]:
                xpos = values1[i]
            else:
                xpos = values2[i]
            ax.text(xpos + 0.1, i, f'{diff1:.1f}%', ha='center', va='center', color='black')

        if values2[i] + values3[i] > 0:  # Избегаем деления на ноль
            diff2 = abs(values3[i] - values2[i]) / values2[i] * 100
            if values2[i] > values3[i]:
                xpos = values2[i]
            else:
                xpos = values3[i]
            ax.text(xpos + 0.1, i - 0.4, f'{diff2:.1f}%', ha='center', va='center', color='black')
    ax.set_yticks(x)
    ax.set_yticklabels(keys)
    ax.set_ylabel('Пальцы')
    ax.set_xlabel('Количество нажатий')
    ax.set_title(f'{file_name}    {file_size:.2f} MB')
    ax.legend()

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.show()

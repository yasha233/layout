import matplotlib.pyplot as plt


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
    labels = list(data.keys())
    values = list(data.values())

    # создание гистограммы
    plt.bar(labels, values)

    plt.title(name)
    plt.xlabel('Пальцы')
    plt.ylabel('Количество нажатий')
    plt.show()

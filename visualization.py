import matplotlib.pyplot as plt


def draw_histogram(name, data):
        labels = list(data.keys())
        values = list(data.values())

        # создание гистограммы
        plt.bar(labels, values)

        plt.title(name)
        plt.xlabel('Пальцы')
        plt.ylabel('Количество нажатий')
        plt.show()


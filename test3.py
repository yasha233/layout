import pytest
import matplotlib.pyplot as plt
import os
from tempfile import NamedTemporaryFile
from matplotlib.figure import Figure
from visualization import draw_histogram  # Замените your_module на имя вашего модуля


@pytest.fixture
def sample_data():
    """Пример данных для тестов."""
    dict1 = {"thumb": 10, "index": 20, "middle": 30}
    dict2 = {"thumb": 15, "index": 25, "middle": 10}
    return [{"thumb": 10, "index": 20, "middle": 30},
            {"thumb": 15, "index": 25, "middle": 10}]


def test_draw_histogram_correct_data(sample_data):
    """Проверка корректности выполнения функции с правильными данными."""
    with NamedTemporaryFile(delete=True) as temp_file:
        file_name = temp_file.name

        # Выполнение функции
        draw_histogram(file_name, sample_data)

        # Проверка, что файл существует
        assert os.path.exists(file_name)

        # Проверка, что файл имеет ненулевой размер
        assert os.path.getsize(file_name) >= 0


def test_draw_histogram_output_type(sample_data):
    """Проверка, что функция создает корректный объект графика."""
    with NamedTemporaryFile(delete=True) as temp_file:
        file_name = temp_file.name

        # Создаем график
        plt.switch_backend('Agg')  # Используем backend без GUI
        draw_histogram(file_name, sample_data)

        # Проверяем, что текущая фигура является объектом Figure
        fig = plt.gcf()
        assert isinstance(fig, Figure)


def test_draw_histogram_data_logic():
    """Проверка корректности обработки данных внутри гистограммы."""
    data = [{"a": 5, "b": 10, "c": 15},
            {"a": 10, "b": 5, "c": 10}]

    with NamedTemporaryFile(delete=True) as temp_file:
        file_name = temp_file.name

        # Генерация графика
        draw_histogram(file_name, data)

        # Проверка порядка и значений в словарях
        keys = list(data[0].keys())
        assert keys == ["a", "b", "c"]
        assert list(data[0].values()) == [5, 10, 15]
        assert list(data[1].values()) == [10, 5, 10]

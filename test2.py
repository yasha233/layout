import tempfile
import os
import pytest
from text_analyzer import TextAnalyzer

@pytest.fixture
def setup_test_file():
    """Создаёт временный файл с тестовыми данными и возвращает путь к нему."""
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix='.txt') as temp_file:
        temp_file.write("Привет, мир!\n")
        temp_file.write("Test123.\n")
        temp_file.write("Тест с символами ABC.")
        temp_file_path = temp_file.name

    yield temp_file_path

    # Удаляем файл после завершения тестов
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
print(f"Создан файл: {setup_test_file}")
@pytest.fixture
def setup_symbols_and_shifts():
    """Возвращает тестовые символы и раскладки."""
    symbols = {
        "lfi": [["а", "б", "в", "г"], ["a", "b", "c"]],
        "rfi": [["д", "е", "ж", "з"], ["d", "e", "f"]],
    }
    shifts = [["1", "2", "3"], ["4", "5", "6"]]
    return symbols, shifts
def test_find_finger(setup_symbols_and_shifts):
    symbols, shifts = setup_symbols_and_shifts

    analyzer = TextAnalyzer(filename="dummy", symbols=symbols, shifts=shifts)

    assert analyzer.find_finger("а") == ["lfi", None]
    assert analyzer.find_finger("b") == [None, "lfi"]
    assert analyzer.find_finger("е") == ["rfi", None]
    assert analyzer.find_finger("f") == [None, "rfi"]
    assert analyzer.find_finger("x") == [None, None]


def test_count_symbols(setup_test_file, setup_symbols_and_shifts):
    symbols, shifts = setup_symbols_and_shifts
    analyzer = TextAnalyzer(filename=setup_test_file, symbols=symbols, shifts=shifts)

    print(f"Тестируем файл: {setup_test_file}")
    result = analyzer.count_symbols()

    assert result is not None, f"count_symbols() вернул None для файла {setup_test_file}"

    finger_load, finger_load2 = result

    # Проверка корректности подсчётов
    assert finger_load["lfi"] > 0, f"Символы для 'lfi' не подсчитаны: {finger_load}"
    assert finger_load["rfi"] > 0, f"Символы для 'rfi' не подсчитаны: {finger_load}"
    assert finger_load2["lfi"] > 0, f"Символы для 'lfi' (вторая раскладка) не подсчитаны: {finger_load2}"
    assert finger_load2["rfi"] > 0, f"Символы для 'rfi' (вторая раскладка) не подсчитаны: {finger_load2}"

def test_display_counts(setup_test_file, setup_symbols_and_shifts, capsys):
    symbols, shifts = setup_symbols_and_shifts
    analyzer = TextAnalyzer(filename=setup_test_file, symbols=symbols, shifts=shifts)
    analyzer.count_symbols()

    analyzer.display_counts()
    captured = capsys.readouterr()

    # Проверка вывода на экран
    assert "'lfi':" in captured.out
    assert "'rfi':" in captured.out
    assert "---------------------" in captured.out
def test_file_not_found_error():
    symbols = {"lfi": [["а"]], "rfi": [["д"]]}
    shifts = [["1"], ["2"]]
    analyzer = TextAnalyzer(filename="non_existent_file.txt", symbols=symbols, shifts=shifts)

    result = analyzer.count_symbols()
    assert result is None  # Ошибка обработана

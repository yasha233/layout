import string


class TextAnalyzer:
    def __init__(self, filename, symbols):
        self.filename = filename
        self.symbols = symbols
        self.symbol_counts = {symbol: 0 for symbol in symbols}

    def count_symbols(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Убираем пробелы по бокам
                for char in line:
                    if char in self.symbol_counts:
                        self.symbol_counts[char] += 1

    def display_counts(self):
        for symbol, count in self.symbol_counts.items():
            print(f"'{symbol}': {count}")

    def calculate_finger_load(self):
        total_load = 0
        for letter, count in self.letter_counts.items():
            total_load += self.finger_load.get(letter, 0) * count
        return total_load

    def display_results(self):
        print("Количество повторений каждой буквы:")
        for letter, count in sorted(self.letter_counts.items()):
            print(f"{letter}: {count}")
        print(f"\nОбщая нагрузка на пальцы: {self.calculate_finger_load()}")


def main():
    filename = 'C:/voina-i-mir.txt'  # Имя файла с текстом
    rows = (
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
        (16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27),
        (30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40),
        (42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53),
        (57,)
    )
    rows_symbols = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',  # Цифровой ряд
                    'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ',  # Верхний ряд
                    'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э',  # Средний ряд
                    'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.', ',',  # Нижний ряд
                    ' '  # Дополнительный
                    )
    symbol_counter = TextAnalyzer(filename, rows_symbols)
    symbol_counter.count_symbols()
    symbol_counter.display_counts()


if __name__ == "__main__":
    main()

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
    top_row = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13) # должно быть 5
    symbol_counter = TextAnalyzer(filename, top_row)
    symbol_counter.count_symbols()
    symbol_counter.display_counts()



if __name__ == "__main__":
    main()

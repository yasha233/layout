import string


class TextAnalyzer:
    def __init__(self, filename, symbols):
        self.filename = filename
        self.symbols = symbols
        self.finger_load = {finger: 0 for finger in symbols.keys()}

    def find_finger(self, char):
        for finger, layouts in self.symbols.items():
            for layout in layouts:
                if char in layout:
                    return finger
                    return None

    def count_symbols(self, char):
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                for char in line.strip().lower():
                    finger = self.find_finger(char)
                if finger:
                    self.finger_load[finger] += 1

    def display_counts(self):
        for symbol, count in self.finger_load.items():
            print(f"'{symbol}': {count}")


def main():
    filename = r'C:\Users\Daniil\PycharmProjects\layoutload\voina-i-mir.txt'  # Имя файла с текстом
    keylout_dd = {
        'rfi5': [('й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'),
                 ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')],
        'rfi4': [('ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'),
                 ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')],
        'rfi3': [('я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'), ('z', 'x', 'c', 'v', 'b', 'n', 'm')],
        'rfi2': [(' '), (' ')],
        'lfi5': [('ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-'),
                 ('`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-')],
        'lfi4': [('й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'),
                 ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')],
        'lfi3': [('ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'),
                 ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')],
        'lfi2': [('я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю'), ('z', 'x', 'c', 'v', 'b', 'n', 'm')]
    }
    symbol_counter = TextAnalyzer(filename, keylout_dd)
    symbol_counter.count_symbols(filename)
    symbol_counter.display_counts()


if __name__ == "__main__":
    main()

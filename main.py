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

    '''def count_symbols(self, char):
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Убираем пробелы по бокам
                for char in line:
                    if char in self.symbol_counts:
                        self.symbol_counts[char] += 1
                for char in line.strip().lower():
                    finger = self.find_finger(char)
                if finger:
                    self.finger_load[finger] += 1'''
    def count_symbols(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                i = -1
                for line in file:
                    i += 1
                    for char in line.strip():
                        finger = self.find_finger(char.lower())
                        if char.isupper():
                            exec(f'self.finger_load["lfi5м"] += 1')
                            #print(char, self.finger_load)
                        try:
                            exec(f'self.finger_load[finger] += 1')
                            #print(char, self.finger_load)
                        except KeyError:
                            pass
                if i > 0:
                    self.finger_load["rfi5м"] += i

        except FileNotFoundError:
            print("Файл не найден.")
        except IOError:
            print("Ошибка ввода-вывода при работе с файлом.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def display_counts(self):
        for symbol, count in self.finger_load.items():
            print(f"'{symbol}': {count}")


def main():
    filename = r'C:\voina-i-mir.txt'  # Имя файла с текстом
    keylout_dd = {
        'rfi5м': [('-', '_', '+', '=', 'з', 'х', 'ъ', '{', '}', '[', ']', 'ж', 'э'),
              ('p', ':', ';', '"', '?', '/')],
        'rfi4б': [(')', '0', 'щ', 'д', 'ю', '>', '.'),
              ('l', 'O')],
        'rfi3с': [('*', '8', '9', '(', 'ш', 'л', 'б', '<', ','), ('i', 'k')],
        'rfi2у': [('&', '7', '?', 'н', 'г', 'р', 'о', 'т', 'ь'), ('y', 'u', 'h', 'j', 'n', 'm')],
        'lfi5м': [('ё', '`', '~', 'й'), ('q', 'a')],
        'lfi4б': [('1', '!', '2', '@', '"', 'ц', 'ы', 'я'), ('w', 's', 'z')],
        'lfi3с': [('3', '#', '№', '4', ';', '$', 'у', 'в', 'ч'), ('e', 'd', 'x')],
        'lfi2у': [('5', '%', '6', '^', ':', 'к', 'е', 'а', 'п', 'с', 'м', 'и'), ('r', 't', 'f', 'g', 'c', 'v', 'b')]
    }

    symbol_counter = TextAnalyzer(filename, keylout_dd)
    symbol_counter.count_symbols()
    symbol_counter.display_counts()


if __name__ == "__main__":
    main()

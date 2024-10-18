import string
import matplotlib.pyplot as plt


class TextAnalyzer:
    def __init__(self, filename, symbols, shifts):
        self.filename = filename
        self.symbols = symbols
        self.shifts = shifts
        self.finger_load = {finger: 0 for finger in symbols.keys()}
        self.finger_load2 = {finger2: 0 for finger2 in symbols.keys()}

    def find_finger(self, char):
        i = [None, None]
        for finger, layouts in self.symbols.items():
            for layout in layouts:
                if char in layout:
                    if layouts.index(layout) == 1:
                        i[1] = finger
                    if layouts.index(layout) == 0:
                        i[0] = finger
        return i

    def count_symbols(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                i = -1
                for line in file:
                    i += 1
                    for char in line.strip():
                        t = self.find_finger(char.lower())
                        finger = t[0]
                        finger2 = t[1]
                        for sb in self.shifts[0]:
                            if char == sb:
                                exec(f'self.finger_load["lfi5м"] += 1')
                        for sb in self.shifts[1]:
                            if char == sb:
                                exec(f'self.finger_load2["lfi5м"] += 1')
                        if char.isupper():
                            exec(f'self.finger_load["lfi5м"] += 1')
                            exec(f'self.finger_load2["lfi5м"] += 1')
                            #print(char, self.finger_load)
                        try:
                            exec(f'self.finger_load[finger] += 1')
                            exec(f'self.finger_load2[finger2] += 1')
                            #print(char, self.finger_load)
                        except KeyError:
                            pass
                if i > 0:
                    self.finger_load["rfi5м"] += i
            return self.finger_load, self.finger_load2
        except FileNotFoundError:
            print("Файл не найден.")
        except IOError:
            print("Ошибка ввода-вывода при работе с файлом.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def display_counts(self):
        for symbol, count in self.finger_load.items():
            print(f"'{symbol}': {count}")
        print('---------------------')
        for symbol, count in self.finger_load2.items():
            print(f"'{symbol}': {count}")


def draw_histogram(name, data):
        # получаем всё из словаря data. первое - пальцы, второе - кол-во нажатий
        labels = list(data.keys())
        values = list(data.values())

        # создание гистограммы
        plt.bar(labels, values)

        plt.title(name)
        plt.xlabel('Пальцы')
        plt.ylabel('Количество нажатий')
        plt.show()


def main():
    filename = r'C:\1.txt'  # Имя файла с текстом
    symb = (('!', '"', '№', ';', '%', ':', '?', '*', '(', ')', '_', '+', '/', ','),
            ('№', '%', ':', ';', '-', '"', '(', ')', '+', 'ъ', '?', '!', '_'))

    keylout_dd = {'rfi5м': [('-', '=', 'з', 'х', 'ъ', 'ж', 'э'),
                            ('0', '*', '=', 'ч', 'ш', 'щ', 'р', 'й', 'ж')],
                  'rfi4б': [(')', '0', 'щ', 'д', 'ю', '.'),
                            ('9', 'д', 'с', 'г')],
                  'rfi3с': [('8', '9', 'ш', 'л', 'б'),
                            ('8', 'к', 'т', 'п')],
                  'rfi2у': [('7', 'н', 'г', 'р', 'о', 'т', 'ь'),
                            ('6', ',', '7', 'з', 'в', 'л', 'н', 'м', 'б')],
                  'lfi5м': [('ё', 'й'),
                            ('ё', '1', 'ц', 'у', 'ф')],
                  'lfi4б': [('1', '2', 'ц', 'ы', 'я'),
                            ('2', 'ь', 'и', 'э')],
                  'lfi3с': [('3', '4', 'у', 'в', 'ч'),
                            ('3', 'я', 'е', 'х')],
                  'lfi2у': [('5', '6', 'к', 'е', 'а', 'п', 'с', 'м', 'и'),
                            ('4', '5', '.', 'а', 'ы', 'ю', 'о')]}

    symbol_counter = TextAnalyzer(filename, keylout_dd, symb)
    symbol_counter.count_symbols()
    symbol_counter.display_counts()
    draw_histogram('йцукен', symbol_counter.count_symbols()[0])
    draw_histogram('diktor', symbol_counter.count_symbols()[1])


if __name__ == "__main__":
    main()
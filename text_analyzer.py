class TextAnalyzer:
    def __init__(self, filename, symbols, shifts):
        """
        Инициализация класса TextAnalyzer.

        :param filename: Путь к файлу, который будет анализироваться.
        :param symbols: Словарь, содержащий символы и соответствующие им раскладки.
        :param shifts: Список сдвигов для анализа символов.
        """
        self.filename = filename
        self.symbols = symbols
        self.shifts = shifts
        self.finger_load = {finger: 0 for finger in symbols.keys()}
        self.finger_load2 = {finger2: 0 for finger2 in symbols.keys()}

    def find_finger(self, char):
        """
        Находит, каким пальцем следует печатать данный символ.

        :param char: Символ, для которого нужно определить палец.
        :return: Список, содержащий два элемента: палец для нижнего и верхнего регистра.
        """
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
        """
        Подсчитывает количество символов, напечатанных каждым пальцем.

        :return: Кортеж с двумя словарями, содержащими количество символов для каждого пальца.
        """
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
                        try:
                            exec(f'self.finger_load[finger] += 1')
                            exec(f'self.finger_load2[finger2] += 1')
                        except KeyError:
                            pass
                if i > 0:
                    self.finger_load["rfi5м"] += i
                    self.finger_load2["rfi5м"] += i
            return self.finger_load, self.finger_load2

        except FileNotFoundError:
            print("Файл не найден.")
        except IOError:
            print("Ошибка ввода-вывода при работе с файлом.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def display_counts(self):
        """
        Выводит на экран количество символов, напечатанных каждым пальцем.

        :return: None
        """
        for symbol, count in self.finger_load.items():
            print(f"'{symbol}': {count}")
        print('---------------------')
        for symbol, count in self.finger_load2.items():
            print(f"'{symbol}': {count}")
class TextAnalyzer:
    def __init__(self, filename, symbols, shifts, homekeys):
        self.distant_symbols = {symbol for group in [('х', 'ъ', 'ё'), ('ш', 'щ', 'ё'), ('ц', 'щ', 'ё'), ('ш', 'щ', '')] for symbol in group}
        self.digits = {str(i) for i in range(10)}
        self.filename = filename
        self.symbols = symbols
        self.shifts = shifts
        self.homekeys = homekeys
        self.finger_loads = {i: {finger: 0 for finger in symbols.keys()} for i in range(4)}

    def find_finger(self, char):
        for finger, layouts in self.symbols.items():
            for index, layout in enumerate(layouts):
                if char in layout:
                    return [finger if i == index else None for i in range(4)]
        return [None] * 4

    def update_finger_load(self, finger_load, finger, char, fine, finger_index):
        if finger in finger_load:
            finger_load[finger] += 1
            # Используем finger_index для доступа к homekeys
            if char not in self.homekeys[finger_index] or char in self.digits or char in self.distant_symbols:
                fine += 1
        return fine

    def count_symbols(self):
        fines = [0] * 4
        for filepath in self.filename:
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    for line in file:
                        for char in line.strip():
                            t = self.find_finger(char.lower())
                            for i, finger in enumerate(t):
                                if finger:
                                    fines[i] = self.update_finger_load(self.finger_loads[i], finger, char, fines[i], i)
                            if char.isupper():
                                for i in range(4):
                                    if t[i] == "lfi5м":
                                        self.finger_loads[i]["rfi5м"] += 1
                                    else:
                                        self.finger_loads[i]["lfi5м"] += 1

                    print(f'Штрафы: {fines}')

                    # Формируем результат как список словарей
                    result = []
                    for i in range(4):
                        result.append(self.finger_loads[i])  # Добавляем словарь для каждого пальца

                    return result, fines  # Возвращаем список словарей и штрафы

            except FileNotFoundError:
                print("Файл не найден.")
            except IOError:
                print("Ошибка ввода-вывода при работе с файлом.")

    def display_counts(self):
        for i in range(4):
            for symbol, count in self.finger_loads[i].items():
                print(f"'{symbol}': {count}")
            print('---------------------')

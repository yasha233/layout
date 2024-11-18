from text_analyzer import TextAnalyzer
from visualization import draw_histogram


def main():
    filename = (r'F:\1.txt', )  # Имя файла с текстом
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
    for filename_i in filename:
        symbol_counter = TextAnalyzer(filename_i, keylout_dd, symb)
        final_loads = symbol_counter.count_symbols()
        # symbol_counter.display_counts()
        draw_histogram(filename_i, final_loads)
        print(final_loads)


if __name__ == "__main__":
    main()

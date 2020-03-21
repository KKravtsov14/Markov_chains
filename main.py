# Text generator for English
# Developers: Kravtsov - 80%
#             Mikhailov - 20%

import random as r


def reader(file):
    slovar = {}
    all_words = []
    blank_character = ''
    punctuation = ['.', ',', '!', '?', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    with open(file, 'r') as text:
        for i in text:
            working_line = i
            working_line += ' '

            for j in range(len(working_line )):
                if working_line [j].isalpha() or working_line [j] in punctuation:
                    blank_character += working_line [j]

                elif blank_character != '' and slovar.get(blank_character, 0) == 0:
                    slovar[blank_character] = list([])
                    all_words.append(blank_character)
                    blank_character = ''

                elif slovar.get(blank_character, 0) != 0:
                    all_words.append(blank_character)
                    blank_character = ''

    for j in range(len(all_words) - 1):
        key_generator = slovar[all_words[j]]
        key_generator = key_generator.append(all_words[j + 1])
    return slovar


def generator(slovar, n):
    slovar_1 = {}
    k = 0

    for i in slovar:
        slovar_1[k] = i
        k += 1

    for i in range(n):

        number = r.randint(0, len(slovar_1) - 1)
        sentens = slovar_1[number]
        a = slovar[slovar_1[number]]
        for j in range(2):
            number = r.randint(0, len(a) - 1)
            if '.' not in a[number] and '!' not in a[number] and '?' not in a[number]:
                sentens += ' '
                sentens += a[number]
                a = slovar[a[number]]

        for j in range(r.randint(1, 16)):
            number = r.randint(0, len(a) - 1)
            if '.' in a[number] or '!' in a[number] or '?' in a[number]:
                sentens += ' '
                sentens += a[number]
                break

            else:
                sentens += ' '
                sentens += a[number]
                a = slovar[a[number]]

        if sentens.count('.') == 0 or sentens.count('!') == 0 or sentens.count('?') == 0:
            sentens += '.'

        print(sentens)

def main():
    print('Программа генерирует предложения английского языка')
    print('Введите название файла(полное, если он хранится в другой папке)')
    generator(reader(str(input())), int(input('Введите количество предложений, которое нужно сгенерировать')))

main()
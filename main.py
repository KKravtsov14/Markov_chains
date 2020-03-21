import random as r


def reader():
    slovar = {}
    all_words = []
    s_cr = ''
    punctuation = ['.', ',', '!', '?', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    with open('text.txt', 'r') as t:
        for i in t:
            s = i
            s += ' '

            for j in range(len(s)):
                if s[j].isalpha() or s[j] in punctuation:
                    s_cr += s[j]

                elif s_cr != '' and slovar.get(s_cr, 0) == 0:
                    slovar[s_cr] = list([])
                    all_words.append(s_cr)
                    s_cr = ''

                elif slovar.get(s_cr, 0) != 0:
                    all_words.append(s_cr)
                    s_cr = ''

    for j in range(len(all_words) - 1):
        otv = slovar[all_words[j]]
        otv = otv.append(all_words[j + 1])
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
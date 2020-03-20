def reader():
    slovar = {}
    all_words = []
    s_cr = ''
    punctuation = ['.', ',', '!', '?', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    with open('text.txt', 'r') as t:
        for i in t:
            s = i
            s = s.replace('\n', '')
            s = s.replace('.', ' . ')
            s = s.replace('!', ' ! ')
            s = s.replace('?', ' ? ')
            s = s.replace(',', ' , ')
            for j in range(len(s)):
                if s[j].isalpha() or s[j] in punctuation:
                    s_cr += s[j].lower()

                elif s_cr != '' and slovar.get(s_cr, 0) == 0:
                    slovar[s_cr] = list([])
                    all_words.append(s_cr)
                    s_cr = ''


                elif slovar.get(s_cr, 0) != 0:
                    all_words.append(s_cr)
                    s_cr = ''

        print(slovar, all_words)

    for j in range(len(all_words) - 1):
        otv = slovar[all_words[j]]
        otv = otv.append(all_words[j + 1])
        slovar[j] = otv

    print(slovar)

reader()

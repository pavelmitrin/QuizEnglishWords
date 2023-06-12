import random

path = "words.txt"
enWords = []
ruWords = []



def add_empty():
    for i in range(1):
        print("")

try:
    with open(path, 'r', encoding='utf-8') as words:
        for line in words:
            symbols = line.split(' - ')
            symbols[1] = symbols[1].replace('\n', '').replace('\r', '')

            enWords.append(symbols[0])
            ruWords.append(symbols[1])

        itter = True

        while itter:
            word = random.randrange(len(enWords))
            print("Выберите правильный вариант ответа")
            print("Перевод слова", enWords[word], "это ...")

            possibleAnswer = random.randrange(4)

            answers = []
            answers.append(ruWords[word])
            # print(ruWords[word])
            for i in range(3):
                answers.append(ruWords[random.randrange(len(ruWords))])
            answers = set(answers)
            answers = list(answers)

            if len(answers) < 4:
                for i in range(len(answers), 5):
                    answers.append(ruWords[random.randrange(len(ruWords))])

            print("1 -", answers[0], "2 -", answers[1], "3 -", answers[2], "4 -", answers[3])

            answer = input('Введите номер варианта или stop для окончания викторины: ')
            try:
                answer = int(answer) -1

                if answers[answer] == ruWords[word]:
                    print("Ответ верный")
                    add_empty()
                else:
                    print("Ответ неверный")
                    add_empty()
            except ValueError:
                if answer.lower() == ("stop" or "стоп"):
                    itter = False
                    add_empty()
                    print("Цикл завершён")
                else:
                    print("Вы ввели непонятное значение, попробуйте ещё раз")
                    add_empty()



except FileNotFoundError:
    print("Данного файла не существует")
except TypeError:
    print("Неверный тип")
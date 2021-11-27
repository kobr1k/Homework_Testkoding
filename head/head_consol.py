import random
bufer_size = 1024 * 1024 * 8

with open("C:/python/Git/Homework_Testkoding/head/word.txt",
 "r" , buffering = 2 , encoding="utf-8"  )as file :
    words = file.readlines(bufer_size)
while True:
    i = random.randrange(0 , len(words))
    word = words[i].strip()

    n = len(word)
    for letter_of_word in word :
        print("-" , end = "")
    print()
    guess = set()
    count_looz = 6
    while True :
        letter = input("введите букву  ")
        guess.add(letter.lower())
        overlap = 0 #совпадения букв
        number_unclown_letter = 0
        for letter_of_word in word :
            if letter_of_word in guess :
                print(letter_of_word, end = "")
            else :
                print("-", end="")
                number_unclown_letter += 1
        print()
        if word.find(letter) == -1:
            count_looz -= 1
        if count_looz == 0:
            print("вы проиграли")
            break
        else :
            print(count_looz,"оставшихся ошибок  ")
        if number_unclown_letter == 0 :
            print("вы выиграли ")
            break
    letter = input("нажмите 0 чтобы выйти или нажмите 1 чтобы сыграть ещё раз  ")
    if letter != "1":
        break
    









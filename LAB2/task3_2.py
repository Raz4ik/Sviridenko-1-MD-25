word = ""
while word != "stop":
    bool = 0
    word = input("Введите слово чтобы проверить на редкость: ")
    for a in word:
        if a == "ф":
            bool = 1
            break

    if bool == 1:
        print("Ого! Это слово редкое")
    else:
        print("Эх, это не очень редкое слово")
    print("Хотите закончить введите stop")

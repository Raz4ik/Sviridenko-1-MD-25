word = input("Введите слово чтобы проверить на редкость: ")
bool = 0

for a in word:
    if a == "ф":
        bool = 1
        break

if bool == 1:
    print("Ого! Это слово редкое")
else:
    print("Эх, это не очень редкое слово")
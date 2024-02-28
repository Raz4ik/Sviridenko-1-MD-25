place = int(input("Введите место: "))

print(place)

if place > 54 or place <= 0:
    print("Такого нет места")
else:
    if place <= 36:
        if place % 2 == 0:
            print("Ваше место верхнее в купэ")
        else:
            print("Ваше место нижнее в купэ")
    else:
        if place % 2 == 0:
            print("Ваше место верхнее боковое")
        else:
            print("Ваше место нижнее в боковое")

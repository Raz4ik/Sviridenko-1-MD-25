import random
bool = 0
while bool != 3:
    x = random.randint(1,9)
    y = random.randint(1,9)
    print(x," + ",y," = ", end= " ")
    ans = int(input())
    if ans != x + y:
        bool += 1
        print("Ответ неверный")
    else:
        print("Правильно")
print("Увы! Вы проиграли")
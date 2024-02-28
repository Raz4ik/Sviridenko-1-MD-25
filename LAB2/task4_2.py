import random
bool = 0
c = 0
while bool != 3:
    x = random.randint(-9,9)
    y = random.randint(-9,9)
    print(x," + ",y," = ", end= " ")
    ans = int(input())
    if ans != x + y:
        bool += 1
        print("Ответ неверный")
    else:
        c += 1
        print("Правильно")
print("Увы! Вы проиграли кол-во правильных ответов = ",c)

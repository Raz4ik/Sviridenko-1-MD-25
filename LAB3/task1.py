def task1():
    print("task1")
    numbers = ['1','5','3','8','20']
    var = input("Введите число:")
    if var in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
def task2():
    print("task2")
    numbers = ['1', '5', '3', '8', '20', '1']
    for a in numbers:
        if numbers.count(a) > 1:
            print(a, " ")
def task3():
    print("task3")
    week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    user = int(input("Сколько выходных на неделе вы хотите:"))
    weekend = week[7 - user:8]
    work = week[0:7 - user]
    print("Ваши выходные дни:", weekend)
    print("Ваши рабочие дни:", work)
def task4():
    import random
    def sport_add(grup):
        add = []
        for i in range(0, 5):
            a = int(random.uniform(0, 9))
            add.append(grup[a])
        return add

    print("task4")
    group25_1 = ["Серега", "Валера", "Алена", "Соня", "Ксюша", "Юра", "Женя", "Даня", "Саша", "Коля"]
    group20_1 = ["Матвей", "Никита", "Катя", "Женя", "Марк", "Ваня", "Света", "Марина", "Антон", "Стас"]
    group1 = []
    group2 = []
    sport_team = ()
    group1 = sport_add(["Серега", "Валера", "Алена", "Соня", "Ксюша", "Юра", "Женя", "Даня", "Саша", "Коля"])
    group2 = sport_add(["Матвей", "Никита", "Катя", "Женя", "Марк", "Ваня", "Света", "Марина", "Антон", "Стас"])
    group = group1 + group2
    sport_team = tuple(group)
    print("25 Группа:", group25_1)
    print("20 Группа:", group20_1)
    print("Спортивная команда:", sport_team, " длина:", len(sport_team))
    sport_team = sorted(sport_team)
    print("Отсортированная спортивная команда:", sport_team)
    count = 0
    for a in sport_team:
        if a == "Женя":
            count += 1
    if count >= 1:
        print("Женя встречается ", count, " раз")
    else:
        print("Женя не встречается в спортивной команде")

task1()
task2()
task3()
task4()
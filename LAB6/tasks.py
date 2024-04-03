def task1():
    print("TASK1")
    d = {
        'Анкара': 'Турция',
        'Россия': 'Москва',
        'Амман' : 'Иордания',
        'Амстердам' : 'Нидерланды',
        'Андорра-ла-Велья' : 'Андорра'
    }
    print(d)
    inp = input("Введите страну: ")
    print("Столица ", inp, " - ",d[inp])
    d2 = dict(sorted(d.items()))
    print(d2)
def task2():
    print("TASK2")
    sim = {"АВЕИНОРСТ" : 1, "ДКЛМПУ" : 2, "БГЁЬЯ" : 3, "ЙЫ" : 4, "ЖЗХЦЧ" : 5, "ШЭЮ" : 8, "ФЩЪ" : 10}
    word = input("Введите ваше слово: ")
    res = 0
    for i in word:
        for name,value in sim.items():
            if name.count(i) > 0:
                res += value
    print("Ваше слово : ",word ,"Имеет сумму = ",res)
task1()
task2()
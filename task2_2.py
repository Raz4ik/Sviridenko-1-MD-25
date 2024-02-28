a = ""
word = ""


while word != "stop":
    a += str(word + " ")
    word = input("Введите слово: ")

print(a)
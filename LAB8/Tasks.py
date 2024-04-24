from PIL import Image, ImageDraw, ImageFont
def task1():
    img = Image.open('card.JPG')
    img = img.crop((360, 10, 750, 350))
    img.save('new_card.jpg')

def task2():
    cards = {
        'День рождения': 'card.JPG',
        'Свадьба': 'card_wedding.jpg',
        '23 февраля': 'card_army.jpg',
        '8 марта': 'card_womenday.jpg'
    }
    print(cards.keys())
    user = input("На какой праздник вам необходима открытка?\nВыберите из списка: ")
    try:
        card_day = cards[user]
    except LookupError :
        print("На данный праздник у нас пока нет открыток(")
    else:
        img = Image.open(card_day)
        img.show()

def task3():
    import sys
    usertext = input("Кому вы хотите подарить открытку?\nВведите имя: ")
    img = Image.open('card.JPG')
    img = img.crop((360, 10, 750, 350))
    text_draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=20)
    print(usertext)
    text_draw.text(
        (185, 170),
        f'{usertext}, поздравляю!)',
        anchor="ms",
        fill="#ff0000",
        font=font
        )
    img.show()
    img.save('new_user_card.jpg')

task3()
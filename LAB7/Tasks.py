import io

from PIL import Image, ImageDraw, ImageFont
def task1():
    img = Image.open(r'D:\Sviridenko-1-MD-25_1\12.jpg')
    img.show()
    print(img.format)
    print(img.size)
    print(img.mode)

def task2():
    img = Image.open(r'D:\Sviridenko-1-MD-25_1\LAB7\12.jpg')
    resize_img = img.resize(
        (img.width // 3, img.height // 3)
    )
    converted_vertical_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_horizontal_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    resize_img.save("resize12.jpg")
    converted_vertical_img.save("converted_vertical_12.jpg")
    converted_horizontal_img.save("converted_horizontal_12.jpg")

def task3_1(img,k):
    from PIL import ImageFilter
    names = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
    img_gray_smooth = img.filter(ImageFilter.SMOOTH)
    edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
    edges_smooth.save(names[k])
def task3():
    img = Image.open(r'D:\Sviridenko-1-MD-25_2\LAB7\3_1.jpg')
    task3_1(img,0)
    img = Image.open(r'D:\Sviridenko-1-MD-25_2\LAB7\3_2.jpg')
    task3_1(img,1)
    img = Image.open(r'D:\Sviridenko-1-MD-25_2\LAB7\3_3.jpg')
    task3_1(img,2)
    img = Image.open(r'D:\Sviridenko-1-MD-25_2\LAB7\3_4.jpg')
    task3_1(img,3)
    img = Image.open(r'D:\Sviridenko-1-MD-25_2\LAB7\3_5.jpg')
    task3_1(img,4)

def task4():
    img = Image.open(r'D:\Sviridenko-1-MD-25_2\LAB7\12.jpg')
    the_string = "Это водяной знак!)"
    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(img)
    drawer.text((100, 20), the_string, font=font, fill='black')

    img.save('new_img.jpg')

task4()
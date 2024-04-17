from PIL import Image
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
    names = ['1.jpg','2.jpg','3.png','4.jpg','5.png']
    img_gray_smooth = img.filter(ImageFilter.SMOOTH)
    edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
    edges_smooth.save(names[k])
def task3():
    img = Image.open(r'D:\Sviridenko-1-MD-25_1\LAB7\3_1.jpg')
    task3_1(img,0)
    img = Image.open(r'D:\Sviridenko-1-MD-25_1\LAB7\3_2.jpg')
    task3_1(img,1)
    img = Image.open(r'D:\Sviridenko-1-MD-25_1\LAB7\3_3.png')
    img = Image.open(r'D:\Sviridenko-1-MD-25_1\LAB7\3_4.jpg')
    task3_1(img,3)
    img = Image.open(r'D:\Sviridenko-1-MD-25_1\LAB7\3_5.png')

task3()
from PIL import Image, ImageFilter
import os
import csv

def task_1():
    exp = "export"
    imp = "import_1"
    if not os.path.exists(imp):
        os.makedirs(imp)
    def convert_to_grayscale(img):
        return img.convert("L")
    for filename in os.listdir(exp):
        input_path = os.path.join(exp, filename)
        output_path = os.path.join(imp, filename)
        img = Image.open(input_path)
        processed_image = convert_to_grayscale(img)
        processed_image.save(output_path)

def task_2():
    exp = "export"
    imp = "import_2"
    if not os.path.exists(imp):
        os.makedirs(imp)
    def convert_to_grayscale(img):
        return img.convert("L")
    for filename in os.listdir(exp):
        if filename.lower().endswith((".png", ".jpg")):
            input_path = os.path.join(exp, filename)
        output_path = os.path.join(imp, filename)
        img = Image.open(input_path)
        processed_image = convert_to_grayscale(img)
        processed_image = processed_image.filter(ImageFilter.FIND_EDGES)
        processed_image = processed_image.filter(ImageFilter.EDGE_ENHANCE)
        processed_image.save(output_path)

def task_3():
    products = []
    with open("product.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            if row["Продукт"]:
                products.append(row)

    total_sum = 0
    print("Нужно купить:")
    for product in products:
        name = product["Продукт"]
        quantity = int(product["Количество"]) if product["Количество"] else 0
        price = int(product["Цена"]) if product["Цена"] else 0
        product_sum = quantity * price
        total_sum += product_sum
        print(f"{name} - {quantity} шт. за {price} руб.")

    print(f"Итоговая сумма: {total_sum} руб.")

task_3()
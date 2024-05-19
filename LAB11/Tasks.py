def task_1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
        def open_restaurant(self):
            print("Ресторан открыт!")

    newRestaurant = Restaurant("Filling", "Russian")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def task_2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"\nНазвание ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
    restaurant1 = Restaurant("Вкусно и Точка", "Фастфуд")
    restaurant2 = Restaurant("Москва", "Европейская")
    restaurant3 = Restaurant("Charlie", "Русская")
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def task_3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"\nНазвание ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")
        def update_rating(self, new_rating):
                self.rating = new_rating
    restaurant1 = Restaurant("McDonald's", "фастфуд",3)
    restaurant2 = Restaurant("Москва", "Европейская",4)
    restaurant3 = Restaurant("Charlie", "Русская", 3)
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
    restaurant1.update_rating(5)
    restaurant2.update_rating(5)
    restaurant3.update_rating(2)
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

task_3()
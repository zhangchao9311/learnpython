class Restaurant:
    """一次餐馆的尝试"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐馆名称和餐馆风味"""
        print(f"The {self.restaurant_name} is {self.cuisine_type}.")

    def open_restaurant(self):
        """打印这家店是开张的"""
        print(f"The {self.restaurant_name} is openning!")

restaurant = Restaurant('Hao Liyou', 'Chinese')
restaurant.describe_restaurant()

restaurant_1 = Restaurant('Tong Fu', 'Xiangcai')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('A Qiang', 'Yuecai')
restaurant_2.describe_restaurant()
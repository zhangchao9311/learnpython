class Restaurant:
    """一次餐馆的尝试"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆名称和餐馆风味"""
        print(f"The {self.restaurant_name} is {self.cuisine_type}.")

    def open_restaurant(self):
        """打印这家店是开张的"""
        print(f"The {self.restaurant_name} is openning!")

    def served_number(self):
        """打印餐馆就餐的人数"""
        print(f"This restaurant has been served {self.number_served} people.")

    def set_number_served(self, numbers):
        """设置就餐人数"""
        self.number_served = numbers


restaurant = Restaurant('Hao Liyou', 'Chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(210)
restaurant.served_number()
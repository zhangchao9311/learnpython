class User:
    """创建用户属性"""

    def __init__(self, first_name, last_name):
        """用户姓名信息"""
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        """打印用户信息摘要"""
        print(f"The user's first name is {self.first_name.title()}, and last name is {self.last_name.title()}.")

    def greet_user(self):
        """向用户打招呼"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

user_1 = User('zhang', 'san')
user_1.describe_user()
user_1.greet_user()

user_2 = User('li', 'si')
user_2.describe_user()
user_2.greet_user()
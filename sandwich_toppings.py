def sandwich(*toppings):
    """打印三明治的食材"""
    print("\nYou have ordered the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

sandwich('banana')
sandwich('orange', 'banana')
sandwich('apple', 'grape', 'melon')
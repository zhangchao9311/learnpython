def make_car(maker, model, **car_info):
    """保存一辆汽车的信息"""
    car_info['make_name'] = maker
    car_info['model_name'] = model
    return car_info

car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)
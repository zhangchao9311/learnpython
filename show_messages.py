def show_messages(messages):
    """打印列表中的每条文本信息"""
    for message in messages:
        msg = f"{message.title()}!"
        print(msg)

txts = ['hello', 'good morning','good afternoon']
show_messages(txts)
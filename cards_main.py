"""__author__ = strickland"""

import cards_tools


while True:
    # 显示操作说明
    cards_tools.print_title()

    # 用户输入操作指令
    order = input('please put the mark：')
    # 对代号做判断
    if order == '1':
        # 增加信息操作
        cards_tools.add_card()
    elif order == '2':
        # 显示所有的名片信息
        cards_tools.show_all()
    elif order == '3':
        # 搜索名片信息
        cards_tools.search_card()
    elif order == '0':
        break
    else:
        print('you put the wrong mark,please put it again')

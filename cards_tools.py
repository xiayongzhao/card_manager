"""author:Strickland"""

cards_list = []


def print_title():

    print('welcome to the card manage system')
    print('*' * 50)
    print('''
    1.add a new card
    2.show the all
    3.search a card

    0.quit
    ''')
    print('*' * 50)


def add_card():

    name = input('please put the name:')
    gender = input('please put the gender:')
    phone = input('please put the phone number:')
    email = input('please put the email:')
    card_dic = {'name': name, 'gender': gender, 'phone': phone, 'email': email}
    cards_list .append(card_dic)
    print(cards_list)
    return cards_list


def show_all():

    print('*'*50)
    print('name\t\tgender\t\tphone\t\temail')
    print('='*50)
    for card_dic in cards_list:
        print('%s\t\t%s\t\t%s\t\t%s' % (card_dic['name'],
                                        card_dic['gender'],
                                        card_dic['phone'],
                                        card_dic['email']))
    print('='*50)


def search_card():
    search_name = input('please put the name you want to search:')
    for card_dic in cards_list:
        if search_name == card_dic['name']:
            print('name\t\tgender\t\tphone\t\temail')
            print('=' * 50)
            print('%s\t\t%s\t\t%s\t\t%s' % (card_dic['name'],
                                            card_dic['gender'],
                                            card_dic['phone'],
                                            card_dic['email']))
            # 对检索到的信息做修改
            revise_card(card_dic)
        else:
            print('the person you find is not exist')


def revise_card(card_dic):
    revise_key = input('please put the program you want to revise:')
    new_value = input('please put the new value:')
    card_dic[revise_key] = new_value
    print('%s\t\t%s\t\t%s\t\t%s' % (card_dic['name'],
                                    card_dic['gender'],
                                    card_dic['phone'],
                                    card_dic['email']))
    return card_dic

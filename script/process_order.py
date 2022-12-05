import pandas as pd
import re
def load_xlsx(file_name = 'menu.xlsx'):
    xls = pd.ExcelFile(file_name)
    df = xls.parse(xls.sheet_names[0])
    df = df.T
    # print(df)
    # print(df.to_dict())
    return df.to_dict()

def write_xlsx(file_name = 'menu.xlsx'):
    menu = {
        "item":["滷肉飯","豆花", "燒肉", "雞腿"],
        "price":[1, 2, 3, 4],
        }
    df = pd.DataFrame(data=menu)
    # df = (df.T)
    # print (df)
    df.to_excel(file_name)

def process_data_to_menu(data_dict:dict):
    menu_dict = dict()
    for key in data_dict:
        menu_dict[data_dict[key]['item']]=data_dict[key]['price']
    # print(menu_dict)
    return menu_dict

def process_price_with_order(menu_dict, order):
    # format is 多少個什麼和多少個什麼
    order = re.split('和|個', order)

    # using stack to process item and amount
    price_dict = dict()
    top = None
    for item in order:
        if item.isdigit():
            if top == None:
                top = item
            else:
                price_dict[top] = {'amount':item, 'price':None}
                top = None
        else:
            if top == None:
                top = item
            else:
                price_dict[item] = {'amount':int(top), 'price':None}
                top = None

    total = 0
    for item in price_dict:
        if item in menu_dict:
            price_dict[item]['price'] = price_dict[item]['amount'] * menu_dict[item]
            total += price_dict[item]['price']

    print(menu_dict)
    print(price_dict)

# write_xlsx()
data_dict = load_xlsx()
menu_dict = process_data_to_menu(data_dict)
process_price_with_order(menu_dict, '100個火腿和7000個蛋糕')
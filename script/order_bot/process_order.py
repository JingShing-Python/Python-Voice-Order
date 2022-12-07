import pandas as pd
import re
from chinese_num_transform import chinese_to_arabic
chinese_char_dict = {
    '〇' : 0, '一' : 1, '二' : 2, '三' : 3, '四' : 4, '五' : 5, '六' : 6, '七' : 7, '八' : 8, '九' : 9, '零' : 0,
    '壹' : 1, '贰' : 2, '叁' : 3, '肆' : 4, '伍' : 5, '陆' : 6, '柒' : 7, '捌' : 8, '玖' : 9, '貮' : 2, '兩' : 2,
}
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
                if item in chinese_char_dict:
                    item = chinese_to_arabic(item)
                price_dict[top] = {'amount':item, 'price':None}
                top = None
        else:
            if top == None:
                top = item
            else:
                if top.isnumeric():
                    top = chinese_to_arabic(top)
                top = int(top)
                price_dict[item] = {'amount':top, 'price':None}
                top = None

    total = 0
    for item in price_dict:
        if item in menu_dict:
            price_dict[item]['price'] = price_dict[item]['amount'] * menu_dict[item]
            total += price_dict[item]['price']
    none_list = []
    for item in price_dict:
        if price_dict[item]['price']==None:
            none_list.append(item)

    print(menu_dict)
    print(price_dict)
    # return total, none_list
    return sum_up_total_line(total, none_list)

def sum_up_total_line(total, none_list):
    total = format(total, ",")
    line = '總共是' + str(total) + '元。'
    if len(none_list)>0:
        line+='不過，我們沒有：'
        for item in none_list:
            line+=item + ', '
    return line

# write_xlsx()
# data_dict = load_xlsx('script/menu.xlsx')
# menu_dict = process_data_to_menu(data_dict)
# print(process_price_with_order(menu_dict, '100個火腿和7000個蛋糕'))
# print(process_price_with_order(menu_dict, '兩千萬個雞腿和兩個蛋糕'))
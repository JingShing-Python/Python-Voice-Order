from chinese_num_transform import chinese_in_string_transform
def print_single_law(idx, data):
    if "刪除" in data[idx][2]:
        print("本法條已被刪除")
        exit()
    if "告訴乃論" in data[idx][2]:
        print("本法條為刑法第"+data[idx][0]+"條，法條內容為"+data[idx][5])
        exit()
    law_item = data[idx][2] + "為刑法第" + data[idx][0] + "條"
    if data[idx][1] != '0':
        law_item += "之" + data[idx][1]
    law_item += '，'
    if data[idx][3] == '1':
        law_item += "為告訴乃論之罪，"
    law_item += "法條內容為"
    law_item += data[idx][5]
    print(law_item)

def input_by_number(self):
    number_of = self.listener()
    number_of = chinese_in_string_transform(number_of)
    search_parameter = []
    # number_of = number_of.replace('第', '')
    # number_of = number_of.replace('條', '')
    if '之' in number_of:
        number_of = number_of.split('之')
        number_of[0] = "".join(filter(str.isdigit, number_of[0]))
        number_of[1] = "".join(filter(str.isdigit, number_of[1]))
        '''
        while number_of[0].isnumeric() == False or number_of[1].isnumeric() == False:
            print("請再說一次")
            return input_by_number()
        '''
        search_parameter.append(number_of[0])
        search_parameter.append(number_of[1])
    else:
        number_of = "".join(filter(str.isdigit, number_of))
        '''
        while number_of.isnumeric() == False:
            print("請再說一次")
            return input_by_number()
        '''
        search_parameter.append(number_of)
        search_parameter.append('0')
    return search_parameter


def input_by_str(self):
    name = ''
    search_parameter = []
    name += '%'
    name_of = self.listener()
    name_of = name_of.replace('罪', '')
    name += name_of
    name += '%'
    search_parameter.append(name)
    return search_parameter


def input_all_info(self):
    print('條號:')
    number = self.listener()
    number = chinese_in_string_transform(number)
    number = "".join(filter(str.isdigit, number))
    '''
    while number.isnumeric() == False:
        print("請再說一次")
        number = self.listener()
    '''
    print('之幾:')
    of = self.listener()
    of = chinese_in_string_transform(of)
    of = "".join(filter(str.isdigit, of))
    '''
    while of.isnumeric() == False:
        print("請再說一次")
        of = self.listener()
    '''
    print('法條名:')
    name = self.listener()
    print('選擇確認或取消告訴乃論?')
    isNTWC = self.listener()
    while isNTWC != '確認' and isNTWC != '取消':
        print("請再說一次")
        isNTWC = self.listener()
    if isNTWC == '確認':
        isNTWC = '1'
    else:
        isNTWC ='0'
    issin = '0'
    print('法條內容:')
    content = self.listener()
    search_parameter = []
    search_parameter.append(number)
    search_parameter.append(of)
    modify_parameter = []
    modify_parameter.append(number)
    modify_parameter.append(of)
    modify_parameter.append(name)
    modify_parameter.append(isNTWC)
    modify_parameter.append(issin)
    modify_parameter.append(content)
    return search_parameter, modify_parameter

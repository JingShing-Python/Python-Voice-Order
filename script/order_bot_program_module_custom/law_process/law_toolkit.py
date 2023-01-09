from chinese_num_transform import chinese_in_string_transform


def print_single_law(idx, data, self):
    law_item = data[idx][2] + "為刑法第" + data[idx][0] + "條"
    if data[idx][1] != '0':
        law_item += "之" + data[idx][1]
    law_item += '，'
    if data[idx][3] == '1':
        law_item += "為告訴乃論之罪，"
    law_item += "法條內容為"
    law_item += data[idx][5]
    if "刪除" in data[idx][2]:
        law_item = "本法條已被刪除"
    if "告訴乃論" in data[idx][2]:
        law_item = "本法條為刑法第"+data[idx][0]+"條，法條內容為"+data[idx][5]
    law_item += "查詢結束"
    self.line_speaker(law_item)

def input_by_number(self):
    number_of = self.listener()
    number_of = chinese_in_string_transform(number_of)
    search_parameter = []
    if '之' in number_of:
        number_of = number_of.split('之')
        number_of[0] = "".join(filter(str.isdigit, number_of[0]))
        number_of[1] = "".join(filter(str.isdigit, number_of[1]))
        search_parameter.append(number_of[0])
        search_parameter.append(number_of[1])
    else:
        number_of = "".join(filter(str.isdigit, number_of))
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
    self.line_speaker('條號:')
    number = ''
    number_in = self.listener()
    number_in = chinese_in_string_transform(number_in)
    number = number.join(filter(str.isdigit, number_in))
    while number.isdigit()==0:
        self.line_speaker("請再說一次")
        number = ''
        number_in = self.listener()
        number_in = chinese_in_string_transform(number_in)
        number = number.join(filter(str.isdigit, number_in))
    self.line_speaker('之幾:')
    of = ''
    of_in = self.listener()
    of_in = chinese_in_string_transform(of_in)
    of = of.join(filter(str.isdigit, of_in))
    while of.isdigit()==0:
        self.line_speaker("請再說一次")
        of = ''
        of_in = self.listener()
        of_in = chinese_in_string_transform(of_in)
        of = of.join(filter(str.isdigit, of_in))
    self.line_speaker('法條名:')
    name = self.listener()
    self.line_speaker('選擇確認或取消告訴乃論?')
    isNTWC = self.listener()
    while isNTWC != '確認' and isNTWC != '取消':
        self.line_speaker("請再說一次")
        isNTWC = self.listener()
    if isNTWC == '確認':
        isNTWC = '1'
    else:
        isNTWC = '0'
    issin = '0'
    self.line_speaker('法條內容:')
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

def chinese_to_arabic(chinese_num):
    chinese_char_dict = {
        '〇' : 0, '一' : 1, '二' : 2, '三' : 3, '四' : 4, '五' : 5, '六' : 6, '七' : 7, '八' : 8, '九' : 9, '零' : 0,
        '壹' : 1, '贰' : 2, '叁' : 3, '肆' : 4, '伍' : 5, '陆' : 6, '柒' : 7, '捌' : 8, '玖' : 9, '貮' : 2, '两' : 2,
    }
    chinese_char_unit = {
        '十' : 10,
        '拾' : 10,
        '百' : 100,
        '佰' : 100,
        '千' : 1000,
        '仟' : 1000,
        '万' : 10000,
        '萬' : 10000,
        '亿' : 100000000,
        '億' : 100000000,
        '兆' : 1000000000000,
    }
    unit = 0
    ldig = []
    # print(chinese_num)
    for char_digit in reversed(chinese_num):
        # print(char_digit)
        if chinese_char_unit.get(char_digit) != None:
            unit = chinese_char_unit.get(char_digit)
            # print("unit:"+str(unit))
            if unit == 10000 or unit == 100000000:
                ldig.append(unit)
                unit = 1
        else:
            dig = chinese_char_dict.get(char_digit)
            # print("num:"+str(dig))
            if unit:
                dig *= unit
                unit = 0
            ldig.append(dig)
    if unit == 10:
        ldig.append(10)
    val, tmp = 0, 0
    for x in reversed(ldig):
        if x == 10000 or x == 100000000:
            val += tmp * x
            tmp = 0
        else:
            tmp += x
    val += tmp
    return val

# print(chinese_to_arabic("九億七千八百萬八千八百八十八"))
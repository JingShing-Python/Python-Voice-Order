import re
from chinese_num_conf import UNIT_CN2AN
all_num = "零一二三四五六七八九"
all_unit = "".join(list(UNIT_CN2AN.keys()))
cn_pattern = f"負?([{all_num}{all_unit}]+點)?[{all_num}{all_unit}]+"
smart_cn_pattern = f"-?([0-9]+.)?[0-9]+[{all_unit}]+"
def chinese_to_arabic(chinese_num):
    chinese_char_dict = {
        '〇' : 0, '一' : 1, '二' : 2, '三' : 3, '四' : 4, '五' : 5, '六' : 6, '七' : 7, '八' : 8, '九' : 9, '零' : 0,
        '壹' : 1, '贰' : 2, '叁' : 3, '肆' : 4, '伍' : 5, '陆' : 6, '柒' : 7, '捌' : 8, '玖' : 9, '貮' : 2, '兩' : 2,
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
    for char_digit in reversed(chinese_num):
        if chinese_char_unit.get(char_digit) != None:
            unit = chinese_char_unit.get(char_digit)
            if unit == 10000 or unit == 100000000:
                ldig.append(unit)
                unit = 1
        else:
            dig = chinese_char_dict.get(char_digit)
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
def __sub_util(inputs, sub_mode: str = "number") -> str:
        try:
            if inputs:
                if sub_mode == "date":
                    return re.sub(fr"(({smart_cn_pattern})|({cn_pattern}))",
                                    lambda x: str(chinese_to_arabic(x.group())), inputs)
                elif sub_mode == "fraction":
                    if inputs[0] != "百":
                        frac_result = re.sub(cn_pattern,
                                                lambda x: str(chinese_to_arabic(x.group())), inputs)
                        numerator, denominator = frac_result.split("分之")
                        return f"{denominator}/{numerator}"
                    else:
                        return inputs
                elif sub_mode == "percent":
                    return re.sub(f"(?<=百分之){cn_pattern}",
                                    lambda x: str(chinese_to_arabic(x.group())), inputs).replace("百分之", "") + "%"
                elif sub_mode == "celsius":
                    return re.sub(f"{cn_pattern}(?=攝氏度)",
                                    lambda x: str(chinese_to_arabic(x.group())), inputs).replace("攝氏度", "℃")
                elif sub_mode == "number":
                    return str(chinese_to_arabic(inputs))
                else:
                    raise Exception(f"error sub_mode: {sub_mode} !")
        except Exception as e:
            print(f"WARN: {e}")
            return inputs
def chinese_in_string_transform(inputs: str) -> str:
    inputs = inputs.replace("廿", "二十").replace("半", "0.5").replace("两", "2").replace('兩','2')
    # date
    inputs = re.sub(
        fr"((({smart_cn_pattern})|({cn_pattern}))年)?([{all_num}十]+月)?([{all_num}十]+日)?",
        lambda x: __sub_util(x.group(),"date"), inputs)
    # fraction
    inputs = re.sub(fr"{cn_pattern}分之{cn_pattern}",
                    lambda x: __sub_util(x.group(),"fraction"), inputs)
    # percent
    inputs = re.sub(fr"百分之{cn_pattern}",
                    lambda x: __sub_util(x.group(),"percent"), inputs)
    # celsius
    inputs = re.sub(fr"{cn_pattern}攝氏度",
                    lambda x: __sub_util(x.group(),"celsius"), inputs)
    # number
    output = re.sub(cn_pattern,
                    lambda x: __sub_util(x.group(),"number"), inputs)
    return output

if __name__ == '__main__':
    # num = '一千七百七十一個蛋糕'
    num = input()
    print(chinese_in_string_transform(num))
    # nume = '十七億三千萬零八'
    # print(chinese_to_arabic(nume))
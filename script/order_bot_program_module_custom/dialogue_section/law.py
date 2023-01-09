from law_process.db import search_by_number, search_by_str, save_to_db
from law_process.law_toolkit import print_single_law, input_by_number, input_by_str, input_all_info
from chinese_num_transform import chinese_in_string_transform
import time


def law(self):
    dbpath = 'script\order_bot_program_module_custom\law_process\datebase\law.db'
    # mode search ,add ,and modify
    self.line_speaker("條號查詢請說第一，法條名查詢請說第二")
    mode = ''
    mode_in = self.listener()
    mode_in = chinese_in_string_transform(mode_in)
    mode = mode.join(filter(str.isdigit, mode_in))
    while mode != "1" and mode != "2" and mode != "3" and mode != "4":
        self.line_speaker("請再說一次")
        mode = ''
        mode_in = self.listener()
        mode_in = chinese_in_string_transform(mode_in)
        mode = mode.join(filter(str.isdigit, mode_in))
    if mode == '1':
        search_parameter = []
        self.line_speaker("請說出條號，如363條、334條之1")
        search_parameter = input_by_number(self)
        result = search_by_number(dbpath, search_parameter, 1)
        if not result:
            self.line_speaker("沒有找到法條，查詢結束")
        else:
            print_single_law(0, result, self)
    elif mode == '2':
        search_parameter = []
        self.line_speaker("請說出法條名，如殺人罪")
        search_parameter = input_by_str(self)
        result = search_by_str(dbpath, search_parameter, 1)
        if not result:
            self.line_speaker("沒有找到法條，查詢結束")
        else:
            self.line_speaker("找到"+str(len(result))+"條法條")
            time.sleep(1.8)
            if len(result) > 1:
                law_item = ''
                for i in range(len(result)):
                    law_item += '結果'+str(i+1)
                    law_item += result[i][2] + '\n'
                self.line_speaker(law_item)
                time.sleep(len(law_item)*0.32)
                self.line_speaker("選擇念出哪條法條")
                choose = ''
                choose_in = self.listener()
                choose_in = chinese_in_string_transform(choose_in)
                choose = choose.join(filter(str.isdigit, choose_in))
                while (1):
                    if choose.isdigit() == 1:
                        if int(choose) <= len(result) and int(choose) > 0:
                            break
                    self.line_speaker("請再說一次")
                    choose = ''
                    choose_in = self.listener()
                    choose_in = chinese_in_string_transform(choose_in)
                    choose = choose.join(filter(str.isdigit, choose_in))
                print_single_law(int(choose)-1, result, self)
            elif len(result) == 1:
                print_single_law(0, result, self)

    elif mode == '3':
        self.line_speaker("因為語音辨識的準確度，建議以文字輸入方式輸入新增")
        time.sleep(len("因為語音辨識的準確度，建議以文字輸入方式輸入新增")*0.32)
        self.line_speaker("選擇確認或取消繼續新增")
        isadd = self.listener()
        while isadd != '確認' and isadd != '取消':
            self.line_speaker("請再說一次")
            isadd = self.listener()
        if isadd == '確認':
            search_parameter, modify_parameter = input_all_info(self)
            result = search_by_number(dbpath, search_parameter, 1)
            if result:
                self.line_speaker("該法條已存在，選擇確認或取消更新")
                isupdate = self.listener()
                while isupdate != '確認' and isupdate != '取消':
                    self.line_speaker("請再說一次")
                    isupdate = self.listener()
                if isupdate == '確認':
                    save_to_db(dbpath, 1, modify_parameter)
                    self.line_speaker("更新成功，結束更新")
                else:
                    self.line_speaker("結束新增")
            else:
                save_to_db(dbpath, 0, modify_parameter)
                self.line_speaker("新增成功，結束新增")

        else:
            self.line_speaker("結束新增")
    else:
        self.line_speaker("因為語音辨識的準確度，建議以文字輸入方式輸入更新")
        time.sleep(len("因為語音辨識的準確度，建議以文字輸入方式輸入新增")*0.32)
        self.line_speaker("選擇確認或取消繼續更新")
        isadd = self.listener()
        while isadd != '確認' and isadd != '取消':
            self.line_speaker("請再說一次")
            isadd = self.listener()
        if isadd == '確認':
            search_parameter, modify_parameter = input_all_info(self)
            result = search_by_number(dbpath, search_parameter, 1)
            if not result:
                self.line_speaker("該法條不存在，選擇確認或取消新增")
                isupdate = self.listener()
                while isupdate != '確認' and isupdate != '取消':
                    self.line_speaker("請再說一次")
                    isupdate = self.listener()
                if isupdate == '確認':
                    save_to_db(dbpath, 0, modify_parameter)
                    self.line_speaker("新增成功，結束新增")
                else:
                    self.line_speaker("結束更新")
            else:
                save_to_db(dbpath, 1, modify_parameter)
                self.line_speaker("更新成功，結束更新")
        else:
            self.line_speaker("結束更新")

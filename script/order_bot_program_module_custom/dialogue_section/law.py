from law_process.db import search_by_number, search_by_str, save_to_db
from law_process.law_toolkit import print_single_law, input_by_number, input_by_str, input_all_info
from chinese_num_transform import chinese_in_string_transform

def law(self):
    dbpath = 'script\order_bot_program_module_custom\law_process\datebase\law.db'
    ### test data ###
    test1 = '第235'
    test2 = '235'
    test3 = '第235'
    test4 = "235條"
    mode1 = "第一"
    ### test data ###
    # mode search ,add ,and modify
    self.line_speaker("請選擇要執行的模式，透過條號查詢請說第一，透過法條名搜尋請說第二，新增法條請說第三，修改法條請說第四")
    mode = ''
    mode_in = self.listener()
    mode_in = chinese_in_string_transform(mode_in)
    mode = mode.join(filter(str.isdigit, mode_in))
    while mode != "1" and mode != "2" and mode != "3" and mode != "4":
        self.line_speaker("請再說一次")
        mode = self.listener()
        mode = chinese_in_string_transform(mode)
        mode = mode.join(filter(str.isdigit, mode))
    # result_law is a list which contains research result.
    if mode == '1':
        search_parameter = []
        self.line_speaker("請說出要查詢的條號，如363條、334條之1")
        search_parameter = input_by_number(self)
        result = search_by_number(dbpath, search_parameter, 1)
        if not result:
            self.line_speaker("很抱歉，沒有找到法條")
        else:
            print_single_law(0, result)
    elif mode == '2':
        search_parameter = []
        self.line_speaker("請說出要查詢的法條名，如殺人罪")
        search_parameter = input_by_str(self)
        result = search_by_str(dbpath, search_parameter, 1)
        if not result:
            self.line_speaker("很抱歉，沒有找到法條")
        else:
            self.line_speaker("找到"+str(len(result))+"條法條")
            self.line_speaker("選擇確認或取消念出法條")
            isdisplay = self.listener()
            while isdisplay != '確認' and isdisplay != '取消':
                self.line_speaker("請再說一次")
                isdisplay = self.listener()
            if isdisplay == '確認':
                if len(result) == 1:
                    print_single_law(0, result)
                else:
                    for i in range(len(result)):
                        self.line_speaker('結果'+str(i+1))
                        print_single_law(i, result)
            else:
                self.line_speaker("結束")
                exit()
    elif mode == '3':
        self.line_speaker("因為語音辨識的準確度，建議以文字輸入方式輸入新增")
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
                        self.line_speaker("更新成功")
                    else:
                        self.line_speaker("結束新增")
                        exit()
                else:
                    save_to_db(dbpath, 0, modify_parameter)
                    self.line_speaker("新增成功")

        else:
            self.line_speaker("結束")
            exit()
    else:
        self.line_speaker("因為語音辨識的準確度，建議以文字輸入方式輸入更新")
        self.line_speaker("選擇確認或取消繼續更新")
        isadd = self.listener()
        while isadd != '確認' and isadd != '取消':
            self.line_speaker("請再說一次")
            isadd = self.listener()
        if isadd == '確認':
            search_parameter, modify_parameter = input_all_info(self)
            result = search_by_number(dbpath, search_parameter, 1)
            if not result:
                print("該法條不存在，選擇確認或取消新增")
                isupdate = self.listener()
                while isupdate != '確認' and isupdate != '取消':
                    print("請再說一次")
                    isupdate = self.listener()
                if isupdate == '確認':
                    save_to_db(dbpath, 0, modify_parameter)
                    print("新增成功")
                else:
                    print("結束更新")
                    exit()
            else:
                save_to_db(dbpath, 1, modify_parameter)
                print("更新成功")
        else:
            self.line_speaker("結束")
            exit()
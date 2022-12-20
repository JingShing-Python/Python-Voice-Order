from order_process.process_order import load_xlsx, process_data_to_menu, process_price_with_order
menu_xlsx_path = 'script\order_bot_program_module_custom\order_process\menu.xlsx'
data_dict = load_xlsx(file_name=menu_xlsx_path)
menu_dict = process_data_to_menu(data_dict)
def order_meal(self):
    total_order = ''
    self.line_speaker('請問要點些什麼呢？')
    while(1):
        order_menu_line = self.listener()
        if '和' in order_menu_line or '個' in order_menu_line:
            total_order+=order_menu_line+'和'
        elif '餐' in order_menu_line or '點完' in order_menu_line:
            # 點完餐
            break
        else:
            self.line_speaker('不好意思，請再說一次。')
    self.line_speaker(process_price_with_order(menu_dict, total_order))
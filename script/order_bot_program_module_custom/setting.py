command_data_dict = {'command_line':'',
                'is_command':False,
                'bot_reply':''}
module_data_dict = dict()

# exit
try:
    import sys
    module_data_dict['離開']=sys.exit
    module_data_dict['結束']=sys.exit
except:
    pass

module_import_dict={
    # calculater
    '餐':'order_meal',
    '方':'equation',
    # dialogue
    '你好':'hello',
    '我是':'my_name',
    '我的名字是':'my_name',
    '吃的':'what_eat',
    '機率':'fake_rate',
    '幾點':'what_time',
    '時間':'what_time',
}

for key in module_import_dict.keys():
    program = '''
try:
    from dialogue_section.'''+module_import_dict[key]+''' import '''+module_import_dict[key]+'''
    module_data_dict["'''+key+'''"]='''+module_import_dict[key]+'''
except:
    pass
'''
    exec(program)
    # print(program)
print(module_data_dict)

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

# dialogue
# hello
try:
    from dialogue_section.hello import hello
    module_data_dict['你好']=hello
except:
    pass
# my name
try:
    from dialogue_section.my_name import my_name
    module_data_dict['我是']=my_name
    module_data_dict['我的名字是']=my_name
except:
    pass
# what eat
try:
    from dialogue_section.what_eat import what_eat
    module_data_dict['吃的']=what_eat
except:
    pass
# fake rate
try:
    from dialogue_section.fake_rate import fake_rate
    module_data_dict['機率']=fake_rate
except:
    pass
# what time
try:
    from dialogue_section.what_time import what_time
    module_data_dict['幾點']=what_time
    module_data_dict['時間']=what_time
except:
    pass

# calculater
# order meal
try:
    from dialogue_section.order_meal import order_meal
    module_data_dict['餐']=order_meal
except:
    pass

# equation
try:
    from dialogue_section.equation import equation
    module_data_dict['方']=equation
except:
    pass
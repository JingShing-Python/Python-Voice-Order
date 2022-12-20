def what_eat(self):    
    eat_count = 0
    self.line_speaker('想吃飯還是麵？')
    while(eat_count<2):
        order_line = self.listener()
        if '飯' in order_line:
            self.line_speaker('我們沒有飯')
            eat_count+=1
        elif '麵' in order_line:
            self.line_speaker('我們沒有麵')
            eat_count+=1
        else:
            self.line_speaker('我們沒有這個')
    self.line_speaker('我們有水餃')
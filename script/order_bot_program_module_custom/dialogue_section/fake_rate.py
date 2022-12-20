def fake_rate(self):
    self.line_speaker('請描述你所要計算的機率問題。講完後請說我說完了')
    while(not '完' in order_line):
        order_line = self.listener()
    self.line_speaker('請問所求為會發生還是不會發生的機率？')
    order_line = self.listener()
    while(not '會' in order_line):
        order_line = self.listener()
    if '不會' in order_line:
        self.line_speaker('二分之一')
    else:
        self.line_speaker('二分之一')
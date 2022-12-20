def hello(self):
    self.line_speaker('你好。')
    if self.master!=None:
        self.line_speaker('我的'+self.master)
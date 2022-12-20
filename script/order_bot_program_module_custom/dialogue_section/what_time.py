from datetime import datetime
def what_time(self):
    now = datetime.now()
    res_text = '現在時間是 %d 點 %d 分 %d 秒' % (now.hour, now.minute, now.second)
    self.line_speaker(res_text)
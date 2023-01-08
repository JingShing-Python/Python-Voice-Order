#change num
from chinese_num_transform import chinese_in_string_transform
#re
import re
#numpy
import numpy as np

from time import sleep

def equation(self):
    self.line_speaker('請講一下是甚麼題目讓你連一元一次方程式都不會解的？')
    self.line_speaker('先講一下題目有幾個變數？')
    # ex: 兩個 -> 2
    try:
       var_num = int(re.findall(r'(\d+)(?=個)',chinese_in_string_transform(self.listener()))[0])
    except:
       self.line_speaker('請再說一次..')
    self.line_speaker('有{}個變數，請說{}個方程式。'.format(var_num,var_num))
    # AX=B
    A = np.array([[0]*var_num for _ in range(var_num)], dtype=float)
    B = np.array([[0] for _ in range(var_num)], dtype=float)
    X = np.array([[None] for _ in range(var_num)], dtype=float)
    for i in range(var_num):
        while True:
            self.line_speaker('可以開始說了..')
            math_line = self.listener()    
            math_line = chinese_in_string_transform(math_line)
            math_line = re.sub(r'[負副富減]+','-',math_line)
            math_line = re.sub(r'等於','=',math_line)
            math_line = re.sub(r'加','+',math_line)
            math_line = re.sub(r'[立力例]','z',math_line)
            math_line = re.sub(r'(?<=\D)(?=[xyz])|^(?=[xyz])','1',math_line)
            if len(re.findall(r'([^.xyzXYZ\+\-\d=])',math_line))!=0 or math_line[-1]=='=' or not '=' in math_line:
                self.line_speaker('請再說一次..')
            else:
                break
        if var_num >= 1:
            finda = re.findall(r'([\+\-\d]+)x',math_line)
            A[i][0] = int(finda[0]) if len(finda)>=1 else 0
        if var_num >= 2:
            finda = re.findall(r'x?([\+\-\d]+)y',math_line)
            A[i][1] = int(finda[0]) if len(finda)>=1 else 0
        if var_num >= 3:
            finda = re.findall(r'x?y?([\+\-\d]+)z',math_line)
            A[i][2] = int(finda[0]) if len(finda)>=1 else 0
        findx = re.findall(r'=(.*)',math_line)
        try:
            B[i][0] = float(findx[0])
        except:
            B[i][0] = 0
    have_ans=True
    try:
        X = np.linalg.inv(A).dot(B)
    except:
        have_ans=False
    if have_ans:
        ans = [X[k][0] for k in range(len(X))]
        for i in range(len(ans)):
            if ans[i]-int(ans[i])==0.0:
                ans[i]=int(ans[i])
        if var_num==1:
            self.line_speaker('X等於{}'.format(ans[0]))
        elif var_num==2:
            self.line_speaker('X等於{}\nY等於{}'.format(ans[0],ans[1]))
        else:
            self.line_speaker('X等於{}\nY等於{}\nZ等於{}'.format(ans[0],ans[1],ans[2]))
    else:
        self.line_speaker('此題無解or無限解 ^_^')
    sleep(2)
    self.line_speaker('很高興為您服務，如果你需要法律諮詢，我們也可以為您解惑')

from chinese_num_transform import chinese_in_string_transform

def BMR_coculator(sex, height, weight, age):
    if sex == '男':
        bmr = round(10 * weight + 6.25 * height - 5 * age + 5, 2)
        return bmr
    if sex == '女':
        bmr = round(10 * weight + 6.25 * height - 5 * age - 161, 2)
        return bmr

def TDEE_coculator(exer, bmr):
    if exer == 1:
        tdee = bmr * 1.2
    if exer == 2:
        tdee = bmr * 1.375
    if exer == 3:
        tdee = bmr * 1.55
    if exer == 4:
        tdee = bmr * 1.725
    if exer == 5:
        tdee = bmr * 1.9
    tdee = round(tdee, 2)
    return tdee

def Nutrient_output(tdee, c, p, f):
    carbon = int(tdee*c/4)
    print(f'您的碳水化合物攝入量是{carbon}大卡')
    protein = int(tdee*p/4)
    print(f'您的蛋白質攝入量是{protein}大卡')
    fat = int(tdee*f/9)
    print(f'您的脂肪攝入量是{fat}大卡')

def fit(self):
    # self.line_speaker('您好，很高興為您服務，請問要做些甚麼？')
    self.line_speaker('您好，請問想計算什麼？')
    while (1):
        order_line = self.listener()
        # 給健身新手參考
        # 計算基礎代謝率(BMR)
        if '代謝' in order_line:
            self.line_speaker('請問您的性別(男 or 女)?')
            sex = self.listener()
            while (1):
                if '男' or '南' in sex:
                    sex = '男'
                    break
                elif '女' in sex:
                    sex = '女'
                    break
                else:
                    continue

            self.line_speaker('請問您的身高是(公分)?')
            while (1):
                temp_height = self.listener()
                height = chinese_in_string_transform(temp_height)
                try:
                    height = int(height)
                    if height >= 100 and height <= 250:
                        break
                except:
                    self.line_speaker('請再說一次')
                    continue

            self.line_speaker('請問您的體重是(公斤)?')
            while (1):
                temp_weight = self.listener()
                weight = chinese_in_string_transform(temp_weight)
                try:
                    weight = int(weight)
                    if weight >= 30 and weight <= 150:
                        break
                except:
                    self.line_speaker('請再說一次')
                    continue

            self.line_speaker('請輸入您的年齡?')
            while (1):
                temp_age = self.listener()
                age = chinese_in_string_transform(temp_age)
                try:
                    age = int(age)
                    if age >= 0 and age <= 130:
                        break
                except:
                    self.line_speaker('請再說一次')
                    continue

            bmr = BMR_coculator(sex, height, weight, age)
            self.line_speaker(f"您的基礎代謝率(BMR):{bmr}")
            break

        # 計算TDEE(總熱量消耗)
        elif '熱量' in order_line:
            self.line_speaker('請問您是否知道自己的基礎代謝率?')
            check = self.listener()
            while (1):
                if '是' in check:
                    self.line_speaker('您的基礎代謝率是?')
                    while (1):
                        temp_bmr = self.listener()
                        bmr = chinese_in_string_transform(temp_bmr)
                        try:
                            bmr = int(bmr)
                            if bmr >= 0 and bmr <= 3000:
                                break
                        except:
                            self.line_speaker('請再說一次')
                            continue
                    break
                elif '否' in check:
                    self.line_speaker('現在幫您計算')
                    self.line_speaker('請問您的性別(男 or 女)?')
                    sex = self.listener()
                    while (1):
                        if '男' or '南' in sex:
                            sex = '男'
                            break
                        elif '女' in sex:
                            sex = '女'
                            break
                        else:
                            self.line_speaker('請再說一次')
                            continue

                    self.line_speaker('請問您的身高是(公分)?')
                    while (1):
                        temp_height = self.listener()
                        height = chinese_in_string_transform(temp_height)
                        try:
                            height = int(height)
                            if height >= 100 and height <= 250:
                                break
                        except:
                            self.line_speaker('請再說一次')
                            continue

                    self.line_speaker('請問您的體重是(公斤)?')
                    while (1):
                        temp_weight = self.listener()
                        weight = chinese_in_string_transform(temp_weight)
                        try:
                            weight = int(weight)
                            if weight >= 30 and weight <= 150:
                                break
                        except:
                            self.line_speaker('請再說一次')
                            continue

                    self.line_speaker('請輸入您的年齡?')
                    while (1):
                        temp_age = self.listener()
                        age = chinese_in_string_transform(temp_age)
                        try:
                            age = int(age)
                            if age >= 0 and age <= 130:
                                break
                        except:
                            self.line_speaker('請再說一次')
                            continue

                    bmr = BMR_coculator(sex, height, weight, age)
                    break
                else:
                    self.line_speaker('請再說一次')
                    continue

            print("請原則下列活動量敘述")
            print("(1)久坐，幾乎沒運動")
            print("(2)每周低強度運動1~3天")
            print("(3)每周中強度運動3~5天")
            print("(4)每周高強度運動6~7天")
            print("(5)每天超高強度運動")
            while (1):
                temp_exer = self.listener()
                exer = chinese_in_string_transform(temp_exer)
                try:
                    exer = int(exer)
                    if exer >= 1 and exer <= 5:
                        break
                except:
                    continue

            tdee = TDEE_coculator(exer, bmr)
            self.line_speaker(f"您的總熱量消耗(TDEE):{tdee}")
            break

        # 計算 增肌(高碳)/減脂(低碳)/增肌減脂(碳循環)
        elif '飲食' in order_line:
            self.line_speaker('請問您是否知道自己的TDEE?')
            while (1):
                check = self.listener()
                if '是' in check:
                    self.line_speaker('您的總熱量消耗是?')
                    while (1):
                        temp_tdee = self.listener()
                        tdee = chinese_in_string_transform(temp_tdee)
                        try:
                            tdee = int(self.listener())
                            if tdee >= 1000 and tdee <= 4500:
                                break
                        except:
                            print('請再說一次')
                            continue
                    self.line_speaker('請問您的性別(男 or 女)?')
                    while (1):
                        sex = self.listener()

                        if '男' or '南' in sex:
                            print('請問您要增肌/減脂/增肌減脂?')  # 還要判斷性別
                            mode = self.listener()
                            if mode == '增肌':  # (高碳) tdee + 150
                                Nutrient_output(tdee+150, 0.45, 0.35, 0.2)
                                break
                            elif mode == '減脂':  # (低碳) tdee * 0.8
                                Nutrient_output(tdee*0.8, 0.2, 0.4, 0.4)
                                break
                            elif mode == '增肌減脂':  # (碳循環) tdee+200 tdee tdee-200
                                print('您的高碳日攝入量是:')
                                Nutrient_output(tdee+200, 0.45, 0.35, 0.2)
                                print('您的中碳日攝入量是:')
                                Nutrient_output(tdee, 0.35, 0.35, 0.3)
                                print('您的低碳日攝入量是:')
                                Nutrient_output(tdee-200, 0.2, 0.4, 0.4)
                                break
                            else:
                                print('請再說一次')
                                continue

                        elif '女' in sex:
                            self.line_speaker('請問您要增肌/減脂/增肌減脂?')  # 還要判斷性別
                            mode = self.listener()
                            if mode == '增肌':  # (高碳) tdee + 100
                                Nutrient_output(tdee+100, 0.45, 0.35, 0.2)
                                break
                            elif mode == '減脂':  # (低碳) tdee * 0.8
                                Nutrient_output(tdee*0.8, 0.2, 0.4, 0.4)
                                break
                            elif mode == '增肌減脂':  # (碳循環) tdee + 100 tdee tdee-100
                                print('您的高碳日攝入量是:')
                                Nutrient_output(tdee+100, 0.45, 0.35, 0.2)
                                print('您的中碳日攝入量是:')
                                Nutrient_output(tdee, 0.35, 0.35, 0.3)
                                print('您的低碳日攝入量是:')
                                Nutrient_output(tdee-100, 0.2, 0.4, 0.4)
                                break
                            else:
                                self.line_speaker('請再說一次')
                                continue

                        else:
                            self.line_speaker('請再說一次')
                            continue

                    break

                elif '否' in check:
                    self.line_speaker('請先去測量')
                    break

                else:
                    self.line_speaker('請再說一次')
                    continue
            break

        # 離開
        elif '離開' in order_line or '結束' in order_line:
            self.line_speaker('很高興為您服務。')
            break

        # not any option upper
        else:
            self.line_speaker('請再說一次')
            continue
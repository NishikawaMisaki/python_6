import sys
import datetime
args = sys.argv


# classの定義
class Aquacalc:
    def __init__(self, day, adult, child):
        '''self.day, self.adult, self.childを定義'''
        self.day = day 
        self.adult = adult
        self.child = child


    # 関数fee_sumの定義
    def fee_sum(self):
        '''合計金額を計算する関数'''
        
        # weekに何曜日なのかを「0～6（日曜～土曜）」を代入する
        t = datetime.date(int(self.day[:4]), int(self.day[4:6]), int(self.day[6:]))
        week = int(t.strftime("%w"))

        # holidayに"土日"か"平日"を代入する
        if week == 0 or week == 6:
            self.holiday = "土日"
        else:
            self.holiday = "平日"
        
        # 合計金額を計算
        self.fee_sum = fee[self.holiday]['大人']*self.adult + fee[self.holiday]['子供']*self.child


    # 関数fee_sum_outの定義
    def fee_sum_out(self):
        return self.fee_sum



# 引数を変数に代入
day = args[1] # 日付（yyyymmdd）
adult = int(args[2]) # 大人の人数
child = int(args[3]) # 子供の人数


# 入場料をfeeに定義する
fee = {'平日': {'大人':2000, '子供':1200}, '土日': {'大人':2400, '子供':1500}}


# 料金の合計を求める
group1 = Aquacalc(day, adult, child)
group1.fee_sum()
fee_sum = group1.fee_sum_out()

# 料金の合計を出力
print(fee_sum, end="")
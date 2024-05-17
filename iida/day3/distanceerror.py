import sys
args = sys.argv

name1 = args[1]
name2 = args[2]


station = {'東京': 0.00, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

try:
    print(round(abs(station[name1] - station[name2]), 2), end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")
from decimal import Decimal, ROUND_HALF_UP

import sys
args = sys.argv

station_1 = args[1]
station_2 = args[2]

distance = {"東京": 0.00,"品川": 6.78,"新横浜": 25.54 ,"名古屋": 342.02 ,"京都":476.31,"新大阪":515.35}

answer = distance[station_2] - distance[station_1]

if answer < 0:
    answer = answer * (-1)

answer = Decimal(str(answer)).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)

answer = round(answer,2)

print(answer,end="")
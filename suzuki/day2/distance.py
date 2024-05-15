import sys
args = sys.argv
sta1 = args[1]
sta2 = args[2]
dis = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}
if dis[sta1] > dis[sta2]:
   A = dis[sta1] - dis[sta2]
   truncated_number_round = round(A, 2)
   print(truncated_number_round, end="")
else:
   A = dis[sta2] - dis[sta1]
   truncated_number_round = round(A, 2)
   print(truncated_number_round, end="")
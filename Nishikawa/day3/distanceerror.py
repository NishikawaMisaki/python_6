import sys
args=sys.argv

station={'東京':0.00,'品川':6.78,'新横浜':25.54,'名古屋':342.02,'京都':476.31,'新大阪':515.35}

start = args[1]
goal = args[2]

try:
    distance=station[goal]-station[start]

    if distance <0:
     distance=distance*(-1)

    print(round(distance,2),end="")

except:
    print("のぞみの停車駅を引数に設定してください")
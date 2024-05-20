import sys
import datetime
from datetime import date
from database import session
from tables import Holiday


# データを取得する


args = sys.argv

a = args[1]
b = int(args[2])
c = int(args[3])


pay = {'平日': {'大人':2000, '子供':1200}, '土日': {'大人':2400, '子供':1500}}

t = datetime.date(int(a[:4]), int(a[4:6]), int(a[6:]))
week = int(t.strftime("%w"))




if week == 0 or week == 6:
    a = "土日"
else:
    a = "平日"

get_date = session.query(Holiday.holi_date).filter_by(holi_date = t).first()

if  get_date is None:
    pass
else:
    a = "土日"


sum = pay[a]['大人']*b + pay[a]['子供']*c

print(sum)

#print(holidaylist)

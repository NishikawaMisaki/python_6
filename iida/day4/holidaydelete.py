from datetime import date
from database import session
from tables import Holiday

# 削除するデータを取得する
result = session.query(Holiday).delete()

#コミット
session.commit()
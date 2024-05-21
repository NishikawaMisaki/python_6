from datetime import date
from database import session
from tables import Mst_merchandise

# 登録するデータの編集
holiday= Mst_merchandise(
    id = date(2024, 1, 1),
    name = "お正月",
    price = "price"
)
#INSERT処理
session.add(holiday)
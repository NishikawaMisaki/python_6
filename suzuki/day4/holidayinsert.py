from datetime import date
from database import session
from tables import Holiday

# 登録するデータの編集
holiday= Holiday(
    holi_date = date(2024, 1, 1),
    holi_text = "お正月"
)
#INSERT処理
session.add(holiday)

holiday= Holiday(
    holi_date = date(2024, 1, 8),
    holi_text = "成人の日"
)
#INSERT処理
session.add(holiday)

holiday= Holiday(
    holi_date = date(2024, 2, 12),
    holi_text = "建国記念の日"
)
#INSERT処理
session.add(holiday)

holiday= Holiday(
    holi_date = date(2024, 2, 23),
    holi_text = "天皇誕生日"
)
#INSERT処理
session.add(holiday)

holiday= Holiday(
    holi_date = date(2024, 3, 20),
    holi_text = "春分の日"
)
#INSERT処理
session.add(holiday)

holiday= Holiday(
    holi_date = date(2024,4, 29),
    holi_text = "昭和の日"
)
#INSERT処理
session.add(holiday)
holiday= Holiday(
    holi_date = date(2024, 5, 3),
    holi_text = "憲法記念日"
)
#INSERT処理
session.add(holiday)
holiday= Holiday(
    holi_date = date(2024, 5, 4),
    holi_text = "みどりの日"
)
#INSERT処理
session.add(holiday)
holiday= Holiday(
    holi_date = date(2024, 5, 6),
    holi_text = "こどもの日"
)
#INSERT処理
session.add(holiday)
holiday= Holiday(
    holi_date = date(2024, 7, 15),
    holi_text = "海の日"
)
#INSERT処理
session.add(holiday)
holiday= Holiday(
    holi_date = date(2024, 8, 12),
    holi_text = "山の日"
)
#INSERT処理
session.add(holiday)
holiday= Holiday(
    holi_date = date(2024, 9, 16),
    holi_text = "敬老の日"
)
#INSERT処理
session.add(holiday)

holiday= Holiday(
    holi_date = date(2024, 9, 23),
    holi_text = "秋分の日"
)
#INSERT処理
session.add(holiday)

holiday= Holiday(
    holi_date = date(2024, 10, 14),
    holi_text = "スポーツの日"
)
#INSERT処理
session.add(holiday)
holiday= Holiday(
    holi_date = date(2024, 11, 4),
    holi_text = "文化の日"
)
#INSERT処理
session.add(holiday)

#INSERT処理
session.add(holiday)
holiday= Holiday(
    holi_date = date(2024, 11, 23),
    holi_text = "勤労感謝の日"
)
#INSERT処理
session.add(holiday)
#コミット
session.commit()

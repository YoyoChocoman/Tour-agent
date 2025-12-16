import sqlite3
import json
from app.core.config import settings

class TourDB:
    def __init__(self):
        self.db_path = settings.DB_PATH
        self._init_table()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def _init_table(self):
        # category is the information category (e.g. restaurant, hotel...)
        # data is json after dumps
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS places (
                    uid TEXT PRIMARY KEY,
                    name TEXT,
                    city TEXT,
                    category TEXT,
                    data TEXT,
                    update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def upsert(self, city: str, category: str, item: dict):
        try:
            if category == "Restaurant":
                uid = item.get("RestaurantID")
                name = item.get("RestaurantName")
            elif category == "Hotel":
                uid = item.get("HotelID")
                name = item.get("HotelName")
            elif category == "ScenicSpot":
                uid = item.get("ScenicSpotID")
                name = item.get("ScenicSpotName")

            data = json.dumps(item, ensure_ascii=False)

            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO places (uid, name, city, category, data, update_at)
                    VALUES (?, ?, ?, ?, ?, datetime('now', 'localtime'))
                """, (uid, name, city, category, data)
                )
                conn.commit()

        except Exception as e:
            print(f"Error: {str(e)}")

    def get_db(self, city: str, category: str):
        OUTDATED_LIM = 1  # day
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(f"""
                    SELECT 1 FROM places WHERE city=? AND category=?
                    AND update_at < datetime('now', 'localtime', '-{OUTDATED_LIM} days')
                    LIMIT 1
                """, (city, category)
                )

                outdated_check = cursor.fetchone()
                if outdated_check:
                    print(f"Found local data but outdated. Ready to refetch...")
                    return []

                cursor.execute("""
                    SELECT data FROM places WHERE city=? AND category=?
                """, (city, category)
                )

                datas = cursor.fetchall()
                return [json.loads(data[0]) for data in datas]

        except Exception as e:
            print(f"Error: {str(e)}")
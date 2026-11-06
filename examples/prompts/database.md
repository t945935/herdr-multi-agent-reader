# Database

只修改 `examples/task_manager/db.py`。提供 init_db、get_tasks、get_task、create_task、update_task、delete_task。DB_PATH 可被測試替換；連線必須關閉，寫入使用交易，值採參數化 SQL。動態欄名必須由固定白名單產生。定義不存在時回傳 None／False，不將資料庫例外偽裝成空清單。

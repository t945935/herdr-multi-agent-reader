# QA

只修改 `tests/`。測試必須遵守需求，不靠降低規格讓測試通過。以 tmp_path 隔離 SQLite，使用 lifespan 啟動 TestClient。涵蓋 CRUD、型態、空值、未知欄位、不存在資料、重啟持久性。實際執行並記錄命令、版本、結束碼和失敗摘要。

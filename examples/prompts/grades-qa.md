# QA：成績系統

讀取 `examples/grades.py` 的介面與 `tests/test_contracts.py` 中既有成績案例。獨立檢查成績合約，不修改程式、不刪除既有測試，不讀取 Developer 的自評，不派生其他 Agent。

只新增或修改 `tests/test_grades_review.py`，並將報告寫入 `reports/grade-qa.md`。檢查三科集合、0／100／60 邊界、bool／NaN／字串、空資料、姓名、1／1／3 同分排名、未四捨五入的精度及輸入是否被修改。

使用 pytest。若案例已由既有測試充分涵蓋，先說明判準，再補上有價值的缺漏；不要複製一份完全相同的測試。不要測試 FastAPI、SQLite 或網站 CRUD，這是成績系統任務。

實際執行測試並保存命令、結束碼、發現與未執行事項。按 Manager 附加的 task_id 與 completion_path 寫入完成收據，artifacts 列出自己產生的報告及測試檔案。

# Developer：成績合約

先讀取 `examples/grades.py` 與 `tests/test_contracts.py` 中的成績案例。只修改 `examples/grades.py`；不修改既有測試、不改動網站程式，不派生其他 Agent。

合約：三科恰好為國文、英文、數學；分數為有限的 int／float，拒絕 bool、字串、缺科、額外科目及超出 0～100 的值。平均 60 分及格；空學生清單回傳空清單；相同未四捨五入總分採競賽排名，維持同分輸入順序；不修改輸入。

保留 calculate_total、calculate_average、get_grade、rank_students 的介面。先核對合約，必要時修正；若已符合，保留程式並說明檢查結果，不為了產生差異而改寫。

以 `.venv/bin/python -m pytest -q tests/test_contracts.py -k 'ranking or scores'` 驗證，將實際命令、結束碼、修改檔案及未處理事項寫入 `reports/grade-developer.md`。按 Manager 附加的 task_id 與 completion_path 寫入完成收據。

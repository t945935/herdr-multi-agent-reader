# 讀者實作包

所有命令從解壓縮後的專案根目錄執行；套件匯入使用 `examples.*`。

成績案例的派工提示為 `prompts/grades-developer.md` 與 `prompts/grades-qa.md`；`prompts/qa.md` 是網站專用提示。請在自己的練習副本派工，以便保留參考版本。

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
.venv/bin/python -m examples.pipeline
```

| 章 | 實作入口 | 驗收 |
| --- | --- | --- |
| 1 | `calculator.py` | 四則運算、零除與型態 |
| 2 | `grades.py` | 邊界成績、缺科、同分競賽排名 |
| 3 | `../scripts/probe_herdr.py --live` | 新建的 shell Pane 執行、讀取、等待及清理 |
| 4 | `../scripts/team.py` | 分階段派工、唯一任務識別、成果檔驗收 |
| 5 | `prompts/reviewer-a.md`、`reviewer-b.md` | 兩份獨立審查及 Manager 決策 |
| 6 | `handoff.py` | 檔案存在、專案範圍及 SHA-256 |
| 7 | `task_manager/` | CRUD、驗證、靜態網頁、重啟持久性 |
| 8 | `research.py` | 主張、來源、引文與未確定狀態 |
| 9 | `pipeline.py` | 結束碼、逾時、成果驗收、失敗停止 |
| 10 | `queue.py` | 重複提交、租約、重啟恢復、死信與併發 |

啟動網站：

```bash
.venv/bin/python -m uvicorn examples.task_manager.main:app --host 0.0.0.0 --port 8000
```

Windows 瀏覽器開啟 `http://localhost:8000/`。正式教學資料預設寫入 `examples/data/tasks.db`；自動測試使用暫存目錄，不接觸此檔。

背景佇列範例是有限次執行的純計算工作，不會呼叫付費模型。真正的模型派工由 `scripts/team.py` 明確執行；先完成對應 CLI 的安裝與登入。

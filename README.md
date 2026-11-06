# HERDR Multi-Agent 實戰教材：讀者實作包

這是《HERDR Multi-Agent 實戰教材》1.0 的讀者服務資源，版本 **v1.0.1**。包含可執行程式、角色提示詞、測試與操作說明。

維護者：Happy eBook／GitHub 帳號 t945935。

## 下載與版本

- [讀者資源庫](https://github.com/t945935/herdr-multi-agent-reader)
- [本書對應的 v1.0.1 下載頁](https://github.com/t945935/herdr-multi-agent-reader/releases/tag/v1.0.1)
- [下載 herdr-multi-agent-reader.zip](https://github.com/t945935/herdr-multi-agent-reader/releases/download/v1.0.1/herdr-multi-agent-reader.zip)
- [下載 SHA256SUMS.txt](https://github.com/t945935/herdr-multi-agent-reader/releases/download/v1.0.1/SHA256SUMS.txt)

公開版本可直接下載，不要求 GitHub 登入。將 ZIP 解壓到可寫入目錄；以下命令從解壓後、含 examples 與 tests 的根目錄執行。

## 環境與開始使用

建議 WSL2／Ubuntu、Python 3.12。安裝依賴需要網路；參考程式與測試不要求模型帳號。

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
.venv/bin/python -m examples.pipeline
```

預期測試結果：`42 passed`。管線會產生 `reports/pipeline/result.json`，成功狀態為 `passed`。

## 啟動任務網站

```bash
.venv/bin/python -m uvicorn examples.task_manager.main:app --host 0.0.0.0 --port 8000
```

在瀏覽器開啟 `http://localhost:8000/`。預設資料庫寫入 examples/data，測試資料全部使用暫存目錄。

## 檔案與章節對照

- 程式入口與章節對照：`examples/README.md`。
- 角色提示詞：`examples/prompts/`。
- 真實派工工具：`scripts/team.py`；先在 Herdr 內啟動並登入對應 Agent。
- 離線範例不要求模型登入；真實派工仍取決於使用者的 CLI、模型與授權。

## 檢查下載完整性

將 ZIP 與 SHA256SUMS.txt 放在同一目錄，在 Ubuntu 執行：

```bash
sha256sum -c SHA256SUMS.txt
```

預期顯示 `herdr-multi-agent-reader.zip: OK`。包內的 `resource-manifest.json` 另保存各檔案的 SHA-256。

## 問題回報與替代取得方式

請使用 [GitHub Issues](https://github.com/t945935/herdr-multi-agent-reader/issues)，附資源版本、系統、執行命令與不含個資的錯誤訊息。若直接下載連結失效，先到 v1.0.1 發行頁查看 Assets；也可以從資源庫的 Code → Download ZIP 取得程式。

本書 1.0 使用 v1.0.1，補充成績專用的 Developer／QA 提示；v1.0.0 仍保留。後續修正以新版本發行並保留對應紀錄；不承諾永久在線或即時更新。書中附錄亦收錄核心程式及提示詞。

## 使用範圍

本資源供配合本書閱讀與執行範例。目前未另行指定通用開源授權；公開可下載不等同於另行授予再散布或商用授權。如需其他使用方式，請透過 Issues 聯繫維護者。

# 本機實作驗收：只讀檢查

請讀取 examples/calculator.py，確認四個對外函式的名稱與零除例外。不要修改任何程式、測試或章稿，不呼叫其他 Agent。

在 Manager 指定的 completion_path 寫入完成 JSON，summary 說明你實際看到的函式與例外，artifacts 列出 examples/calculator.py 的絕對路徑。僅此一份完成紀錄可以寫入。讀不到檔案則回報 blocked，不虛構。

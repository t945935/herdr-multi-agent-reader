# Backend

只修改 `examples/task_manager/main.py`。使用 FastAPI lifespan 初始化資料表，拒絕未知欄位及型態轉換。POST 成功 201、PATCH 成功 200、DELETE 成功 204、不存在 404、不合法輸入 422。PATCH 的省略欄位保持原值，明確 null 拒絕；description 可以清空。不要更改 Database 所有的檔案。

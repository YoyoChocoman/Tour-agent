# Tour-Agent 的初步實作

這是一個專為 **OpenWebUI** 設計的後端擴充專案，提供增強的 Function Calling（工具調用）能力。本專案遵循 **12-Factor App** 原則構建，確保配置與代碼分離，並透過 Docker 容器化部署。

主要包含天氣查詢與旅遊推薦功能，並針對 LLM 的 Prompt 進行了優化，以確保輸出的格式與內容最符合用戶需求。

## 目前主要功能 (Features)

### 1. 天氣查詢 (Weather Tool)
- **功能**：獲取指定城市的即時天氣數據。
- **特點**：經過 Prompt 優化，包含溫度、濕度與天氣狀況，便於閱讀。
- **工具名稱**：`get_weather`

### 2. 客製化旅遊推薦 (Tourist Spot Tool)
- **功能**：查詢特定城市的旅遊景點。
- **特點**：從資料庫中篩選最合適的景點，並解釋推薦原因。(正在開發智慧篩選功能，使推薦根據使用者需求做調整)
- **工具名稱**：`get_tourist_spot`

### 3. 客製化餐廳推薦 (Restaurant Tool)
- **功能**：查詢特定城市的餐廳。
- **特點**：從資料庫中篩選最合適的餐廳，並解釋推薦原因。(正在開發智慧篩選功能，使推薦根據使用者需求做調整)
- **補充**：由於餐廳資料有不齊全狀況，因此若該縣市沒有餐廳資訊，會改回傳夜市資料
- **工具名稱**：`get_restaurant`

### 4. 客製化住宿推薦 (Hotel Tool)
- **功能**：查詢特定城市的住宿。
- **特點**：從資料庫中篩選最合適的住宿，並解釋推薦原因。(正在開發智慧篩選功能，使推薦根據使用者需求做調整)
- **工具名稱**：`get_hotel`

### 5. 安全與架構 (Architecture)
- **12-Factor App**：環境變數 (`.env`) 與程式碼完全分離。
- **Dockerized**：提供 `docker-compose` 支援，一鍵啟動。
- **SQLite 本地資料庫**：會設置本地資料庫避免重複請求API，也有助於後續更精準話回答

---

## 📂 專案結構 (Project Structure)

```text
.
├── app/                  # 主要應用程式邏輯 (Python)
│   ├── core/             # 核心資料，包括 API KEY 管理以及 DB 管理
│   ├── tools/            # 所有 Tools 管理
│   ├── utils/            # 所有輔助 Tools 的工具
│   └── main.py           # 主程式
├── openwebui_config/     # OpenWebUI 專用的工具設定檔與 Prompt 模板
├── .env.example          # 環境變數範例檔
├── .gitignore            # Git 忽略清單
├── docker-compose.yml    # Docker 容器編排設定
├── requirements.txt      # Python 依賴套件
└── README.md             # 專案說明文件
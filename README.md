# Tour-Agent 的初步實作

這是一個專為 **OpenWebUI** 設計的後端擴充專案，提供增強的 Function Calling（工具調用）能力。本專案遵循 **12-Factor App** 原則構建，確保配置與代碼分離，並透過 Docker 容器化部署。

主要包含天氣查詢與旅遊推薦功能，並針對 LLM 的 Prompt 進行了優化，以確保輸出的格式與內容最符合用戶需求。

## 目前主要功能 (Features)

### 1. 天氣查詢 (Weather Tool)
- **功能**：獲取指定城市的即時天氣數據。
- **工具名稱**：`get_weather`

### 2. 旅遊規劃與 HTML 匯出 (Itinerary & Export Tool)
- **行程規劃**：提供客製化的景點、餐廳與住宿推薦。
- **HTML 匯出功能**：將規劃好的行程轉換為精美的 HTML 檔案，支援點擊下載，方便使用者離線查看。
- **工具名稱**：`get_tourist_spot`, `get_restaurant`, `get_hotel`, `form_itny_link`

### 3. 安全與架構 (Architecture)
- **12-Factor App**：環境變數 (`.env`) 與程式碼完全分離。
- **乾淨架構 (Clean Architecture)**：引入 Service Layer 與 Template Engine (Jinja2)，將業務邏輯與視圖層分離，具備高度擴充性。
- **Dockerized**：提供 `docker-compose` 支援，一鍵啟動。
- **SQLite 本地資料庫**：設置本地快取，減少重複 API 請求，提升查詢效率並確保回答精準度。

---

## 📂 專案結構 (Project Structure)

```text
.
├── app/                  # 主要應用程式邏輯 (Python)
│   ├── core/
│   │   ├── config.py     # 核心資料，包括 API KEY 管理
│   │   ├── database.py   # 處理本地資料庫 (SQLite)
│   │   └── schemas.py    # 資料契約 (Pydantic Models)
│   ├── outputs/          # 輸出的 HTML 位置
│   ├── services/         # 業務邏輯 (HTML 渲染處理)
│   ├── templates/        # HTML 格式模板 (去中心化)
│   ├── tools/            # 所有 Tools 管理
│   ├── utils/            # 所有輔助 Tools 的工具
│   └── main.py           # 主程式
├── openwebui_config/     # OpenWebUI 專用的工具設定檔與 Prompt 模板
├── .env.example          # 環境變數範例檔
├── .gitignore            # Git 忽略清單
├── docker-compose.yml    # Docker 容器編排設定
├── requirements.txt      # Python 依賴套件
└── README.md             # 專案說明文件
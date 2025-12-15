def convert_format(city_input: str) -> str:
    if not city_input:
        return ""
    key = city_input.strip().lower()
    mapping = {
        "台北": "Taipei", "臺北": "Taipei", "台北市": "Taipei", "臺北市": "Taipei", "taipei": "Taipei",
        "新北": "NewTaipei", "新北市": "NewTaipei", "newtaipei": "NewTaipei",
        "桃園": "Taoyuan", "桃園市": "Taoyuan", "taoyuan": "Taoyuan",
        "台中": "Taichung", "臺中": "Taichung", "台中市": "Taichung", "臺中市": "Taichung", "taichung": "Taichung",
        "台南": "Tainan", "臺南": "Tainan", "台南市": "Tainan", "臺南市": "Tainan", "tainan": "Tainan",
        "高雄": "Kaohsiung", "高雄市": "Kaohsiung", "kaohsiung": "Kaohsiung",
        "基隆": "Keelung", "基隆市": "Keelung", "keelung": "Keelung",
        "新竹": "Hsinchu", "新竹市": "Hsinchu", "hsinchu": "Hsinchu",
        "嘉義": "Chiayi", "嘉義市": "Chiayi", "chiayi": "Chiayi",
        "新竹縣": "HsinchuCounty", "hsinchucounty": "HsinchuCounty",
        "苗栗": "MiaoliCounty", "苗栗縣": "MiaoliCounty", "miaoli": "MiaoliCounty", "miaolicounty": "MiaoliCounty",
        "彰化": "ChanghuaCounty", "彰化縣": "ChanghuaCounty", "changhua": "ChanghuaCounty", "changhuacounty": "ChanghuaCounty",
        "南投": "NantouCounty", "南投縣": "NantouCounty", "nantou": "NantouCounty", "nantoucounty": "NantouCounty",
        "雲林": "YunlinCounty", "雲林縣": "YunlinCounty", "yunlin": "YunlinCounty", "yunlincounty": "YunlinCounty",
        "嘉義縣": "ChiayiCounty", "chiayicounty": "ChiayiCounty",
        "屏東": "PingtungCounty", "屏東縣": "PingtungCounty", "pingtung": "PingtungCounty", "pingtungcounty": "PingtungCounty",
        "宜蘭": "YilanCounty", "宜蘭縣": "YilanCounty", "yilan": "YilanCounty", "yilancounty": "YilanCounty",
        "花蓮": "HualienCounty", "花蓮縣": "HualienCounty", "hualien": "HualienCounty", "hualiencounty": "HualienCounty",
        "台東": "TaitungCounty", "臺東": "TaitungCounty", "台東縣": "TaitungCounty", "臺東縣": "TaitungCounty", "taitung": "TaitungCounty", "taitungcounty": "TaitungCounty",
        "澎湖": "PenghuCounty", "澎湖縣": "PenghuCounty", "penghu": "PenghuCounty",
        "金門": "KinmenCounty", "金門縣": "KinmenCounty", "kinmen": "KinmenCounty",
        "連江": "LienchiangCounty", "連江縣": "LienchiangCounty", "馬祖": "LienchiangCounty", "matsu": "LienchiangCounty"
    }

    return mapping.get(key, city_input)
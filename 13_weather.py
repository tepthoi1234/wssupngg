import streamlit as st
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# =========================================================
# CẤU HÌNH STREAMLIT
# =========================================================

st.set_page_config(
    page_title="Thu thập dữ liệu thời tiết",
    page_icon="🌤️",
    layout="wide"
)

st.title("🌤️ THU THẬP DỮ LIỆU THỜI TIẾT")

st.write(
    "Thu thập dữ liệu thời tiết từ AccuWeather "
    "của 5 thành phố lớn tại Việt Nam."
)


# =========================================================
# DANH SÁCH THÀNH PHỐ
# =========================================================

cities = {
    "Hà Nội":
        "https://www.accuweather.com/en/vn/hanoi/353412/current-weather/353412",

    "Hồ Chí Minh":
        "https://www.accuweather.com/en/vn/ho-chi-minh-city/353981/current-weather/353981",

    "Hải Phòng":
        "https://www.accuweather.com/en/vn/haiphong/353511/current-weather/353511",

    "Đà Nẵng":
        "https://www.accuweather.com/en/vn/da-nang/352954/current-weather/352954",

    "Cần Thơ":
        "https://www.accuweather.com/en/vn/can-tho/352508/current-weather/352508"
}


# =========================================================
# HÀM LẤY DỮ LIỆU
# =========================================================

def get_weather_data(city, url):

    options = Options()

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    options.add_argument(
        "user-agent=Mozilla/5.0"
    )

    driver = webdriver.Chrome(
        options=options
    )

    try:

        # ==============================
        # MỞ TRANG
        # ==============================

        driver.get(url)

        time.sleep(5)


        # ==============================
        # NHIỆT ĐỘ
        # ==============================

        try:

            temperature = driver.find_element(
                By.CSS_SELECTOR,
                ".display-temp"
            ).text

        except:

            temperature = "Không lấy được"


        # ==============================
        # THỜI TIẾT
        # ==============================

        try:

            weather = driver.find_element(
                By.CSS_SELECTOR,
                ".phrase"
            ).text

        except:

            weather = "Không lấy được"


        # ==============================
        # ĐỘ ẨM
        # ==============================

        try:

            humidity = driver.find_element(
                By.XPATH,
                "//*[contains(text(),'Humidity')]/following-sibling::*[1]"
            ).text

        except:

            humidity = "Không lấy được"


        # ==============================
        # GIÓ
        # ==============================

        try:

            wind = driver.find_element(
                By.XPATH,
                "//*[contains(text(),'Wind')]/following-sibling::*[1]"
            ).text

        except:

            wind = "Không lấy được"


        # ==============================
        # CHẤT LƯỢNG KHÔNG KHÍ
        # ==============================

        try:

            air_quality = driver.find_element(
                By.XPATH,
                "//*[contains(text(),'Air Quality')]/following::*[1]"
            ).text

        except:

            air_quality = "Không lấy được"


        # ==============================
        # TRẢ KẾT QUẢ
        # ==============================

        return {
            "Thành phố": city,
            "Thời tiết": weather,
            "Nhiệt độ": temperature,
            "Độ ẩm": humidity,
            "Tốc độ gió": wind,
            "Chất lượng không khí": air_quality
        }


    except Exception as e:

        print(
            f"Lỗi {city}: {e}"
        )

        return {
            "Thành phố": city,
            "Thời tiết": "Lỗi",
            "Nhiệt độ": "Lỗi",
            "Độ ẩm": "Lỗi",
            "Tốc độ gió": "Lỗi",
            "Chất lượng không khí": "Lỗi"
        }


    finally:

        driver.quit()


# =========================================================
# NÚT THU THẬP
# =========================================================

if st.button(
    "🚀 Bắt đầu thu thập dữ liệu",
    use_container_width=True
):

    data = []

    progress = st.progress(0)

    status = st.empty()

    total = len(cities)

    # =====================================================
    # THU THẬP 5 THÀNH PHỐ
    # =====================================================

    for index, (city, url) in enumerate(
        cities.items()
    ):

        status.write(
            f"🔎 Đang thu thập: **{city}**"
        )

        result = get_weather_data(
            city,
            url
        )

        data.append(result)

        progress.progress(
            (index + 1) / total
        )


    # =====================================================
    # TẠO DATAFRAME
    # =====================================================

    df = pd.DataFrame(data)


    # =====================================================
    # B4: ĐÁNH STT TỪ 1
    # =====================================================

    df.insert(
        0,
        "STT",
        range(1, len(df) + 1)
    )


    # =====================================================
    # B1: LƯU FILE CSV
    # =====================================================

    df.to_csv(
        "weather.csv",
        index=False,
        encoding="utf-8-sig"
    )


    # Lưu vào session
    st.session_state.weather_data = df


    status.success(
        "✅ Đã thu thập dữ liệu thành công!"
    )

    st.rerun()


# =========================================================
# B5: HIỂN THỊ BỘ DỮ LIỆU
# =========================================================

if "weather_data" in st.session_state:

    df = st.session_state.weather_data

    st.divider()

    st.subheader(
        "📊 B5. Bộ dữ liệu thời tiết"
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


    # =====================================================
    # B6: THÔNG TIN BỘ DỮ LIỆU
    # =====================================================

    st.subheader(
        "📋 B6. Thông tin bộ dữ liệu"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Số dòng",
            df.shape[0]
        )

    with col2:

        st.metric(
            "Số cột",
            df.shape[1]
        )

    with col3:

        st.metric(
            "Số thành phố",
            len(df)
        )


    st.write("### Các trường dữ liệu")

    for column in df.columns:

        st.write(
            f"- **{column}**"
        )


    # =====================================================
    # XEM FILE CSV
    # =====================================================

    st.subheader(
        "📁 File CSV"
    )

    csv_data = df.to_csv(
        index=False,
        encoding="utf-8-sig"
    )

    st.download_button(
        label="📥 Tải weather.csv",
        data=csv_data,
        file_name="weather.csv",
        mime="text/csv"
    )
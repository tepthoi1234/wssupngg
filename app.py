import streamlit as st
st.set_page_config(page_title="Supper App", layout="wide")
st.markdown("""
<style>
    .main {
        background-color: #f7f7f7;
    }

    .title {
        text-align: center;
        color: #b8860b;
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .price-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border: 1px solid #eeeeee;
    }

    .price-title {
        color: #777;
        font-size: 15px;
        margin-bottom: 8px;
    }

    .price {
        color: #b8860b;
        font-size: 28px;
        font-weight: bold;
    }

    .update {
        color: #777;
        font-size: 13px;
        margin-top: 8px;
    }

    .section-title {
        color: #333;
        font-size: 22px;
        font-weight: 600;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 45px;
        font-size: 16px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)
st.title("🚀 Super App: Sức khỏe & Giải trí ")

st.markdown(""" 
### 🤚 Chào mừng bạn !
ứng dụng gồm:
- Theo dõi sức khỏe
- 📰Đọc tin tức
- 🎮Giải trí game
- Nghe nhạc
- ứng dụng sức khỏe nâng cao
Chức năng ở phần sidebar bên trái 
""")
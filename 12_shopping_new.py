import streamlit as st


# ==================================================
# CẤU HÌNH
# ==================================================

st.set_page_config(
    page_title="Vương quốc mô hình",
    page_icon="✨"
)


# ==================================================
# CLASS MODEL
# ==================================================

class Model:

    # Constructor
    def __init__(self, name, code, image):
        self.name = name
        self.code = code
        self.image = image

    # Phương thức hiển thị mô hình
    def show(self):
        st.image(
            self.image,
            caption=f"{self.name} - Mã mô hình: {self.code}"
        )


# ==================================================
# TẠO CÁC OBJECT
# ==================================================

# -------- Dragon Ball --------

goku = Model(
    "Goku Ultra Instinct",
    "001",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThzdVzFl0LSNZUQtIl9VEKa4kvYcoW9lzuZ19jMULFCA&s=10"
)

vegeta = Model(
    "Vegeta Super Saiyen",
    "002",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTHjDxbkjHukXxN1oSxGAaYpS47RmjA8OtTtHwfttHVQ&s=10"
)

picolo = Model(
    "Picolo",
    "003",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4rCayThrM0tTFp5A23Y3H_25Qygi6ipMGtDiQLap-Aw8EXUEm6VKUCfs&s=10"
)


# -------- Naruto --------

naruto = Model(
    "Uzumaki Naruto",
    "001",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTilw3RVq-biylDlRSjtroR1ZmH7nHhEzqy23HihxlXBw&s=10"
)

sasuke = Model(
    "Uchiha Sasuke",
    "002",
    "https://upload.wikimedia.org/wikipedia/vi/4/42/SasukeKishimoto.jpg"
)

kakashi = Model(
    "Hatake Kakashi",
    "003",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxhzKR1ICETzwcfOxevXCyAc6JRJmeRG-ceKTOuJa5caLAP_wK9MM3fJ8&s=10"
)


# -------- One Piece --------

luffy = Model(
    "Monkey D. Luffy",
    "001",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEwqmFvs7UmwADjH7w0iEu1wP32yILJ14k7MLJFOk7Mw&s=10"
)

zoro = Model(
    "Roronoa Zoro",
    "002",
    "https://upload.wikimedia.org/wikipedia/vi/a/a4/Roronoa_Zoro.jpg"
)

vinsmoke = Model(
    "Vinsmoke",
    "003",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG094c7KLIqjiFkmJRR29fOEliGV0XFPmNJYTcJwtK1wuS2J6D4Kj62n_2&s=10"
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("Vương quốc mô hình")

    st.header(
        "Chào mừng bạn đến với vương quốc mô hình"
    )

    st.image(
        "https://www.ffcollectibles.com.au/cdn/shop/products/G5STUDIOHIGHENDCUSTOMSERIESTHELIFEOFNARUTOUZUMAKI_2.jpg?v=1689176734&width=823"
    )

    st.write(
        """
        Chúng tôi chuyên bán các mô hình nhân vật
        hoạt hình chất lượng.

        Luôn cập nhật và đa dạng sản phẩm,
        cam kết sự hài lòng của khách hàng
        với dịch vụ chuyên nghiệp.

        Hãy đến và khám phá thế giới mô hình
        tại Vương quốc mô hình.
        """
    )

    st.write("🏠 Địa chỉ cửa hàng")

    st.write("📞 Điện thoại liên hệ")


# ==================================================
# TRANG CHÍNH
# ==================================================

st.title("Vương quốc mô hình")


# ==================================================
# CHỌN THỂ LOẠI
# ==================================================

col1, col2, col3 = st.columns(3)


with col1:

    b1 = st.button(
        "Dragon Ball",
        use_container_width=True
    )


with col2:

    b2 = st.button(
        "Naruto",
        use_container_width=True
    )


with col3:

    b3 = st.button(
        "One Piece",
        use_container_width=True
    )


# ==================================================
# DRAGON BALL
# ==================================================

if b1:

    st.header("Danh sách mô hình Dragon Ball")

    col4, col5, col6 = st.columns(3)

    with col4:
        goku.show()

    with col5:
        vegeta.show()

    with col6:
        picolo.show()


# ==================================================
# NARUTO
# ==================================================

if b2:

    st.header("Danh sách mô hình Naruto")

    col4, col5, col6 = st.columns(3)

    with col4:
        naruto.show()

    with col5:
        sasuke.show()

    with col6:
        kakashi.show()


# ==================================================
# ONE PIECE
# ==================================================

if b3:

    st.header("Danh sách mô hình One Piece")

    col4, col5, col6 = st.columns(3)

    with col4:
        luffy.show()

    with col5:
        zoro.show()

    with col6:
        vinsmoke.show()
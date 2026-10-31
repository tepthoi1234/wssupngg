import streamlit as st
st.set_page_config(page_title="Vương quốc mô hình", page_icon=":sparkles")

with st.sidebar:
    st.title("Vương quốc mô hình")
    st.header("Chào mừng bạn đến với vương quốc mô hình")
    st.image("https://www.ffcollectibles.com.au/cdn/shop/products/G5STUDIOHIGHENDCUSTOMSERIESTHELIFEOFNARUTOUZUMAKI_2.jpg?v=1689176734&width=823")
    st.write("""Chúng tôi chuyên bán các mô hình nhân vật hoạt hình chất lương. Luôn cập nhật và đa dạng sản phẩm
    cam kết sự hài lòng của khách hàng với dịch vụ chuyên nghiệp. Hãy đến và khám phá thế giới mô hình
    tại Vương quốc mô hình
    """)
    st.write(":house: Địa chỉ cửa hàng")
    st.write(":Phone: Điện thoại liên hệ")

st.title("Vương quốc mô hình")
col1, col2, col3 = st.columns(3)
with col1:
    b1 = st.button("Dragon Ball")
with col2:
    b2 = st.button("Naruto")
with col3:
    b3 = st.button("One Piece")

if b1:
    st.header("Danh sách mô hình dragon Ball")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThzdVzFl0LSNZUQtIl9VEKa4kvYcoW9lzuZ19jMULFCA&s=10", 
                 caption="Goku ultra Instinct - Mã mố: 001")
    with col5:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTHjDxbkjHukXxN1oSxGAaYpS47RmjA8OtTtHwfttHVQ&s=10", 
                 caption="Vegeta super saiyen - Mã mố: 002")
    with col6:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4rCayThrM0tTFp5A23Y3H_25Qygi6ipMGtDiQLap-Aw8EXUEm6VKUCfs&s=10", 
                 caption="Picolo - Mã mố: 003")
if b2:
    st.header("Danh sách mô hình Naruto")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTilw3RVq-biylDlRSjtroR1ZmH7nHhEzqy23HihxlXBw&s=10", 
                 caption="Uzumaki - Mã mố: 001")
    with col5:
        st.image("https://upload.wikimedia.org/wikipedia/vi/4/42/SasukeKishimoto.jpg?utm_source=vi.wikipedia.org&utm_campaign=index&utm_content=original", 
                 caption="Uchiha Sasuke - Mã mố: 002")
    with col6:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxhzKR1ICETzwcfOxevXCyAc6JRJmeRG-ceKTOuJa5caLAP_wK9MM3fJ8&s=10", 
                 caption="Hatake kakashi - Mã mố: 003")
if b3:
    st.header("Danh sách mô hình One Piece")
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEwqmFvs7UmwADjH7w0iEu1wP32yILJ14k7MLJFOk7Mw&s=10", 
                 caption="Monkey D.luffy - Mã mố: 001")
    with col5:
        st.image("https://upload.wikimedia.org/wikipedia/vi/a/a4/Roronoa_Zoro.jpg?utm_source=vi.wikipedia.org&utm_campaign=index&utm_content=original", 
                 caption="Roronoa Zoro - Mã mố: 002")
    with col6:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG094c7KLIqjiFkmJRR29fOEliGV0XFPmNJYTcJwtK1wuS2J6D4Kj62n_2&s=10", 
                 caption="Vinsmoke sanji- Mã mố: 003")
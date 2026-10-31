import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import date
# =====================================================
# CẤU HÌNH WEBSITE
# =====================================================
st.set_page_config(
    page_title="Quản lý chi tiêu cá nhân - OOP",
    page_icon="💰",
    layout="wide"
)
st.title("💰 Quản lý chi tiêu cá nhân")
st.markdown("Ứng dụng quản lý thu - chi sử dụng lập trình hướng đối tượng.")
# =====================================================
# CLASS EXPENSE MANAGER
# =====================================================
class ExpenseManager:
    def __init__(self):
        if "transactions" not in st.session_state:
            st.session_state.transactions = []
    # =================================================
    # THÊM GIAO DỊCH
    # =================================================
    def add_transaction(
        self,
        transaction_date,
        transaction_type,
        category,
        amount,
        note
    ):
        transaction = {
            "Ngày": str(transaction_date),
            "Loại": transaction_type,
            "Danh mục": category,
            "Số tiền": amount,
            "Ghi chú": note
        }
        st.session_state.transactions.append(transaction)
    # =================================================
    # XÓA GIAO DỊCH
    # =================================================
    def delete_transaction(self, index):
        st.session_state.transactions.pop(index)
    # =================================================
    # LẤY DATAFRAME
    # =================================================
    def get_dataframe(self):
        columns = [
            "Ngày",
            "Loại",
            "Danh mục",
            "Số tiền",
            "Ghi chú"
        ]
        if len(st.session_state.transactions) == 0:
            return pd.DataFrame(columns=columns)
        return pd.DataFrame(
            st.session_state.transactions
        )
    # =================================================
    # TỔNG SỐ GIAO DỊCH
    # =================================================
    def total(self):
        return len(
            st.session_state.transactions
        )
    # =================================================
    # TỔNG THU
    # =================================================
    def total_income(self):
        df = self.get_dataframe()
        if len(df) == 0:
            return 0
        return df[
            df["Loại"] == "Thu"
        ]["Số tiền"].sum()
    # =================================================
    # TỔNG CHI
    # =================================================
    def total_expense(self):
        df = self.get_dataframe()
        if len(df) == 0:
            return 0
        return df[
            df["Loại"] == "Chi"
        ]["Số tiền"].sum()
    # =================================================
    # SỐ DƯ
    # =================================================
    def balance(self):
        return (
            self.total_income()
            -
            self.total_expense()
        )
    # =================================================
    # LỌC DỮ LIỆU
    # =================================================
    def filter_data(
        self,
        transaction_type="Tất cả",
        category="Tất cả"
    ):
        df = self.get_dataframe()
        if transaction_type != "Tất cả":
            df = df[
                df["Loại"] == transaction_type
            ]
        if category != "Tất cả":
            df = df[
                df["Danh mục"] == category
            ]
        return df

    # =================================================
    # XUẤT EXCEL
    # =================================================

    def export_excel(self, data):
        output = BytesIO()
        with pd.ExcelWriter(
            output,
            engine="openpyxl"
        ) as writer:
            # Sheet giao dịch
            data.to_excel(
                writer,
                sheet_name="Giao dich",
                index=False
            )
            # Tính thống kê
            income = data[
                data["Loại"] == "Thu"
            ]["Số tiền"].sum()

            expense = data[
                data["Loại"] == "Chi"
            ]["Số tiền"].sum()

            balance = income - expense

            summary = pd.DataFrame({

                "Chỉ tiêu": [

                    "Tổng giao dịch",

                    "Tổng thu",

                    "Tổng chi",

                    "Số dư"
                ],

                "Giá trị": [

                    len(data),

                    income,

                    expense,

                    balance
                ]
            })

            # Sheet thống kê

            summary.to_excel(
                writer,
                sheet_name="Thong ke",
                index=False
            )

        return output.getvalue()


# =====================================================
# TẠO ĐỐI TƯỢNG
# =====================================================

manager = ExpenseManager()


# =====================================================
# SIDEBAR - THÊM GIAO DỊCH
# =====================================================

st.sidebar.header("➕ Thêm giao dịch")


transaction_date = st.sidebar.date_input(
    "Ngày",
    value=date.today()
)


transaction_type = st.sidebar.selectbox(
    "Loại",
    [
        "Thu",
        "Chi"
    ]
)


category = st.sidebar.selectbox(
    "Danh mục",
    [
        "Ăn uống",
        "Đi lại",
        "Lương",
        "Mua sắm",
        "Giải trí",
        "Tiền điện",
        "Tiền nước",
        "Học tập",
        "Y tế",
        "Khác"
    ]
)


amount = st.sidebar.number_input(
    "Số tiền",
    min_value=1000,
    step=1000
)


note = st.sidebar.text_input(
    "Ghi chú"
)


# =====================================================
# BUTTON LƯU
# =====================================================

if st.sidebar.button(
    "💾 Lưu giao dịch",
    use_container_width=True
):

    if amount <= 0:

        st.sidebar.warning(
            "Số tiền phải lớn hơn 0."
        )

    else:

        manager.add_transaction(
            transaction_date,
            transaction_type,
            category,
            amount,
            note
        )

        st.sidebar.success(
            "Đã lưu giao dịch!"
        )

        st.rerun()


# =====================================================
# LẤY DATA
# =====================================================

df = manager.get_dataframe()


# =====================================================
# DANH SÁCH GIAO DỊCH
# =====================================================

st.header("📋 Danh sách giao dịch")


if len(df) == 0:

    st.info(
        "Chưa có giao dịch nào."
    )

else:

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# XÓA GIAO DỊCH
# =====================================================

st.header("🗑️ Xóa giao dịch")


if len(df) > 0:

    delete_index = st.selectbox(

        "Chọn giao dịch muốn xóa",

        options=df.index,

        format_func=lambda x:
        f"{x + 1}. "
        f"{df.loc[x, 'Ngày']} - "
        f"{df.loc[x, 'Danh mục']} - "
        f"{df.loc[x, 'Số tiền']:,.0f} VNĐ"
    )


    if st.button("🗑️ Xóa giao dịch"):

        manager.delete_transaction(
            delete_index
        )

        st.success(
            "Đã xóa giao dịch."
        )

        st.rerun()


# =====================================================
# BỘ LỌC
# =====================================================

st.header("🔍 Bộ lọc")


col1, col2 = st.columns(2)


with col1:

    filter_type = st.selectbox(

        "Loại giao dịch",

        [
            "Tất cả",
            "Thu",
            "Chi"
        ]
    )


with col2:

    categories = [
        "Tất cả"
    ]

    if len(df) > 0:

        categories += list(
            df["Danh mục"].unique()
        )

    filter_category = st.selectbox(

        "Danh mục",

        categories
    )


# =====================================================
# DỮ LIỆU SAU KHI LỌC
# =====================================================

filtered_df = manager.filter_data(

    transaction_type=filter_type,

    category=filter_category
)


st.subheader("📋 Dữ liệu sau khi lọc")


st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


# =====================================================
# THỐNG KÊ
# =====================================================

st.header("📊 Thống kê")


income = filtered_df[
    filtered_df["Loại"] == "Thu"
]["Số tiền"].sum()


expense = filtered_df[
    filtered_df["Loại"] == "Chi"
]["Số tiền"].sum()


balance = income - expense


c1, c2, c3, c4 = st.columns(4)


c1.metric(
    "💵 Tổng thu",
    f"{income:,.0f} VNĐ"
)


c2.metric(
    "💸 Tổng chi",
    f"{expense:,.0f} VNĐ"
)


c3.metric(
    "💰 Số dư",
    f"{balance:,.0f} VNĐ"
)


c4.metric(
    "📝 Giao dịch",
    len(filtered_df)
)


# =====================================================
# BIỂU ĐỒ CHI TIÊU THEO DANH MỤC
# =====================================================

st.header("📈 Chi tiêu theo danh mục")


expense_df = filtered_df[
    filtered_df["Loại"] == "Chi"
]


if len(expense_df) > 0:

    category_chart = (
        expense_df
        .groupby("Danh mục")["Số tiền"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(
        category_chart
    )

else:

    st.info(
        "Chưa có dữ liệu chi tiêu."
    )


# =====================================================
# CHI TIÊU THEO NGÀY
# =====================================================

st.header("📅 Chi tiêu theo ngày")


if len(expense_df) > 0:

    daily_chart = (
        expense_df
        .groupby("Ngày")["Số tiền"]
        .sum()
    )

    st.line_chart(
        daily_chart
    )

else:

    st.info(
        "Chưa có dữ liệu."
    )


# =====================================================
# TỶ LỆ CHI TIÊU
# =====================================================

st.header("🎯 Tỷ lệ chi tiêu")


if income > 0:

    expense_ratio = expense / income

    st.progress(
        min(expense_ratio, 1.0)
    )

    st.write(
        f"Bạn đã chi "
        f"**{expense_ratio * 100:.1f}%** "
        f"so với tổng thu."
    )

else:

    st.info(
        "Chưa có khoản thu để tính tỷ lệ."
    )


# =====================================================
# XUẤT EXCEL
# =====================================================

st.header("📥 Xuất Excel")


export_option = st.radio(

    "Dữ liệu muốn xuất",

    [
        "Toàn bộ dữ liệu",
        "Dữ liệu đã lọc"
    ],

    horizontal=True
)


if export_option == "Toàn bộ dữ liệu":

    export_df = manager.get_dataframe()

else:

    export_df = filtered_df


excel_data = manager.export_excel(
    export_df
)


st.download_button(

    label="📄 Tải file Excel",

    data=excel_data,

    file_name="quan_ly_chi_tieu.xlsx",

    mime=(
        "application/vnd.openxmlformats-officedocument."
        "spreadsheetml.sheet"
    ),

    use_container_width=True
)
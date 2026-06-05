import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="KimiaKu",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 KimiaKu")
st.subheader("Tabel Periodik & Kalkulator Pengenceran")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Kalkulator Pengenceran", "Tabel Periodik"]
)

# =========================
# KALKULATOR PENGENCERAN
# =========================
if menu == "Kalkulator Pengenceran":

    st.header("Kalkulator Pengenceran")
    st.latex(r"M_1V_1=M_2V_2")

    col1, col2 = st.columns(2)

    with col1:
        M1 = st.number_input(
            "M1 (Molaritas Awal)",
            min_value=0.0,
            format="%.4f"
        )

        V1 = st.number_input(
            "V1 (Volume Awal mL)",
            min_value=0.0,
            format="%.4f"
        )

    with col2:
        M2 = st.number_input(
            "M2 (Molaritas Akhir)",
            min_value=0.0,
            format="%.4f"
        )

    if st.button("Hitung V2"):

        if M2 == 0:
            st.error("M2 tidak boleh nol")
        else:
            V2 = (M1 * V1) / M2

            st.success(
                f"Volume akhir (V₂) = {V2:.2f} mL"
            )

# =========================
# TABEL PERIODIK
# =========================
elif menu == "Tabel Periodik":

    st.header("⚛️ Tabel Periodik Unsur")

    data = {
        "Nomor Atom": [1,2,3,4,5,6,7,8,9,10],
        "Simbol": ["H","He","Li","Be","B","C","N","O","F","Ne"],
        "Nama Unsur": [
            "Hidrogen",
            "Helium",
            "Litium",
            "Berilium",
            "Boron",
            "Karbon",
            "Nitrogen",
            "Oksigen",
            "Fluorin",
            "Neon"
        ]
    }

    df = pd.DataFrame(data)

    cari = st.text_input(
        "Cari simbol atau nama unsur"
    )

    if cari:
        df = df[
            df["Simbol"].str.contains(cari, case=False)
            |
            df["Nama Unsur"].str.contains(cari, case=False)
        ]

    st.dataframe(
        df,
        use_container_width=True
    )

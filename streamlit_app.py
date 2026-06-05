import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PeriodicCalc",
    page_icon="⚗️",
    layout="wide"
)

st.title("⚗️ PeriodicCalc")

# Data unsur dasar untuk contoh
data = [
    [1, "H", "Hidrogen", 1.008],
    [6, "C", "Karbon", 12.011],
    [7, "N", "Nitrogen", 14.007],
    [8, "O", "Oksigen", 15.999],
    [11, "Na", "Natrium", 22.990],
    [17, "Cl", "Klorin", 35.45]
]

df = pd.DataFrame(
    data,
    columns=["Nomor Atom", "Simbol", "Nama", "Massa Atom"]
)

# Pilih unsur
st.header("Informasi Unsur")

pilih = st.selectbox(
    "Pilih Unsur",
    df["Simbol"]
)

unsur = df[df["Simbol"] == pilih].iloc[0]

st.write(f"*Nama:* {unsur['Nama']}")
st.write(f"*Nomor Atom:* {unsur['Nomor Atom']}")
st.write(f"*Massa Atom:* {unsur['Massa Atom']}")

st.divider()

# Tabel periodik sederhana
st.header("Tabel Periodik")

baris1 = st.columns(18)
baris1[0].button("H")
baris1[17].button("He")

baris2 = st.columns(18)
baris2[0].button("Li")
baris2[1].button("Be")
baris2[12].button("B")
baris2[13].button("C")
baris2[14].button("N")
baris2[15].button("O")
baris2[16].button("F")
baris2[17].button("Ne")

baris3 = st.columns(18)
baris3[0].button("Na")
baris3[1].button("Mg")
baris3[12].button("Al")
baris3[13].button("Si")
baris3[14].button("P")
baris3[15].button("S")
baris3[16].button("Cl")
baris3[17].button("Ar")


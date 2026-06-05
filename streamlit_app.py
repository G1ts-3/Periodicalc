import streamlit as st
import pandas as pd
import re

st.set_page_config(
    page_title="PeriodicCalc",
    page_icon="⚗️",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================
df = pd.read_csv("data/periodic_table.csv")

Ar = dict(zip(df["simbol"], df["massa_atom"]))

# ==========================
# JUDUL
# ==========================
st.title("⚗️ PeriodicCalc")
st.caption("Tabel Periodik & Kalkulator Kimia")

# ==========================
# PENCARIAN UNSUR
# ==========================
st.header("⚛️ Informasi Unsur")

simbol = st.selectbox(
    "Pilih Unsur",
    df["simbol"]
)

unsur = df[df["simbol"] == simbol].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.metric("Nomor Atom", unsur["nomor_atom"])

with col2:
    st.metric("Massa Atom", unsur["massa_atom"])

st.write("*Nama Unsur:*", unsur["nama"])

# ==========================
# TABEL PERIODIK
# ==========================
st.divider()
st.header("📋 Tabel Periodik")

periodik = [
["H","","","","","","","","","","","","","","","","","He"],
["Li","Be","","","","","","","","","","","B","C","N","O","F","Ne"],
["Na","Mg","","","","","","","","","","","Al","Si","P","S","Cl","Ar"],
["K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr"],
["Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe"],
["Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu",""],
["Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr",""]
]

for baris in periodik:
    cols = st.columns(18)

    for i, item in enumerate(baris):

        if item != "":
            if cols[i].button(item, use_container_width=True):
                hasil = df[df["simbol"] == item]

                if not hasil.empty:
                    st.session_state["unsur"] = item
        else:
            cols[i].write("")

if "unsur" in st.session_state:

    hasil = df[df["simbol"] == st.session_state["unsur"]].iloc[0]

    st.success(
        f"{hasil['nama']} | "
        f"Z = {hasil['nomor_atom']} | "
        f"Ar = {hasil['massa_atom']}"
    )

# ==========================
# MASSA MOLAR
# ==========================
st.divider()
st.header("⚖️ Kalkulator Massa Molar")

def hitung_mr(rumus):

    total = 0

    token = re.findall(
        r'([A-Z][a-z]?)(\d*)',
        rumus
    )

    for unsur, jumlah in token:

        jumlah = int(jumlah) if jumlah else 1

        if unsur in Ar:
            total += Ar[unsur] * jumlah

    return total

rumus_mr = st.text_input(
    "Masukkan Rumus Kimia",
    "NaCl"
)

if st.button("Hitung Massa Molar"):

    mr = hitung_mr(rumus_mr)

    st.success(
        f"Massa Molar = {mr:.3f} g/mol"
    )

# ==========================
# PEMBUATAN LARUTAN
# ==========================
st.divider()
st.header("🧪 Pembuatan Larutan")

rumus = st.text_input(
    "Rumus Kimia",
    "NaCl"
)

molaritas = st.number_input(
    "Molaritas (M)",
    min_value=0.0,
    value=0.1,
    step=0.1
)

volume = st.number_input(
    "Volume (mL)",
    min_value=1.0,
    value=100.0
)

if st.button("Hitung Massa Zat"):

    mr = hitung_mr(rumus)

    massa = mr * molaritas * (volume / 1000)

    st.success(
        f"Mr = {mr:.3f} g/mol"
    )

    st.success(
        f"Massa yang harus ditimbang = {massa:.4f} gram"
    )

# ==========================
# DATA UNSUR
# ==========================
st.divider()

with st.expander("Lihat Data 118 Unsur"):
    st.dataframe(
        df,
        use_container_width=True
    )

import streamlit as st
from utils.tabel_periodik_118 import elemen_periodik, Ar_tiap_unsur
def tampilkan_tabel_periodik(filter_golongan=None):
 for baris in elemen_periodik:
 kolom = st.columns(len(baris))
 for i, elemen in enumerate(baris):
 simbol = elemen.get("simbol", "")
 golongan = elemen.get("golongan", "lainnya")
 if simbol and (filter_golongan is None or golongan == filter_golongan):
 Ar = Ar_tiap_unsur.get(simbol, "")
 label = f"{simbol}"
 tooltip = f"{simbol} (Ar = {Ar})" if Ar else simbol
 if kolom[i].button(label, help=tooltip, key=f"{simbol}_{i}", use_container_width=True):
 if "selected_elements" not in st.session_state:
 st.session_state.selected_elements = []
 if len(st.session_state.selected_elements) < 2 and simbol not in 
st.session_state.selected_elements:
 st.session_state.selected_elements.append(simbol)
 else:
 kolom[i].markdown(" ")
massa_atom = {
 "H": 1.01, "He": 4.00, "Li": 6.94, "Be": 9.01, "B": 10.81, "C": 12.01, "N": 14.01, "O": 16.00, "F": 19.00, 
"Ne": 20.18,
 "Na": 22.99, "Mg": 24.31, "Al": 26.98, "Si": 28.09, "P": 30.97, "S": 32.07, "Cl": 35.45, "Ar": 39.95,
 "K": 39.10, "Ca": 40.08, "Sc": 44.96, "Ti": 47.87, "V": 50.94, "Cr": 52.00, "Mn": 54.94, "Fe": 55.85,
 "Co": 58.93, "Ni": 58.69, "Cu": 63.55, "Zn": 65.38, "Ga": 69.72, "Ge": 72.63, "As": 74.92, "Se": 78.97,
 "Br": 79.90, "Kr": 83.80, "Rb": 85.47, "Sr": 87.62, "Y": 88.91, "Zr": 91.22, "Nb": 92.91, "Mo": 95.95,
 "Tc": 98.00, "Ru": 101.1, "Rh": 102.9, "Pd": 106.4, "Ag": 107.9, "Cd": 112.4, "In": 114.8, "Sn": 118.7,
 "Sb": 121.8, "Te": 127.6, "I": 126.9, "Xe": 131.3, "Cs": 132.9, "Ba": 137.3, "La": 138.9, "Ce": 140.1,
 "Pr": 140.9, "Nd": 144.2, "Pm": 145.0, "Sm": 150.4, "Eu": 152.0, "Gd": 157.3, "Tb": 158.9, "Dy": 162.5,
 "Ho": 164.9, "Er": 167.3, "Tm": 168.9, "Yb": 173.0, "Lu": 175.0, "Hf": 178.5, "Ta": 180.9, "W": 183.8,
 "Re": 186.2, "Os": 190.2, "Ir": 192.2, "Pt": 195.1, "Au": 197.0, "Hg": 200.6, "Tl": 204.4, "Pb": 207.2,
 "Bi": 208.9, "Po": 209.0, "At": 210.0, "Rn": 222.0, "Fr": 223.0, "Ra": 226.0, "Ac": 227.0, "Th": 232.0,
 "Pa": 231.0, "U": 238.0, "Np": 237.0, "Pu": 244.0, "Am": 243.0, "Cm": 247.0, "Bk": 247.0, "Cf": 251.0,
 "Es": 252.0, "Fm": 257.0, "Md": 258.0, "No": 259.0, "Lr": 262.0, "Rf": 267.0, "Db": 270.0, "Sg": 271.0,
 "Bh": 270.0, "Hs": 277.0, "Mt": 276.0, "Ds": 281.0, "Rg": 280.0, "Cn": 285.0, "Nh": 284.0, "Fl": 289.0,
 "Mc": 288.0, "Lv": 293.0, "Ts": 294.0, "Og": 294.0
}
elemen_periodik = [
 # Baris 1
 [{"simbol": "H", "golongan": "nonlogam"}] + [{}]*16 + [{"simbol": "He", "golongan": "gas mulia"}],
 
 # Baris 2
 [{"simbol": "Li", "golongan": "logam alkali"},
 {"simbol": "Be", "golongan": "logam alkali tanah"}] + [{}]*10 + 
 [{"simbol": "B", "golongan": "metaloid"},
 {"simbol": "C", "golongan": "nonlogam"},
 {"simbol": "N", "golongan": "nonlogam"},
 {"simbol": "O", "golongan": "nonlogam"},
 {"simbol": "F", "golongan": "halogen"},
 {"simbol": "Ne", "golongan": "gas mulia"}],
 
 # Baris 3
 [{"simbol": "Na", "golongan": "logam alkali"},
 {"simbol": "Mg", "golongan": "logam alkali tanah"}] + [{}]*10 +
 [{"simbol": "Al", "golongan": "logam pasca transisi"},
 {"simbol": "Si", "golongan": "metaloid"},
 {"simbol": "P", "golongan": "nonlogam"},
 {"simbol": "S", "golongan": "nonlogam"},
 {"simbol": "Cl", "golongan": "halogen"},
 {"simbol": "Ar", "golongan": "gas mulia"}],
 # Baris 4
 [{"simbol": "K", "golongan": "logam alkali"},
 {"simbol": "Ca", "golongan": "logam alkali tanah"},
 {"simbol": "Sc", "golongan": "logam transisi"},
 {"simbol": "Ti", "golongan": "logam transisi"},
 {"simbol": "V", "golongan": "logam transisi"},
 {"simbol": "Cr", "golongan": "logam transisi"},
 {"simbol": "Mn", "golongan": "logam transisi"},
 {"simbol": "Fe", "golongan": "logam transisi"},
 {"simbol": "Co", "golongan": "logam transisi"},
 {"simbol": "Ni", "golongan": "logam transisi"},
 {"simbol": "Cu", "golongan": "logam transisi"},
 {"simbol": "Zn", "golongan": "logam transisi"},
 {"simbol": "Ga", "golongan": "logam pasca transisi"},
 {"simbol": "Ge", "golongan": "metaloid"},
 {"simbol": "As", "golongan": "metaloid"},
{"simbol": "Se", "golongan": "nonlogam"},
 {"simbol": "Br", "golongan": "halogen"},
 {"simbol": "Kr", "golongan": "gas mulia"}],
 # Baris 5
 [{"simbol": "Rb", "golongan": "logam alkali"},
 {"simbol": "Sr", "golongan": "logam alkali tanah"},
 {"simbol": "Y", "golongan": "logam transisi"},
 {"simbol": "Zr", "golongan": "logam transisi"},
 {"simbol": "Nb", "golongan": "logam transisi"},
 {"simbol": "Mo", "golongan": "logam transisi"},
 {"simbol": "Tc", "golongan": "logam transisi"},
 {"simbol": "Ru", "golongan": "logam transisi"},
 {"simbol": "Rh", "golongan": "logam transisi"},
 {"simbol": "Pd", "golongan": "logam transisi"},
 {"simbol": "Ag", "golongan": "logam transisi"},
 {"simbol": "Cd", "golongan": "logam transisi"},
 {"simbol": "In", "golongan": "logam pasca transisi"},
 {"simbol": "Sn", "golongan": "logam pasca transisi"},
 {"simbol": "Sb", "golongan": "metaloid"},
 {"simbol": "Te", "golongan": "metaloid"},
 {"simbol": "I", "golongan": "halogen"},
 {"simbol": "Xe", "golongan": "gas mulia"}],
 # Baris 6
 [{"simbol": "Cs", "golongan": "logam alkali"},
 {"simbol": "Ba", "golongan": "logam alkali tanah"}] +
 [{"simbol": ""}] * 2 +
 [{"simbol": "La", "golongan": "lanthanida"},
 {"simbol": "Ce", "golongan": "lanthanida"},
 {"simbol": "Pr", "golongan": "lanthanida"},
 {"simbol": "Nd", "golongan": "lanthanida"},
 {"simbol": "Pm", "golongan": "lanthanida"},
 {"simbol": "Sm", "golongan": "lanthanida"},
 {"simbol": "Eu", "golongan": "lanthanida"},
 {"simbol": "Gd", "golongan": "lanthanida"},
 {"simbol": "Tb", "golongan": "lanthanida"},
 {"simbol": "Dy", "golongan": "lanthanida"},
 {"simbol": "Ho", "golongan": "lanthanida"},
 {"simbol": "Er", "golongan": "lanthanida"},
 {"simbol": "Tm", "golongan": "lanthanida"},
 {"simbol": "Yb", "golongan": "lanthanida"},
 {"simbol": "Lu", "golongan": "lanthanida"}] +
 [{"simbol": "Hf", "golongan": "logam transisi"},
 {"simbol": "Ta", "golongan": "logam transisi"},
 {"simbol": "W", "golongan": "logam transisi"},
 {"simbol": "Re", "golongan": "logam transisi"},
 {"simbol": "Os", "golongan": "logam transisi"},
 {"simbol": "Ir", "golongan": "logam transisi"},
 {"simbol": "Pt", "golongan": "logam transisi"},
 {"simbol": "Au", "golongan": "logam transisi"},
 {"simbol": "Hg", "golongan": "logam transisi"},
 {"simbol": "Tl", "golongan": "logam pasca transisi"},
 {"simbol": "Pb", "golongan": "logam pasca transisi"},
 {"simbol": "Bi", "golongan": "logam pasca transisi"},
 {"simbol": "Po", "golongan": "metaloid"},
 {"simbol": "At", "golongan": "halogen"},
 {"simbol": "Rn", "golongan": "gas mulia"}],
# Baris 7
 [{"simbol": "Fr", "golongan": "logam alkali"},
 {"simbol": "Ra", "golongan": "logam alkali tanah"}] +
 [{"simbol": ""}] * 2 +
 [{"simbol": "Ac", "golongan": "aktinida"},
 {"simbol": "Th", "golongan": "aktinida"},
 {"simbol": "Pa", "golongan": "aktinida"},
 {"simbol": "U", "golongan": "aktinida"},
 {"simbol": "Np", "golongan": "aktinida"},
 {"simbol": "Pu", "golongan": "aktinida"},
 {"simbol": "Am", "golongan": "aktinida"},
 {"simbol": "Cm", "golongan": "aktinida"},
 {"simbol": "Bk", "golongan": "aktinida"},
 {"simbol": "Cf", "golongan": "aktinida"},
 {"simbol": "Es", "golongan": "aktinida"},
 {"simbol": "Fm", "golongan": "aktinida"},
 {"simbol": "Md", "golongan": "aktinida"},
 {"simbol": "No", "golongan": "aktinida"},
 {"simbol": "Lr", "golongan": "aktinida"}] +
 [{"simbol": "Rf", "golongan": "logam transisi"},
 {"simbol": "Db", "golongan": "logam transisi"},
 {"simbol": "Sg", "golongan": "logam transisi"},
 {"simbol": "Bh", "golongan": "logam transisi"},
 {"simbol": "Hs", "golongan": "logam transisi"},
 {"simbol": "Mt", "golongan": "logam transisi"},
 {"simbol": "Ds", "golongan": "logam transisi"},
 {"simbol": "Rg", "golongan": "logam transisi"},
 {"simbol": "Cn", "golongan": "logam transisi"},
 {"simbol": "Nh", "golongan": "logam pasca transisi"},
 {"simbol": "Fl", "golongan": "logam pasca transisi"},
 {"simbol": "Mc", "golongan": "logam pasca transisi"},
 {"simbol": "Lv", "golongan": "logam pasca transisi"},
 {"simbol": "Ts", "golongan": "halogen"},
 {"simbol": "Og", "golongan": "gas mulia"}]
]
Ar_tiap_unsur = massa_atom

import streamlit as st
import pandas as pd

st.title("Tabel Periodik Unsur")

df = pd.read_csv("data/periodic_table.csv")

pilih = st.selectbox(
    "Pilih Unsur",
    df["simbol"]
)

unsur = df[df["simbol"] == pilih].iloc[0]

st.write("### Informasi Unsur")
st.write(f"Nama : {unsur['nama']}")
st.write(f"Nomor Atom : {unsur['nomor_atom']}")
st.write(f"Massa Atom : {unsur['massa_atom']}")

 nomor_atom,simbol,nama,massa_atom
1,H,Hidrogen,1.008
2,He,Helium,4.003
3,Li,Litium,6.94
4,Be,Berilium,9.012
5,B,Boron,10.81
6,C,Karbon,12.011
7,N,Nitrogen,14.007
8,O,Oksigen,15.999
9,F,Fluorin,18.998
10,Ne,Neon,20.180
11,Na,Natrium,22.990
12,Mg,Magnesium,24.305
13,Al,Aluminium,26.982
14,Si,Silikon,28.085
15,P,Fosfor,30.974
16,S,Sulfur,32.06
17,Cl,Klorin,35.45
18,Ar,Argon,39.948
19,K,Kalium,39.098
20,Ca,Kalsium,40.078
21,Sc,Skandium,44.956
22,Ti,Titanium,47.867
23,V,Vanadium,50.942
24,Cr,Kromium,51.996
25,Mn,Mangan,54.938
26,Fe,Besi,55.845
27,Co,Kobalt,58.933
28,Ni,Nikel,58.693
29,Cu,Tembaga,63.546
30,Zn,Seng,65.38
31,Ga,Galium,69.723
32,Ge,Germanium,72.630
33,As,Arsen,74.922
34,Se,Selenium,78.971
35,Br,Bromin,79.904
36,Kr,Kripton,83.798
37,Rb,Rubidium,85.468
38,Sr,Stronsium,87.62
39,Y,Yitrium,88.906
40,Zr,Zirkonium,91.224
41,Nb,Niobium,92.906
42,Mo,Molibdenum,95.95
43,Tc,Teknesium,98
44,Ru,Rutenium,101.07
45,Rh,Rodium,102.91
46,Pd,Paladium,106.42
47,Ag,Perak,107.87
48,Cd,Kadmium,112.41
49,In,Indium,114.82
50,Sn,Timah,118.71
51,Sb,Antimon,121.76
52,Te,Telurium,127.60
53,I,Iodin,126.90
54,Xe,Xenon,131.29
55,Cs,Sesium,132.91
56,Ba,Barium,137.33
57,La,Lantanum,138.91
58,Ce,Cerium,140.12
59,Pr,Praseodimium,140.91
60,Nd,Neodimium,144.24
61,Pm,Prometium,145
62,Sm,Samarium,150.36
63,Eu,Europium,151.96
64,Gd,Gadolinium,157.25
65,Tb,Terbium,158.93
66,Dy,Disprosium,162.50
67,Ho,Holmium,164.93
68,Er,Erbium,167.26
69,Tm,Tulium,168.93
70,Yb,Ytterbium,173.05
71,Lu,Lutesium,174.97
72,Hf,Hafnium,178.49
73,Ta,Tantalum,180.95
74,W,Tungsten,183.84
75,Re,Rhenium,186.21
76,Os,Osmium,190.23
77,Ir,Iridium,192.22
78,Pt,Platina,195.08
79,Au,Emas,196.97
80,Hg,Merkuri,200.59
81,Tl,Talium,204.38
82,Pb,Timbal,207.2
83,Bi,Bismut,208.98
84,Po,Polonium,209
85,At,Astatin,210
86,Rn,Radon,222
87,Fr,Fransium,223
88,Ra,Radium,226
89,Ac,Aktinium,227
90,Th,Torium,232.04
91,Pa,Protaktinium,231.04
92,U,Uranium,238.03
93,Np,Neptunium,237
94,Pu,Plutonium,244
95,Am,Amerisium,243
96,Cm,Kurium,247
97,Bk,Berkelium,247
98,Cf,Kalifornium,251
99,Es,Einsteinium,252
100,Fm,Fermium,257
101,Md,Mendelevium,258
102,No,Nobelium,259
103,Lr,Lawrensium,266
104,Rf,Rutherfordium,267
105,Db,Dubnium,268
106,Sg,Seaborgium,269
107,Bh,Bohrium,270
108,Hs,Hassium,277
109,Mt,Meitnerium,278
110,Ds,Darmstadtium,281
111,Rg,Roentgenium,282
112,Cn,Kopernisium,285
113,Nh,Nihonium,286
114,Fl,Flerovium,289
115,Mc,Moskovium,290
116,Lv,Livermorium,293
117,Ts,Tennessine,294
118,Og,Oganesson,294
import re

Ar = dict(zip(df["simbol"], df["massa_atom"]))

def hitung_massa_molar(rumus):
    total = 0

    token = re.findall(r'([A-Z][a-z]?)(\d*)', rumus)

    for unsur, jumlah in token:
        jumlah = int(jumlah) if jumlah else 1
        total += Ar[unsur] * jumlah

    return total
 st.subheader("Kalkulator Massa Molar")

rumus = st.text_input("Masukkan Rumus Kimia")

if rumus:
    mm = hitung_massa_molar(rumus)
    st.success(f"Massa Molar = {mm:.3f} g/mol")

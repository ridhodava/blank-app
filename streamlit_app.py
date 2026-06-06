import streamlit as st
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="Kalkulator Turbin Air", layout="centered")

st.title("🌊 Estimasi Daya Listrik Turbin Air")
st.write("Aplikasi sederhana untuk menghitung estimasi daya listrik yang dihasilkan oleh sistem turbin air berdasarkan prinsip Mekanika Fluida.")

# --- BAGIAN INPUT ---
st.sidebar.header("Parameter Input")
Q = st.sidebar.number_input("Debit Air (m³/s)", min_value=0.0, value=10.0, step=0.5)
H = st.sidebar.number_input("Head Turbin (m)", min_value=0.0, value=50.0, step=1.0)
efisiensi_persen = st.sidebar.slider("Efisiensi Sistem (%)", min_value=0, max_value=100, value=85)

# --- BAGIAN PERHITUNGAN ---
# Konstanta
rho = 1000  # Massa jenis air (kg/m^3)
g = 9.81    # Percepatan gravitasi (m/s^2)
eta = efisiensi_persen / 100.0  # Konversi persen ke desimal

# Menghitung Daya (dalam Watt, lalu dikonversi ke kiloWatt)
daya_potensial_w = rho * g * Q * H
daya_aktual_w = daya_potensial_w * eta

daya_potensial_kw = daya_potensial_w / 1000
daya_aktual_kw = daya_aktual_w / 1000

# --- BAGIAN OUTPUT ---
st.subheader("⚡ Hasil Perhitungan Daya")
st.success(f"Estimasi Daya Listrik yang Dihasilkan: **{daya_aktual_kw:,.2f} kW**")

# --- VISUALISASI SEDERHANA ---
st.subheader("📊 Visualisasi Sistem")
st.write("Grafik di bawah ini membandingkan daya energi potensial air murni dengan daya listrik aktual yang dihasilkan setelah memperhitungkan rugi-rugi (efisiensi).")

fig, ax = plt.subplots(figsize=(6, 4))
kategori = ['Daya Potensial (100% Efisiensi)', 'Daya Aktual Dihasilkan']
nilai = [daya_potensial_kw, daya_aktual_kw]
warna = ['#3498db', '#2ecc71']

bars = ax.bar(kategori, nilai, color=warna)
ax.set_ylabel('Daya (kW)')
ax.set_title('Perbandingan Daya Potensial vs Daya Aktual')
ax.set_ylim(0, max(nilai) * 1.2) # Memberikan ruang di atas bar untuk teks

# Menambahkan label angka di atas bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + (max(nilai)*0.02), f'{yval:,.2f} kW', ha='center', va='bottom', fontweight='bold')

st.pyplot(fig)

st.markdown("---")
st.caption("Dibuat untuk Tugas Besar Mekanika Fluida")

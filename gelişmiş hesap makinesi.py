import streamlit as st
import math
import time

# 🎨 Başlık ve açıklama
st.set_page_config(page_title="Hesap Makinesi", page_icon="🧮", layout="centered")

st.title("🧮 Akıllı Hesap Makinesi")

st.markdown("""
### 👇 İşlem Seçiniz
Aşağıdan yapmak istediğiniz matematiksel işlemi seçin:
""")

# 🎛 İşlem Seçimi
işlem = st.radio(
    "İşlem türü:",
    ("Toplama ➕", "Çıkarma ➖", "Çarpma ✖️", "Bölme ➗", "Üs Alma ⬆️", "Karekök 🔢", "Logaritma 🧠", "Çıkış 🚪")
)

# 🧮 İşlem Seçimi Mantığı
if işlem == "Çıkış 🚪":
    st.warning("İşleminiz sonlandırılıyor...")
    time.sleep(1)
    st.success("👋 Tekrar bekleriz!")
    st.stop()

# 🔢 Sayı Girişi ve İşlemler
if işlem == "Toplama ➕":
    sayı1 = st.number_input("Birinci sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("İkinci sayıyı giriniz:", step=1.0)
    if st.button("Topla ➕"):
        time.sleep(0.5)
        st.success(f"{sayı1} + {sayı2} = {sayı1 + sayı2}")

elif işlem == "Çıkarma ➖":
    sayı1 = st.number_input("Birinci sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("İkinci sayıyı giriniz:", step=1.0)
    if st.button("Çıkar ➖"):
        time.sleep(0.5)
        st.success(f"{sayı1} - {sayı2} = {sayı1 - sayı2}")

elif işlem == "Çarpma ✖️":
    sayı1 = st.number_input("Birinci sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("İkinci sayıyı giriniz:", step=1.0)
    if st.button("Çarp ✖️"):
        time.sleep(0.5)
        st.success(f"{sayı1} × {sayı2} = {sayı1 * sayı2}")

elif işlem == "Bölme ➗":
    sayı1 = st.number_input("Birinci sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("İkinci sayıyı giriniz:", step=1.0)
    if st.button("Böl ➗"):
        if sayı2 == 0:
            st.error("❌ Bir sayı sıfıra bölünemez!")
        else:
            time.sleep(0.5)
            st.success(f"{sayı1} ÷ {sayı2} = {sayı1 / sayı2}")

elif işlem == "Üs Alma ⬆️":
    sayı1 = st.number_input("Tabanı giriniz:", step=1.0)
    sayı2 = st.number_input("Üssü giriniz:", step=1.0)
    if st.button("Üs Al ⬆️"):
        time.sleep(0.5)
        st.success(f"{sayı1} üssü {sayı2} = {math.pow(sayı1, sayı2)}")

elif işlem == "Karekök 🔢":
    sayı1 = st.number_input("Sayıyı giriniz:", step=1.0)
    if st.button("Karekök Al 🔢"):
        if sayı1 < 0:
            st.error("❌ Negatif sayının karekökü alınamaz!")
        else:
            time.sleep(0.5)
            st.success(f"{sayı1} sayısının karekökü = {math.sqrt(sayı1)}")

elif işlem == "Logaritma 🧠":
    sayı1 = st.number_input("Sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("Logaritmanın tabanını giriniz:", step=1.0)
    if st.button("Logaritma Hesapla 🧠"):
        if sayı1 <= 0 or sayı2 <= 0 or sayı2 == 1:
            st.error("❌ Geçersiz değer! Logaritmada sayı ve taban > 0 olmalı, taban ≠ 1 olmalı.")
        else:
            time.sleep(0.5)
            st.success(f"{sayı1} sayısının {sayı2} tabanında logaritması = {math.log(sayı1, sayı2)}")

# 🎨 Alt yazı
st.markdown("---")
st.caption("💡 *Streamlit ile geliştirilmiştir — Barış Kaya için özel sürüm*")


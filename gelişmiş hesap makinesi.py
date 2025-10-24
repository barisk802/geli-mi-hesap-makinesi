import streamlit as st
import math
import time

st.title("🧮 Hesap Makinesi")

st.write("""
**İşlem Seçenekleri:**

1️⃣ Toplama  
2️⃣ Çıkarma  
3️⃣ Çarpma  
4️⃣ Bölme  
5️⃣ Üs almak  
6️⃣ Sayının karekökünü almak  
7️⃣ Sayının logaritmasını almak  
🛑 Çıkmak için 'q' yazın.
""")

işlem = st.text_input("İşleminizi Giriniz (1-7 veya q):")

if işlem == "q":
    st.warning("İşleminiz sonlandırılıyor...")
    time.sleep(1)
    st.success("Tekrar bekleriz..")

elif işlem == "1":
    sayı1 = st.number_input("Birinci sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("İkinci sayıyı giriniz:", step=1.0)
    if st.button("Toplama Yap"):
        time.sleep(1)
        st.success(f"{sayı1} + {sayı2} = {sayı1 + sayı2}")

elif işlem == "2":
    sayı1 = st.number_input("Birinci sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("İkinci sayıyı giriniz:", step=1.0)
    if st.button("Çıkarma Yap"):
        time.sleep(1)
        st.success(f"{sayı1} - {sayı2} = {sayı1 - sayı2}")

elif işlem == "3":
    sayı1 = st.number_input("Birinci sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("İkinci sayıyı giriniz:", step=1.0)
    if st.button("Çarpma Yap"):
        time.sleep(1)
        st.success(f"{sayı1} * {sayı2} = {sayı1 * sayı2}")

elif işlem == "4":
    sayı1 = st.number_input("Birinci sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("İkinci sayıyı giriniz (0 olmasın):", step=1.0)
    if st.button("Bölme Yap"):
        if sayı2 == 0:
            st.error("Bir sayı sıfıra bölünemez!")
        else:
            time.sleep(1)
            st.success(f"{sayı1} / {sayı2} = {sayı1 / sayı2}")

elif işlem == "5":
    sayı1 = st.number_input("Tabanı giriniz:", step=1.0)
    sayı2 = st.number_input("Üssü giriniz:", step=1.0)
    if st.button("Üs Al"):
        time.sleep(1)
        st.success(f"{sayı1} üssü {sayı2} = {math.pow(sayı1, sayı2)}")

elif işlem == "6":
    sayı1 = st.number_input("Sayıyı giriniz:", step=1.0)
    if st.button("Karekök Al"):
        if sayı1 < 0:
            st.error("Negatif sayının karekökü alınamaz!")
        else:
            time.sleep(1)
            st.success(f"{sayı1} sayısının karekökü = {math.sqrt(sayı1)}")

elif işlem == "7":
    sayı1 = st.number_input("Sayıyı giriniz:", step=1.0)
    sayı2 = st.number_input("Logaritmanın tabanını giriniz:", step=1.0)
    if st.button("Logaritma Hesapla"):
        if sayı1 <= 0 or sayı2 <= 0 or sayı2 == 1:
            st.error("Geçersiz değer! Logaritmada sayı ve taban > 0 olmalı, taban ≠ 1 olmalı.")
        else:
            time.sleep(1)
            st.success(f"{sayı1} sayısının {sayı2} tabanında logaritması = {math.log(sayı1, sayı2)}")

elif işlem:
    st.error("Geçersiz işlem! Lütfen 1-7 arası bir değer veya 'q' girin.")

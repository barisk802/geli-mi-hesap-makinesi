print("""*********

Hesap Makinesi 

Toplama = 1
Çıkarma = 2
Çarpma = 3
Bölme = 4
Üs almak için = 5
Sayının karekökünü almak için = 6 
Sayının logaritması için = 7
Çıkmak için q ya basın...


*********""")
import time
import math
while True:
    işlem=input("İşleminizi Giriniz:")

    if işlem=="q":
        print("İşleminiz sonlandırılıyor...")
        time.sleep(1)
        print("Tekrar bekleriz..")
        break

    elif işlem=="1":
        sayı1=int(input("Sayıyı giriniz :"))
        sayı2=int(input("Sayıyı giriniz :"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} + {} = {}".format(sayı1,sayı2,sayı1+sayı2))

    elif işlem=="2":
        sayı1=int(input("Sayıyı giriniz :"))
        sayı2=int(input("Sayıyı giriniz :"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} - {} = {}".format(sayı1,sayı2,sayı1-sayı2))

    elif işlem=="3":
        sayı1 = int(input("Sayıyı giriniz :"))
        sayı2 = int(input("Sayıyı giriniz :"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} * {} = {}".format(sayı1,sayı2,sayı1*sayı2))

    elif işlem=="4":
        sayı1 = int(input("Sayıyı giriniz :"))
        sayı2 = int(input("Sayıyı giriniz :"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} / {} = {}".format(sayı1,sayı2,sayı1/sayı2))

    elif işlem=="5":
        sayı1 = int(input("Sayıyı tabanını giriniz :"))
        sayı2 = int(input("Üssü giriniz :"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        x=math.pow(sayı1,sayı2)
        print("{} üssü {} = {}".format(sayı1,sayı2,math.pow(sayı1,sayı2)))

    elif işlem=="6":
        sayı1 = int(input("Sayıyı giriniz :"))

        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        x=math.sqrt(sayı1)
        print("{} sayısının karekökü = {}".format(sayı1,math.sqrt(sayı1)))

    elif işlem=="7":
        sayı1 = int(input("Sayıyı giriniz :"))
        sayı2 = int(input("logaritmanın tabanını giriniz :"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} sayısının {} tabanında logaritması = {} ".format(sayı1,sayı2,math.log(sayı1,sayı2)))

    else:
        print("Geçersiz İşlem!")
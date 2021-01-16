from sarki import *

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Sarkı Ekle

3. Sarkı Sil 

4. Listedeki şarkı süresi toplamı

Çıkmak için 'q' ya basın.
***********************************""")

sarki = Sarki()

while True:
    işlem = input("Yapacağınız İşlem:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (işlem == "1"):
        sarki.sarkilari_goster()

    elif (işlem == "2"):
        sarki = input("sarki:")
        sanatci = input("sanatci:")
        album = input("album:")
        prodüksiyon = input("prodüksiyon:")
        sure = int(input("sure"))

        yeni_sarki = Sarki(sarki,sanatci,album,prodüksiyon,sure)

        print("Sarkı ekleniyor....")
        time.sleep(2)

        sarki.sarki_ekle(yeni_sarki)
        print("Kitap Eklendi....")


    elif (işlem == "4"):
        sarki = input("Hangi kitabı silmek istiyorsunuz ?")

        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Kitap Siliniyor...")
            time.sleep(2)
            sarki.sarki_sil(sarki)
            print("Kitap silindi....")

    else:
        print("Geçersiz İşlem...")

#   Siz de bir tane Şarkı projesi geliştirmeye çalışın.

#                     Örnek özellikler;

#                     1. Şarkı İsmi 
#                     2. Sanatçı
#                     3. Albüm
#                     4. Prodüksiyon Şirketi
#                     5. Şarkı Süresi

#                     Örnek Metodlar;

#                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
#                     2. Şarkı Ekle
#                     3. Şarkı Sil


import sqlite3

import time

class Album():

    def __init__(self,sarki,sanatci,album,prodüksiyon,sure):

        self.sarki = sarki
        self.sanatci = sanatci
        self.album = album
        self.prodüksiyon = prodüksiyon
        self.sure = sure

    # Album nesnesini print yardımı ile bastırmak için str tanımlıyoruz
    def __str__(self):

        return "sarki: {}\nsanatci: {}\nalbum: {}\nprodüksiyon: {}\nsure: {}".format(self.sarki,self.sanatci,self.album,self.prodüksiyon,self.sure)


class Playlist():
    def __init__(self):

        self.baglanti_olustur()

    # veri tabanı bağlantısı 
    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("sarki.db")

        # veritabanı üzerinde işlem gerçekleştirecek cursor oluşturuyoruz
        self.cursor = self.baglanti.cursor()

        # tablo oluşturuyoruz
        sorgu = "Create Table If not exists sarkilar (sarki TEXT,sanatci TEXT,album TEXT,prodüksiyon TEXT,sure INT)"

        #veritabanı oluşturulması
        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def sarkilari_goster(self):

        sorgu =  "Select * From sarkilar"

        self.cursor.execute(sorgu)

        #veritabanı bilgilerini okuma
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Şarkı bulunmuyor...")
        else:
            for i in sarkilar:

                album = Album(i[0],i[1],i[2],i[3],i[4])
                print(album)    
        
    def sarki_ekle(self,sarki):

        sorgu = "Insert into sarkilar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(sarki.isim,sarki.yazar,sarki.yayınevi,sarki.tür,sarki.baskı))

        self.baglanti.commit()

    def sarki_sil(self,silinecek):

        sorgu = "Delete From kitaplar where sil = ?"

        self.cursor.execute(sorgu,(silinecek,))

        self.baglanti.commit()


    def toplam_sure(self):

        sorgu =  "Select * From  where sure= ?"

        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
   

        for i in sarkilar:    
            sure= sure + sarkilar[0][4]
        print("Toplam= {}",sure)    








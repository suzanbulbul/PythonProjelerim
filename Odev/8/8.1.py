import random
import time


class Kumanda():
    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tvAc(self):
        if(self.tv_durum == "Açık"):
            print("Tv zaten açık")
        else:
            print("Tv açılıyor.")
            self.tv_durum = "Açık"

    def tvKapat(self):
        if(self.tv_durum == "Kapli"):
            print("Tv zaten kapalı")
        else:
            print("Tv kapatılıyor.")
            self.tv_durum = "Kapalı"

    def sesAyarla(self):

        while True:
            cevap = input("Sesi arttırmak: >\nSesi azaltma: <\nÇıkış: exit")

            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses-= 1
                    print("Ses: ",self.tv_ses)
                else:
                    print("Ses zaten kapalı")    
                
            elif(cevap == ">"):
                if(self.tv_ses != 31):
                    self.tv_ses+= 1
                    print("Ses: ",self.tv_ses)
                else:
                    print("Ses zaten full")

            elif(cevap == "exit"): 
                print("Çıkış yapılıyor...")
                break   
            else:
                print("Hatalı işlem...")    

    def kanalEkle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print(kanal_ismi)

    def rastgeleKanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal: ",self.kanal)

    def __len__(self):
         return len(self.kanal_listesi)

    def __str__(self):
        return "tv Durumu: {}\nSes: {}\nKanal Listesi: {}\nŞu anki Kanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)         


kumanda = Kumanda()
print(""""
Televisyon Uygulama:
1.Tv aç
2.Tv kapat
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısının Öğrenme
6.Rasgele Kanala Geçe
7.Televizyon Bilgileri
Çıkış için q ya basın
""")    

while True:

    islem= input("İşlem türünü seçin")

    if(islem == "q"):
        print("Program sonlandırılıyor...")
        break

    elif(islem == "1"):
        kumanda.tvAc()

    elif(islem == "2"):
        kumanda.tvKapat()

    elif(islem == "3"):
        kumanda.sesAyarla()

    # BURADA TAKILIYOSUN SAYIN SB     
    elif(islem == "4"):
        kanal_isimleri= input("Kanal isimlerini , ile ayırarak yazın")
        kanal_listesi= kanal_isimleri.split(",")    #split = () içerisindekyazılan değeri görünce ayırır
        for eklenecekler in kanal_listesi:
            kumanda.kanalEkle(eklenecekler)

    elif(islem == "5"):
        print("Kanal sayısı: ",len(kumanda))

    elif(islem== "6"):
        kumanda.rastgeleKanal()

    elif(islem== "7"):
        print(kumanda)

    else:
        print("Geçersiz işlem...")            


    




            

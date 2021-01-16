class Calisan:
    # constructor tanımlıyoruz
    def __init__(self, isim, maas, departman):
        self.isim= isim
        self.maas= maas
        self.departman= departman

    def bilgileriGoster(self):
         print("""" 
        Çalışan sınıfının özellikleri:
        isim: {}
        Maaş: {}
        Departman: {}
        """.format(self.isim,self.maas, self.departman))

    def departmanDegistir(self, yeni_departman):
        self.departman= yeni_departman 

class Yonetici(Calisan):    # Çalışanlardan kalıtım yaptık   

    def __init__(self, isim, maas, departman, kisi_sayisi):
        super().__init__(isim, maas, departman)
        self.kisi_sayisi= kisi_sayisi

    def bilgileriGoster(self):
         print("""" 
        Yönetici sınıfının özellikleri:
        isim: {}
        Maaş: {}
        Departman: {}
        Sorumlu Kisi Sayısı {}
        """.format(self.isim,self.maas, self.departman, self.kisi_sayisi))    
    
    def zamYap(self, yeni_maas):
        self.maas+= yeni_maas   
     
            

calisan = Calisan("Suzan",3500 ,"Bilişim")
calisan.bilgileriGoster()
calisan.departmanDegistir("Bilgi İşlem")
calisan.bilgileriGoster()
print("*********************************************")
yonetici = Yonetici("Gürkan", 5000, "Bilişim", 10)
yonetici.bilgileriGoster()
yonetici.zamYap(500)
yonetici.bilgileriGoster()






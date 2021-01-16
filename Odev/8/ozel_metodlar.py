class Kitap:
    #init methodu tanımlama
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        self.isim= isim
        self.yazar= yazar
        self.sayfa_sayisi= sayfa_sayisi
        self.tur= tur

    #self metodu tanımlama    
    def __str__(self):    
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}\n".format(self.isim, self.yazar, self.sayfa_sayisi, self.tur)    
    
    #len metodu tanımlama
    def __len__(self):
        return self.sayfa_sayisi
    
    #del metodu tanımlama
    def __del__(self):
        print("Kitap objesi siliniyo...")


#init methodu çağırma
kitap = Kitap("İstanbul Hatırası","Ahmet Ümit",561 ,"Polisiye")

#self metodu çağırma
print("Self metodu")
print(kitap)

#len metodu çağırma
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561 ,"Polisiye")
print("len metodu")
len(kitap1)

#del metodu tanımlama
del kitap   #kitap objesini siler
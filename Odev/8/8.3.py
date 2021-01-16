#   Bu projede ise 4 tane sınıfı oluşturun.
#   Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.
#   Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
#   Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.
#   At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.


class Hayvan():
    def __init__(self, isim, yas, renk, cins ):
        self.isim= isim
        self.yas= yas
        self.renk= renk
        self.cins= cins

    def bilgileriGoster(self):
        print("""" 
        Hayvan özellikleri yazılıyor:
        isim: {}
        Yas: {}
        Renk: {}
        Cins: {}
        """.format(self.isim, self.yas, self.renk, self.cins))   

class Kopek(Hayvan):
    def __init__(self, isim, yas, cins,):
        super().__init__(self, isim, yas, renk, cins)
    def evcilMi(evcil):
        if(evcil == "evet"):
            print("Çocuğunla mutluluklar :)")    
        else:
            print("Sahiplenmeye ne dersin")              
class Kus(Hayvan):
    def __init__(self, isim, yas, cins, ):
        super().__init__(self, isim, yas, renk)
    def konusuyorMu(konusma):
        if(konusma == "evet"):
            print("Papağan mı ya :D")    
        else:
            print("Üzülme belki zamanla öğrenir :)")
class At(Hayvan):
    def __init__(self, isim, yas, cins, hiz):
        super().__init__(self, isim, yas, renk)
        self hiz= hiz

hayvan = Hayvan("Kedi",2 ,"Beyaz", "İran")
kopek = Kopek(

        
            
    
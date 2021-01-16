#   Python’da bir nesne çağırdığınızda otomatik olarak çalışacak ve sadece nesneyi ilk oluşturduğunuzda çalışacak 
#  olan bir fonksiyon tanımlayabilirsiniz. Bu fonksiyonun adı Python yapımcıları tarafından __init__() olarak 
#  belirlenmiş. Dışarıdan ulaşılmasını istediğimiz her fonksiyona self parametresini eklememiz gerektiğini de 
#  belirtelim.

class Dosya():

    def __init__(self,dosya_ismi):

        with open(dosya_ismi,"r",encoding = "utf-8") as file:

            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()

            self.sade_kelimeler = list()

            for kelime in kelimeler:
                kelime = kelime.strip()
                kelime = kelime.strip(".")
                kelime = kelime.strip("\n")

                self.sade_kelimeler.append(kelime)
    def kelime_bul(self,aranan):

        konumlar = list()
        say = 1
        for kelime in self.sade_kelimeler:
            if (kelime == aranan ):
                konumlar.append(say)

            say += 1

        if (len(konumlar) == 0):
            print("Dosyada böyle bir kelime bulunmuyor...")
        else:

            print("{} kelimesi dosyada şuralarda geçiyor. \n{}".format(aranan,konumlar))



    def kelime_histogramı(self):

        kelime_frekansı = dict()
        kelime_kümesi = set()

        for kelime in self.sade_kelimeler:
            kelime_kümesi.add(kelime)
            if (kelime in kelime_frekansı):
                kelime_frekansı[kelime] += 1
            else:
                kelime_frekansı[kelime] = 1
        print("Kelimelerin Frekansı........................")
        for i, j in kelime_frekansı.items():
            print("{} kelimesi metinde {} defa geçiyor.".format(i, j))

        print("Tüm Kelimeler")
        for i in kelime_kümesi:
            print(i)
            print("*************************************")


dosya =  Dosya("dosya.txt")
print("""****************

Dosya İşlemleri 

1. Tüm kelime frekansını öğren

2. Kelime Ara

Çıkmak için 'q' ya basın.

""")
while True:
    işlem = input("İşlem:")

    if (işlem == "q"):
        print("Programdan Çıkılıyor....")
        break
    elif (işlem == "1"):
        dosya.kelime_histogramı()
    elif (işlem == "2"):
        kelime = input("Hangi kelimeyi arıyorsunuz ?")
        dosya.kelime_bul(kelime)
    else:
        print("Geçersiz İşlem...")



class Yazılımcı():

    def __init__(self, isim, soyisim, numara, maas, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller


    def bilgileriGoster(self):
        print("""" 
        Yazılımcı objesinin özellikleri:
        isim: {}
        Soyisim: {}
        Numara: {}
        Maaş: {}
        Bildiği Diller: {}
        """.format(self.isim, self.soyisim, self.numara, self.maas, self.diller))

    def dilEkle(self, yeni_dil):
        self.diller.append(yeni_dil)    

yazılımcı = Yazılımcı("Suzan","Bülbül",1234,3.500,["Java","c","Python"])
yazılımcı.bilgileriGoster()
print("*******************************")
yazılımcı.dilEkle("Dart")
yazılımcı.bilgileriGoster()

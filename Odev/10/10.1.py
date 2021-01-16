class Ogrenci:
    isim= ""
    puan= 0 
    harf_notu= ""

def not_hesapla(satir):
    ogrenci = Ogrenci()

    #dosya okuma işlemindeki boş satırları siler
    satir= satir[:-1]

    #her satırı , e göre ayırdı
    liste= satir.split(",")

    #Listenin 0 elemanı ismi
    isim= liste[0]
    #Listenin 1 elemanı 1.notu
    not1= int(liste[1])
    #Listenin 2 elemanı 2.notu
    not2= int(liste[2])
    #Listenin 3 elemanı 3.notu
    not3= int(liste[3])

    son_not= not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if(son_not >= 90):
        harf= "AA"
    elif(son_not >= 85):
        harf= "BA"    
    elif(son_not >= 80):
        harf= "BB"
    elif(son_not >= 75):
        harf= "CB"
    elif(son_not >= 65):
        harf= "CC"   
    elif(son_not >= 60):
        harf= "DC"
    elif(son_not >= 55):
        harf= "FD"
    else:
        harf= "FF" 

    ogrenci.isim= isim
    ogrenci.puan= son_not
    ogrenci.harf_notu= harf

    return ogrenci       
    

#DOSYA OKUMA İŞLEMİ
#utf= türkçe karakterler olduğu için 
file1 = open("dosya.txt", "r", encoding="utf-8")
file2 = open("geçenler.txt", "w", encoding="utf-8")
file3 = open("kalanlar.txt", "w", encoding="utf-8")


    #fonk dönen değeri yazmak için boş liste oluşturuyoruz
eklenecekler_listesi= []

    #dosya içerisindeki her satırı fonk. göndermemiz gerek 
for i in file1:

        #fonk. dönen sonucu listenin sonuna yazar
    eklenecekler_listesi.append(not_hesapla(i))

for i in eklenecekler_listesi:
    if i.puan >= 55:
        amk= i.isim +" "+ i.harf_notu +" "+ str(i.puan)+"\n"
        file2.write(amk)
    else:
        amk= i.isim +" "+ i.harf_notu +" "+ str(i.puan)+"\n"
        file3.write(amk)

file1.close()
file2.close()
file3.close()

#with open("benimyazdigim.txt","w",encoding= "utf-8") as file1: 
#    deger= input("gir")  
#    file1.write(deger)



                 



    
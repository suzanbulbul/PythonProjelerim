#Bir sayının tam bölenlerini bulan program (list ile)

def tambolenlerinibulma(sayi):
    tam_bolenler = []

    for i in range(2,sayi):

        if (sayi % i == 0):  #sayı i ye bölünüyorsa

            tam_bolenler.append(i)  #i değerini listenin sonuna ekle

    return tam_bolenler    #tam_bolenler listesini döndürür

while True:

    print("Çıkış için q ya basın")
    sayı = input("Sayi:")

    if(sayı == "q"):      #çıkış için q ya basma işlemi

        print("Program sonlandırılıyot")
        break

    else:

        sayı = int(sayı)    #string değeri int çeviririz
        print("Tam bölenler: " ,tambolenlerinibulma(sayı))   #fonk çağırma işlemi
           
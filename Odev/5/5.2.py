# Armstrong" sayısı olup olmadığını bulmaya çalışın.
#  1634 = 1^4 + 6^4 + 3^4 + 4^4

sayı = input("Sayı:")   #String değer alınır
basamak_sayisi = len(sayı)  #string değerin uzunluğunu alır
sayı = int(sayı)    #string değeri int çevirir
basamak = 0
toplam = 0

gecici_sayı = sayı  

while (gecici_sayı > 0): #len(sayi)= 4 olduğundan 0-4 kadar dön diyoruz
    
    basamak = gecici_sayı % 10 #mod 10 alıyoruz basamak değişkenine atıyoruz
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayı //= 10
    

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")
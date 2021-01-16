# Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

toplam= 0
while True:
    islem= input("Toplama işlemi için 1 e basın\n Çıkış için q ya basın\n")
    if islem == '1':
        sayi = int(input("Sayi girin"))
        toplam = toplam + sayi
        print(toplam)
    elif islem == 'q' :
        print(toplam)
        break
    else:
        print("Hatalı işlem")

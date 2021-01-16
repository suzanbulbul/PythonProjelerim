#   Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
#   Örnek: 97 ---------> Doksan Yedi

listeonlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
listebirler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]

def okunus(sayı):

    onlar= sayı // 10
    birler= sayı % 10

    return listeonlar[onlar] + " " + listebirler[birler]

sayi = int(input("2 basamaklı bir sayı girin"))
print(okunus(sayi))
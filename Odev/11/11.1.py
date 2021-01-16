#   Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.
#            [(3,4),(10,3),(5,6),(1,9)]
#   Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.
#            [12, 30, 30, 9]
#   Not : map() fonksiyonunu kullanmaya çalışın.

#   Örnek:  list(map(lambda x : x ** 2, [1,2,3,4,5,6,7,8,9]))  Çıktı: [1, 4, 9, 16, 25, 36, 49, 64, 81]


def alanHesapla(demet):
     return demet[0]*demet[1]

liste= [(3,4),(10,3),(5,6),(1,9)]

print(list(map(alanHesapla, liste)))

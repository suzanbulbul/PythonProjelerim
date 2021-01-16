#   Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.
#        [(3,4,5),(6,8,10),(3,10,7)]
#   Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.
#        [(3, 4, 5), (6, 8, 10)]
#   Not: filter() fonksiyonunu kullanmaya çalışın.
#   Ö:  list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))   Çıktı:    [2, 4, 6, 8, 10]

#   Üçgen olma şartı:   |b-c| < a < b+c, |a-b| < c < a+b, |a-c| < b < a+c



def ucgenMi(demet):
    
    if (abs(demet[0]+demet[1]) > demet[2] and abs(demet[0]+demet[2]) > demet[1] and abs(demet[1]+demet[2]) > demet[0]):
        return True
    else:
        return False
    
liste= [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(ucgenMi,liste)))




#   Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.
#          isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
#         soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
#   Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.
#   Not: zip() fonksiyonunu kullanmaya çalışın.

liste1 = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
liste2 = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(liste1,liste2):
    print(i,j)
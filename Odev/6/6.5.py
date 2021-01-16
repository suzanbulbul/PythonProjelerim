#   1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def pisagor_bulma():
    
    pisagor_listesi = list()    #boş liste oluştur
    for i in range(1,101):
        for j in range(1,101):

            c = (i ** 2 + j ** 2) ** 0.5    # a^a = karakök( b^b + c^c )

            if (c == int(c) ):
                pisagor_listesi.append((i,j,int(c)))

    return pisagor_listesi

for i in pisagor_bulma():   #i değerini pisagor_bulam fonk çalıştığı kadar dönder ve yazdır
    print(i)




 
# Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

# Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

# Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

# Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

# Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir

secim = int(input("Hesaplamak istediğiniz geometrik şekli seçin \n 1.Dikdörgen\n 2.Üçgen\n"))

if(secim == 1):
    a = int(input("1.Kenar değeri:"))
    b = int(input("2.Kenar değeri:"))
    c = int(input("3.Kenar değeri:"))
    d = int(input("4.Kenar değeri:"))

    if(a==b and a==c and a==d):
        print("Kare")
    elif(a==c and b==d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")    
    
elif(secim == 2):
    a = int(input("1.Kenar değeri:"))
    b = int(input("2.Kenar değeri:"))
    c = int(input("3.Kenar değeri:"))

    if(a==b and a==c):
        print("Eşkenar üçgen")
    elif(a==b or b==c or a==c):
        print("İkizkenar üçgen")
    else:
        print("Çeşitkenar üçgen")   

else:
    print("Geçersiz işlem...")         

    











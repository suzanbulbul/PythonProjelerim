# Mükemmel sayı bulma (kendi bölümlerinin toplamı kendisini vermeli Ö: 2+3+1= 6)

sayi = int(input("Sayıyı girin:"))
mukemmel = 0
i = 1

while(i < sayi):
    if(sayi % i == 0):
        print()
        mukemmel = mukemmel+i
        i+=1
    else:
        i+=1

print(mukemmel)
if(mukemmel == sayi):
    print("Sayı mükemmeldir")
else:
    print("Sayı mükemmel değildir")    

  




    
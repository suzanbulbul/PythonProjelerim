#   Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.


def ebobbulma(a,b):
    ebob= 0

    
    for i in range(1,a):
            
        if(a%i==0 and b%i==0):
            ebob= i
     
    

    print(ebob)             

print("2 SAYIYININ EBOBUNU BULMA: ")
sayı1 = int(input("1.sayıyı girin:"))
sayı2 = int(input("2.sayıyı girin:"))
ebobbulma(sayı1,sayı2)

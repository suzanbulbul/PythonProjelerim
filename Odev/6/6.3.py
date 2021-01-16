#  Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

def ekokbulma(a, b):
    ekok = 1

    for i in range(2, a):

        while True:
            if(a % i == 0 or b % i == 0):

                ekok *= i

                if(a % i == 0 and b % i == 0):
                    a = a/i
                    b = b/i
                elif(a % i == 0):
                    a = a/i
                else:
                    b = b/i

            else:
                break

    print(ekok)


print("2 SAYIYININ EKOKUNU BULMA: ")
sayı1 = int(input("1.sayıyı girin:"))
sayı2 = int(input("2.sayıyı girin:"))
ekokbulma(sayı1, sayı2)

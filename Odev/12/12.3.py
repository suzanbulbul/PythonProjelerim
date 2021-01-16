#   Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.
#                    coskun.m.murat@gmail.com
#                    example@xyz.com
#                    mustafa.com
#                    mustafa@gmail
#                    kerim@yahoo.com
#   İpucu: Stringlerde bulunan endswith() ve find metodlarını kullanabilirsiniz.

#   endswith(x) : String x ile bitiyorsa True, bitmiyorsa False değeri döndürür.
#   find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.



with open("mailler.txt","r",encoding="utf-8") as file:
    for satır in file:
        
        if (satır.endswith(".com") and satır.find("@") != -1):
            print(satır)
            

         
    



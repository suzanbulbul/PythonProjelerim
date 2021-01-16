# list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

liste = [x for x in range(1,101) if x % 2 == 0]  #(ilk fordan sonraki x ile if arası) 1-100 arasında x ile dön. geri kalan kısım şartı sağlayanları x ile dönder
print(liste)
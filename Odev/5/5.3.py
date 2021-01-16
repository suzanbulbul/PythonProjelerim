# 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

for i in range(1,11):
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))

    print("")
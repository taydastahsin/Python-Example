def hesapla(sayı):
    depo = []
    for i in range(1,sayı):
        if sayı %i ==0:
            depo.append(i)
    return depo
sayı = int (input("sayı giriniz : "))
print(hesapla(sayı))
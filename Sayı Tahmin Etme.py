from  random import randint
tahmin = randint(1,100)
hak =0
print("Sayı Tahmin Oyununa Hoşgeldiniz ")
while hak < 7:
    hak += 1
    a = int(input("Bir sayı yazınız : "))
    if a == tahmin:
        print("Tebrikler Bildiniz {} sayısı tutulan sayıydı.  ".format(tahmin))
        break
    if tahmin > a:
        print("Yanlış cevap tekrar deneyiniz ")
        print("Daha büyük sayı giriniz")
        continue

    if tahmin < a:
        print("Yanlış cevap tekrar deneyiniz ")
        print("Daha küçük sayı giriniz")
        continue






print("Üniversite Başarı Puan HEsaplama programına hoşgeldiniz")
vize = int(input("Vize sınav sonucunu yazınız : "))
final= int(input("Final sınav sonucunu yazınız : "))

hesaplama = vize *0.4 + final*0.6

print("Başarı puanınız : {}".format(hesaplama))

if hesaplama >= 85:
    print("Başarı Harf notunuz : AA ")

elif hesaplama >= 70:
        print("Başarı Harf notunuz : BA ")

elif hesaplama>=60:
    print("Başarı Harf notunuz : BB ")

elif hesaplama>=50:
    print("Başarı Harf notunuz : CB ")

elif hesaplama >= 40:
    print("Başarı Harf notunuz : CC ")

elif hesaplama < 40:
    print("Başarı Harf notunuz : FF ")
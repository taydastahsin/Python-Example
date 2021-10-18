sayı = int(input("Bir sayı giriniz: ")) # Tek-Çift ayrımı yaptırdık.

if(sayı % 2 == 1):
    print("Girdiğiniz {} sayısı Tektir.".format(sayı))

else:
    print("Girdiğiniz {} sayısı Çifttir.".format(sayı))


id = input("Kullanıcı adı: ") # Admin giriş paneli yaptık.
key = input("Şifre: ")

if id == "Tahsin" and key == "1234":
    print("Tahsin bey hoşgeldiniz")
else:
    print("Tekrar Deneyiniz")


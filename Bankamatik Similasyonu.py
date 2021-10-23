id = input("İd Giriniz : ")
şifre=int ( input("Şifrenizi giriniz : "))

if id =="admin" and şifre == 1234 :
    print("Tahsin Bey Hoşgeldiniz ")
    tutar = 2000
    while True:
        print("1-Para Çekme\n2-Para Yatırma\n3-Kart Bİlgileri\n4-Kart İade\n")
        sayı = int (input("Bir seçeneği seçiniz : "))
        if sayı ==1:
            paraç =int(input("Çekiceğiniz Tutarı giriniz : "))
            if paraç>tutar:
                print("Yetersiz bakiye")
                continue
            tutar-=paraç
            print("çektiğiniz tutar {}".format(paraç))
            continue
        elif sayı ==2:
            paray =int (input("Yatırcağınız tutar : "))
            tutar+=paray
            print("yatırdğınız tutar  {}".format(paray))

        elif sayı==3:
            print("AD : Tahsin\nSoyad : Taydaş\nİban : TR45468468468486")
            print("Tutarınız :",tutar)

        elif sayı ==4:
            print("Bizi kulladığınzı için teşekkürlerrrrrrr")
            break





class Sirket ():
    def __init__(self,ad):
        self.ad =ad
        self.calisma= True
    def program(self):
        secim = self.menusecim()

        if secim == 1:
            self.calısanadd()
        elif secim == 2:
            self.calısandel()
        elif secim == 3:
            self.calısantmaas()
        elif secim == 4:
            self.maaslarıver()
        elif secim == 5:
            self.masrafgir()
        elif secim == 6:
            self.gelirgir()


        pass
    def menusecim (self):
        secim= int ( input("{} A.Ş. Hoşgeldiniz \n1-)Çalışan ekle\n2-)Çalışan sil\n3-)Çalışan maaş\n4-)maaslarıver\n5-)masrafgir\n6-)gelirgir\nYapmak istediğiniz seçim :  ".format(self.ad)))
        while secim<1 or secim>6:
            secim = int(input("Lütfen 1-6 arası sayı seçiniz!!!! \n1-)Çalışan ekle\n2-)Çalışan sil\n3-)Çalışan maaş\n4-)maaslarıver\n5-)masrafgir\n6-)gelirgir\nYapmak istediğiniz seçim :  "))
        return secim

    def calısanadd(self):

        id=1
        ad = input("Çalışanın adı : ")
        soyad =input("Çalışanın soyadı : ")
        yas = int (input("Çalışanın yaşı : "))
        cinsiyet = input("Çalışanın cinsiyeti : ")
        maas = int(input("Çalışanın maaşı : "))

        with open("calisanlar.txt","r") as dosya:
            calısanliste = dosya.readline()
        if len(calısanliste) ==0:
            id=1
        else:
            with open("calisanlar.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1
        with open("calisanlar.txt","a+")as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))

    def calısandel(self):
        with open("calisanlar.txt", "r") as dosya:
            calisanlar = dosya.readlines()
        gcalisanlar = []
        for calisan in calisanlar:
            gcalisanlar.append(" ".join(calisan[:-2].split("-")))
        for calisan in gcalisanlar:
            print(calisan)
        secim = int (input("Çıkarmak istediğiniz id giriniz ( 1-{}) : ".format(len(gcalisanlar))))
        while secim<1 or secim>len(gcalisanlar):
             secim = int (input("Lütfen 1-{} arasındaki sayı giriniz : ".format(len(gcalisanlar))))

        calisanlar.pop(secim-1)
        sayac =1
        msayi= len(calisanlar)
        dcalisanlar =[]
        for calisan in calisanlar:
            dcalisanlar.append(str(sayac) + ")"+calisan.split(")")[1])
            sayac+= 1
        with open("calisanlar.txt","w") as dosya:
            dosya.writelines(dcalisanlar)


    def calısantmaas(self):
        with open("calisanlar.txt", "r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int (calisan.split("-")[-1]))
        hesap = input("Ödenecek olan maaşların aylık yada yıllıkmı olduklarını seçiniz(a/y) : ")
        if hesap =="a":
            print("Bu ay ki toplam ödencek maaş {}".format(sum(maaslar)))
        elif hesap =="y":
            print("Bu ay ki toplam ödencek maaş {}".format(sum(maaslar)*12))
        else:
         hesap = input("Ödenecek olan maaşların aylık yada yıllıkmı olduklarını seçiniz(a/y) : ")

    def maaslarıver(self):
        with open("calisanlar.txt", "r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        toplamaas= sum(maaslar)

        with open("butce.txt","r") as dosya:
            tbutce = int (dosya.readlines()[0])
        tbutce-=toplamaas
        with open("butce.txt","w") as dosya:
            dosya.write(str (tbutce))



sirket = Sirket("Tahsin Taydaş")

while sirket.calisma:
    sirket.program()

sirket.menusecim()
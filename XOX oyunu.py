class Oyun():
    def __init__(self):
        self.tahta=[["","",""],["","",""],["","",""]]
        self.durum=True
        self.hamle=0
    def oyna(self):
        if self.hamle %2 ==0:
            self.p1secim()
        else:
            self.p2secim()

        self.hamle +=1

        self.durum = self.oyunkontrol()
        if not self.durum:
            kazanan=""
            if self.hamle %2 ==0:
                kazanan="2"
            else:
                kazanan="1"
            print("Oyun Sonlandı !! Kazanan Oyuncu : {}. oyuncu ".format(kazanan))


    def p1secim(self):
        self.tahtagoster()
        print("Birinci oyuncu ")
        satir=int(input("Satırı giriniz :"))
        while satir<1 or satir>3:
            satir=int(input("1-3 arasında değer seçiniz, Değeriniz : "))
        sutun=int(input("Sütünu giriniz :"))
        while sutun < 1 or sutun > 3:
            sutun = int(input("1-3 arasında değer seçiniz, Değeriniz : "))

        if self.dolumu(satir-1,sutun-1):
            self.p1secim()
        else:
            self.tahta[satir-1][sutun-1] = "X"
    def p2secim(self):
        self.tahtagoster()
        print("İkinci oyuncu ")
        satir = int(input("Satırı giriniz :"))
        while satir < 1 or satir > 3:
            satir = int(input("1-3 arasında değer seçiniz, Değeriniz : "))
        sutun = int(input("Sütünu giriniz :"))
        while sutun < 1 or sutun > 3:
            sutun = int(input("1-3 arasında değer seçiniz, Değeriniz : "))

        if self.dolumu(satir-1, sutun-1):
            self.p1secim()
        else:
            self.tahta[satir-1][sutun-1] = "O"
    def dolumu(self,satir,sutun):
        if self.tahta[satir][sutun] !="" :
            return True
        else:
            return False
    def tahtagoster(self):
        for i in self.tahta:
            print(i)

    def oyunkontrol(self):
        #Yatay Kontrol
        if [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]] == ["X","X","X"] or [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]] == ["O","O","O"]:
            self.tahtagoster()
            return False
        if [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]] == ["X","X","X"] or [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]] == ["O","O","O"]:
            self.tahtagoster()
            return False
        if [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]] == ["X","X","X"] or [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]] == ["O","O","O"]:
            self.tahtagoster()
            return False
        #Dikey Kontrol
        if [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]] == ["X","X","X"] or [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]] == ["O","O","O"]:
            self.tahtagoster()
            return False
        if [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]] == ["X","X","X"] or [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]] == ["O","O","O"]:
            self.tahtagoster()
            return False
        if [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]] == ["X","X","X"] or [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]] == ["O","O","O"]:
            self.tahtagoster()
            return False
        #Çapraz Kontrol
        if [self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]] == ["X","X","X"] or [self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]] == ["O","O","O"]:
            self.tahtagoster()
            return False
        if [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]] == ["X","X","X"] or [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]] == ["O","O","O"]:
            self.tahtagoster()
            return False

        return True





oyun =Oyun()

while oyun.durum:
    oyun.oyna()
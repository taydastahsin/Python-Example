class Araba ():
    def __init__(self,marka,model,fiyat,renk):
      self.gelenmarka = marka
      self.gelenmodel = model
      self.gelenfiyat = fiyat
      self.gelenrenk = renk

    def bilgileriyazdır(self):
       print(self.gelenmarka,self.gelenmodel,self.gelenfiyat,self.gelenrenk)

    def renkdegis (self,renk):
        self.gelenrenk =renk

araba1=Araba("Audi","Sedan",150_000,"Mavi")
araba1.bilgileriyazdır()
araba1.renkdegis("Kırmızı")
araba1.bilgileriyazdır()
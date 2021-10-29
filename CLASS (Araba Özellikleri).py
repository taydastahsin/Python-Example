class Araba (): #Bir sınıf oluşturduk , oluşturduğumuz sınıfın araba özellikleri girerek tanımladık.
    marka = "Renault"
    model = "Cio"
    fiyat = 50_000
    renk = "Mavi"
    def bilgilerigöster (self): # "self" bütün seçenekelri anlamına gelir. Araba özelliklerinin hepsini çağırdık.
        print(self.renk,self.fiyat,self.model,self.marka)

araba =Araba() # "Araba()" sınıfını tanımladık ve "araba" yazınca işlem yapmasını sağladık.

araba.bilgilerigöster() # değişkenden çekilen bilgi

print(Araba.renk) # Sınıf tan çekilen bilgi
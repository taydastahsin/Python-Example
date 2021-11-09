class Personel():
    def __add__(self, other): # "other" yani eklenen objeyi temsil ediyor.
        return 10+other # girilen objenin yapılması gereken işlemi içerir.
    def __len__(self): # len fonksiyonu str yapılı elemanları sayar.Burda çağrıldığında içerisindekini yazdırcaktır.
        for i in range(50):#1-50 arası sayıları yazdırır.
            print(i)
        return 10 #"type none" hatası almamak için koyuldu.

personel =Personel() #"Personel" adlı sınıfı personel adlı değişkene eşitledik.
len(personel) #len fonksiyonunu kullandık
print(personel+100) # add fonksiyonunu kullandık.

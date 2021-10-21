# for saydır in range(101): # 0-100 e kadar bütün sayıları saydırdık.
  #  print(saydır)
# for saydır1 in range(25,101): # 25-100 e kadar bütün sayıları saydırdık.
  #  print(saydır1)
# for saydır2 in range(25,51,5): # 25-51 e kadar 5 er 5er saydırdık.
   #  print(saydır2)

def asal_sayı(sayi):  #def sınıfı oluşrutduk.
     for i in range(2,sayi): # 2-sayi arasındaki değerleri yazdırdık.
          if sayi % i==0: # sayi değişkenin elemanlarının i ye bölümünden 0 kalanları almamasını yaptık.
               return  False
     return True # ayi değişkenin elemanlarının i ye bölümünden kalanların 0 hariç hepsini aldırdık.

sayi =int (input("Sayı giriniz : ")) # kullanıcıya sayı girdirdik.
asal_sayılar = [] # çıkan asal sayıları burda topladık.

for i in range(2,sayi+1): # kullanıcının girdiği sayıyı 1 artırarak yazdırdık.
     if asal_sayı(i): # kullanıcının girdiği sayıyı def e atarak doğrulattık.
          asal_sayılar.append(i) #çıkan asla sayıları ekledik

print(asal_sayılar)
print(len(asal_sayılar))

def saydır(sayı): # "sayı" adında bir değişken tanımlayıp değer tutturuyoruz.
    for i in range(1,sayı+1): # 1 den sayı değişkenin değeri kadar saydırdık.
        print(i)

def topla (*ekler): # ekler değişkeni tanımlayıp içine bir çok eleman girdik.
    topla =0
    for i in ekler:
        topla +=i
    print(topla)

def göster(**see): #elemanları anahtar kelimelerle beraber yazdırmak için kullanırız.
   for kayıt ,islem in see.items():
       print(kayıt,islem)

saydır(10)
topla(10,15,15,12,13,13,15,14)
göster(ad ="tahsin",sınıf =4,yas=23,il ="İstanbul")
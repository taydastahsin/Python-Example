# a= dict() # Dictionary fonksiyonunu gösterir.
# a = {} # Elemanları gruplandırabiliriz.

a = { "süre": [10,15,20,25,30]}
#yaş = {"Tahsin":23,
 #      "Ayşe":24,
  #     "Mehmet":26,
   #    "Hakkı":32,
    #   "Burak":35}

# print(a["süre"]) # a değişkenin "dict" içindeki "süre" değişkenin elemanlarını gösterir.
# print(yaş["Tahsin"]) # yaş değişkeninde isme göre yaşları gösterdi.

# a["süre"].append(35) # a değişkenin içindeki "süre değişkenine eleman ekledik.
# print(a)



ekle = int (input ("Eklemek istediğiniz değeri girin : "))
a["süre"].append(ekle)
print(a)




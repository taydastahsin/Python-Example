# Break Örneği ;
# while True:
  #  sayı = int(input("Sayı giriniz ( Sayı eğer tekse program biter ) : "))
   # if sayı % 2 ==1:
    #    print("Programın Sonu")
     #   break
   # print("Döngü Devam ediyor....")


while True:
    sayı = int(input("Sayı Giriniz ( Sayı eğer tekse programda kalıp tekrar yazıcaksınız) :"))
    if sayı % 2 ==1:
        continue

    print(sayı)
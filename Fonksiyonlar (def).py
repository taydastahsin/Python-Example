def saydır(sayı,yazı): # saydır fonksiyonu oluşturduk.
    for i in range(sayı): # sayı kadar eleman tekrarı yapmasını istedik.
        print(yazı)

# saydır(15,"Tahsin") # kaç kere tekrarı yazıdık sonra neyi tekrar ediceğini belirttik.

a = int(input("Bİrinci sayı : "))
b = int(input("İkinci sayı : "))
def topla():
    print(a+b)
def çıkar():
    print(a-b)
def çarp ():
    print(a*b)
def böl():
    print(a/b)

topla() # Yapmak istediğimiz işlemi çağırıyoruz.
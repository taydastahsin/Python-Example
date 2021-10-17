# "and" : "ve" anlamına gelir . Belirtilen işlemde kullanılan ve bağlacı her iki tarafında doğru olmasını ister.
# "or" : "veya" anlamına gelir. Belirtilen işlemde kullanılan veya bağlacı bir tarafın doğru olmasını ister.
# print(55 == 55 and "Tahsin" == "Tahsin") # Her iki işleminde doğru olması "True" döndürdü.
# print("Tahsin" == "Tahsin" or 3333 == 33) # Bir işlemin doğru olması bile "True" değerini döndürdü.

kbilgiler = ["Tahsin",123456] # Kullanıcı giriş bilgileri

id = input("Kullanıcı adınız: ") # Kullanıcı id isteme
sifre = int (input("Şifrenizi giriniz: ")) # Kullanıcı şifre isteme

kontrol = kbilgiler[0] == id and kbilgiler[1] == sifre  # "ve" bağlacını kullanarak id ve şifreyi eşleştirdik.
# id ve şifre eşleşince "True" değerini döndürüyor.
print(kontrol)

a = int (input("Bİr sayı giriniz: ")) # Kullanıcıya bir sayı girdiriyoruz.

print(a%2 ==0 or a%3 ==0 or a%5 ==0) # Girilen sayı 2,3 veya 5'e bölümünden kalan 0 ise "True" değerini döndürecektir.

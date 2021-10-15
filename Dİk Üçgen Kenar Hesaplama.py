# import math # Matematik modülünü kendisi çağırdı.

a = float (input("Birinci kenar : ")) # Birinci kenarın uzunluğu
b= float (input("İkinci kenar : "))   # İkinci kenarın uzunluğu
# c= math.sqrt( (a*a) +(b*b))         # Birinci kenar ile ikinci keanrın karelerinin toplamının karekökünü alma
c= (a**2 + b**2) ** 0.5
print(c)

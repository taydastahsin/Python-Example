"""
#While döngüsüyle örnek
a = 0
while a <100:
    a+=1
    if (a%2 ==0 and a %3==0):
     print(a)
"""
######################################################
"""
#For döngüsüyle örnek
sayı = []
for i in range(1,1001):
    if i%2==0 and i%3 ==0:
        sayı.append(i)
print(sayı)

"""
######################################################
#List Comp. Örnek
#Tek satır üzerinde bütün işlemleri yapıyoruz.
sayılar = [x for x in range(1,1000) if x %2 ==0 and x %3==0]
print(sayılar)

kişiler = ["Tahsin","Yusuf","Semih","Burak","Enver","Tolga","Yunus","Ertan"]

yazdır = [kişi for kişi in kişiler if "T" in kişi]
print(yazdır)

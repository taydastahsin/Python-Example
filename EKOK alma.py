def ekok(a,b):
    ekok =a*b
    for i in range( ekok,max(a,b),-1):
         if i % a ==0 and i %b ==0:
             ekok = i
    return ekok

sayı1 = int ( input("Birinci sayı : "))
sayı2 = int ( input("İkinci sayı : "))
print(ekok(sayı1,sayı2))

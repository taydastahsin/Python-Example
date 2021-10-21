sayı = int(input("Sayı girin: "))
sayaç =2
asal = []
while sayı >0:
     asal.append(sayı)
     while sayaç<sayı:
         if sayı%sayaç == 0:
             asal.remove(sayı)
             break
         sayaç+=1
     sayaç=2
     sayı-=1
print(asal)
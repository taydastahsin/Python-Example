a = 15
while (a >0 ): # 15 den 0 a kadar olan sayıları yazdırdık.
    #print(a)
    a-=1

a = int(input("Faktoriyel alıncak sayı: "))
b=1
while True:
    b *= a
    a-=1
    if (a == 1):
        break
print(b)
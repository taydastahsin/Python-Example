def ebob(a,b):
    enküçüksayı = min(a,b) # en küçük sayıyı bulur.
    enbüyükbölen=1
    for i in range(1,enküçüksayı+1): # 1 den en küçük sayının +1 fazlasına kadar sayıları saydırır
        if a %i ==0 and b %i ==0 : # a ve b sayılarını i değişkenine tam bölüneni alır.
            enbüyükbölen=i # a ve b ye tam bölünen i elemanını tutar.
    print(enbüyükbölen) # en  son oluşan i elemanını yazdırır.

ebob(70,50)

"""
# Kendi yaptığım
def ebob(a,b):
    if a>b:
        for i in range(1,b+1):
            if a %i ==0 and b%i ==0:
                bölen.append(i)
    if b>a:
        for i in range(1,a+1):
            if a %i ==0 and b%i ==0:
                bölen.append(i)

bölen=[]
ebob(70,50)
print(bölen.pop())
"""


import random

a=random.randint(0,100)
c = int(input("kaç hak istiyorsunuz"))

while c>0:
    c-=1
    b = int(input('bir sayı girininz..'))
    if b<a:
        print("daha büyük bir sayı girniz")

    elif a<b:
        print("daha küçük bir sayı giriniz")

    elif a==b:
        print("tebrikler kazandınız..")
        break

    if c==0:
        print("hakkınız bitmiştir.. Game over")
        print(a)
        break

sayı=int(input("Bir sayı giriniz : "))
b =1
if sayı>0:
    for i in range(1, sayı + 1):
        b *= i
        i -= 1
    print(b)


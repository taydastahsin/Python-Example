def yazdır (sayı): # yazdır adında fonksiyon oluşturduk.
    if sayı%2 ==0: # 2 ye tam bölünüyorsa çifttir dedik.
        print( "Sayı çifttir {}".format(sayı))
    return "sayı tektir"# yukardaki koşul sağlanmadığında direk return yapısındaki ayzı consola gelcek

#print(yazdır(5))# fonksiyonu çağırırken print içinde çağırmak zorundayız yoksa none değeri olan "return" göremeyiz.

def sayıdöndür (first,end):
    for i in range(first,end):
        print(i)
    return "{} sayısından {} sayısına kadar yazdırdık.".format(first,end-1)

print(sayıdöndür(1,11))

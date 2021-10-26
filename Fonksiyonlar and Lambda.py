çift_mi = lambda sayı: sayı%2 ==0 # tek satırda çift olup olmadığını gösterir.

print(çift_mi(35))

def çift_mi(sayı): #"çift_mi" fonksiyonu kurarak çiftmi olduğunu kontrol ettik.
    if sayı%2 ==0:
        print(False)
    return True

çift_mi(18)
# a = 5 in [1,2,3,4,5,6] # burda "in" aracılığıyla "5" elemanının olup olmadığını gördük
# print(a)
# sayılar = (1,2,3,4,5,6,7,8,9,10)
# For döngüsü kullanarak sayılar değişkenşn içindeki elelmanların karesini aldık
# for x in sayılar:
#  print(x ** 2)

a = [(1,2),(5,6),(8,10)]

for x,y in a:
#   print(x[0],x[1]) # 0 ıncı elemanları ve 1 inci elelmanları gösterir.( sadece x değişkeni olunca)
    print(x,y)

metin=input("Lütfen bir metin giriniz: ")
harf=[]
sayi=[]
for i in(metin):
    if not (i in harf):
        harf.append(i)
        sayi.append(1)
    else:
        sayi[harf.index(i)]=sayi[harf.index(i)]+1
print ("Harf","sayi")

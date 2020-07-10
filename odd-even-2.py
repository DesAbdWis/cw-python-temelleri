list = [11, 36, 24, 61, 48, 33, 3]
even = 0
odd = 0
for i in list:
    if i %2 == 0:
        even += 1
    else:
        odd += 1
print ("The number of evens : ", even)
print ("The number of odds : ", odd)

coll=[2,5,9,5,4,7,0,27,35,44,66]
print([i for i in coll if i%2] )
print([i for i in coll if i%2==0] )

example = [11, 2, 24, 61, 48, 33, 3]
even = []
odd = []
for i in example:
    if i%2:  #listedeki cift sayilar
        even.append(i)
    else:
        odd.append(i) #listedeki tek sayilar
x=0
for y in even: #listedeki cift sayilarin toplami
    x +=y
print ('listedeki cift sayilarin toplami: {}'.format(x))
a=0
for b in odd: #listedeki tek sayilarin toplami
    a +=b
print ('listedeki tek sayilarin toplami: {}'.format(a))
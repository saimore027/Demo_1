l1=[10,23,2,45,7,190]
l2=[32,34,1,4,5,2,]
l3=sorted(l1+l2)#wirh repetition
l4=sorted(set(l1)|set(l2))#without repetition
print(l3)
print(l4)

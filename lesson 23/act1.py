import array as arr

basket1={"banana","kiwi","orange","banana","mango"}
basket2={"apple","passion fruit","orange","apple","mango"}
print("basket1:",basket1)
print("basket1:",basket2)
basket1.add("star fruit")

intersectedfruits=basket1.intersection(basket2)

fruitcount=arr.array('i',[2,5,4,3])
print("fruit count array:",fruitcount)
fruitcount.insert(3,5)
fruitcount.append(6)
count=fruitcount.count(3)

fruitcount.reverse()
print("reversed fruit count array:",fruitcount)

print("")
print("========FRUIT BASKET ORGANISER========")
print("basket1:",basket1)
print("basket2:",basket2)
print("intersected fruits:",intersectedfruits)  
print("fruit count:"fruitcount)
print("==========================")
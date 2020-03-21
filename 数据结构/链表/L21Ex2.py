from OrderedListTail import OrderedListTail

data =[5,6,3,1,2,7,9]
olt = OrderedListTail()

for num in data:
    olt.add(num)

olt.remove(6)
olt.remove(1)
olt.remove(9)

for number in olt:
    print(number,end=" ")
print()

from UnorderedListTail import UnorderedListTail

data1 = [1,3,5]
data2 = [2,4,6]
ult = UnorderedListTail()

for i in range(len(data1)):
    ult.add_to_head(data1[i])
    ult.add_to_tail(data2[i])

for number in ult:
    print(number,end=" ")
print()

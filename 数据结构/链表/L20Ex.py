from UnorderedList import UnorderedList
from OrderedList import OrderedList

name_list = ["Gill","Tom","Eduardo","Raffaele","Serena","Bella"]
my_unorderedlist = UnorderedList()
for name in name_list:
    my_unorderedlist.add(name)

for item in my_unorderedlist:
    print(item,end=" ")

print()
my_orderedlist = OrderedList()

for name in name_list:
    my_orderedlist.add(name)

for item in my_orderedlist:
    print(item,end=" ")
print()

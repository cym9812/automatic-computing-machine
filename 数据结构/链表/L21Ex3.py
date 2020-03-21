from LinkedListDLL import LinkedListDLL

def test_DoublyLinkedList():
    my_list = LinkedListDLL()
    for x in range(1,10):
        my_list.add_to_head(x)
    print(my_list.size())
    
    for x in range(1,9):
        my_list.remove_from_tail()
    print()
    print(my_list.size())
    
test_DoublyLinkedList()

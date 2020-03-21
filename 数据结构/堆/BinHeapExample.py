from BinHeap import BinHeap

def main():
	heap = BinHeap([10, 5, 2, 9, 3, 6])
	heap.print()
	min = heap.del_min()
	print("delete min=",min)
	heap.print()
	min = heap.del_min()
	print("delete min=",min)
	heap.print()
	min = heap.del_min()
	print("delete min=",min)
	heap.print()

main()

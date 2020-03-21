from RefBinaryTree import RefBinaryTree

def main():
	tree = RefBinaryTree(9)
	tree.insert_left(3)
	tree.insert_right(6)
	print(tree)
	print("\nChange root value and add subtrees:")
	
	tree.set_value(0)
	tree.get_left_subtree().insert_right(7) 
	tree.get_right_subtree().insert_right(2)
	print(tree)

main()
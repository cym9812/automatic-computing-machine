from ListBinaryTree import ListBinaryTree

def preorder(tree):
	if(tree!=None):
		print(tree.get_value(), end=" ")	
		preorder(tree.get_left_subtree())
		preorder(tree.get_right_subtree())

def inorder(tree):
	if(tree!=None):
		inorder(tree.get_left_subtree())
		print(tree.get_value(), end=" ")	
		inorder(tree.get_right_subtree())

def postorder(tree):
	if(tree!=None):
		postorder(tree.get_left_subtree())
		postorder(tree.get_right_subtree())
		print(tree.get_value(), end=" ")	

def main():
	tree = ListBinaryTree(55)
	tree.insert_left(4)
	tree.insert_right(6)
	tree.set_value(tree.get_value() + 4)
	print("1.", tree.get_value())	
	right = tree.get_right_subtree()
	left = tree.get_left_subtree()
	left.insert_left(7) 
	right.insert_right(2)
	right.insert_tree_left(ListBinaryTree(5))     
	print("2.", tree.get_right_subtree().get_left_subtree().get_value())

	print(tree)
	print("\nPreorder:", end=" ")
	preorder(tree)
	print("\nInorder:", end=" ")
	inorder(tree)
	print("\nPostorder:", end=" ")
	postorder(tree)
	
main() 


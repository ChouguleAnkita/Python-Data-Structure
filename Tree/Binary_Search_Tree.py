# *************Binary Search Tree**********************

class BST:
#intialize key to root node=================
	def __init__(self,key):
		self.key=key
		self.lchild=None
		self.rchild=None

#Insert node in tree==========================
	def insert(self,data):
		if self.key is None:   #if tree is empty 
			self.key=data
			return
		if self.key==data:     #To avoid duplicate data
			return
		if data<self.key:      
			if self.lchild:    #lchild is not None i.e true
				self.lchild.insert(data)  #function calls itself i.e recursion
			else:
				self.lchild=BST(data)  #it creates new node for adding to tree
		else:
			if self.rchild:          #rchild is not None i.e true
				self.rchild.insert(data)
			else:
				self.rchild=BST(data)
#Search given node==================================
	def search(self,data):
		if self.key==data:
			print("Node is found")
			return
		if data<self.key:
			if self.lchild:
				self.lchild.search(data) #function calls itself i.e recursion
			else:
				print("Given node is not present in tree!") 
		else:
			if self.rchild:
				self.rchild.search(data)
			else:
				print("Given node is not present in tree!") 

#Pre-order Traversal==================================
	def preorder(self):            # root,lchild,rchild
		print(self.key,end=" ")
		if self.lchild:
			self.lchild.preorder()  #function calls itself i.e recursion
		if self.rchild:
			self.rchild.preorder()

#In-order Traversal==================================
	def inorder(self):               #lchild,root,rchild
		if self.lchild:
			self.lchild.inorder()     #function calls itself i.e recursion
		print(self.key,end=" ")
		if self.rchild:
			self.rchild.inorder()

#Post-order Traversal==================================
	def postorder(self):       #lchild,rchild,root
		if self.lchild:
			self.lchild.postorder()  #function calls itself i.e recursion
		if self.rchild:
			self.rchild.postorder()
		print(self.key,end=" ")

#delete given node from tree===========================
	def delete(self,data,rkey):
		if self.key is None:
			print("Tree is Empty")
			return
		if data<self.key:
			if self.lchild:
				self.lchild=self.lchild.delete(data,rkey)    #function calls itself i.e recursion
			else:
				print("Given node is not present in the tree")
		elif data>self.key:
			if self.rchild:
				self.rchild=self.rchild.delete(data,rkey)
			else:
				print("Given node is not present in the tree")
		else:
			if self.lchild is None:
				temp=self.rchild
				if data==rkey:            #if root node has only one child i.e right child
					self.key=temp.key
					self.lchild=temp.lchild
					self.rchild=temp.rchild
					return
				self=None
				return temp
			if self.rchild is None:
				temp=self.lchild
				if data==rkey:           #if root node has only one child i.e left child
					self.key=temp.key
					self.lchild=temp.lchild
					self.rchild=temp.rchild
					return
				self=None
				return temp

			node =self.rchild      #when given node having 2 childs         
			while node.lchild:
				node=node.lchild
			self.key=node.key
			self.rchild=self.rchild.delete(node.key,rkey)
		return self

#Smallest node from the tree=========================
	def min_node(self):
		current=self
		while current.lchild:
			current=current.lchild
		print("Smallest node from the tree is=",current.key)

#Largest node from the tree=========================
	def max_node(self):
		current=self
		while current.rchild:
			current=current.rchild
		print("Largest node from the tree is=",current.key)

#************************************************************
#Total Number of nodes in tree
def count(node):
	if node is None:
		return 0
	return 1+count(node.lchild)+count(node.rchild)

#************************************************************
#Creating object of class BST
root=BST(None)

while True:
	print("""Select Operation Perform On Tree: 
		1.Insert 
		2.Search
		3.Delete
		4.PreOrder Traversal
		5.InOrder Traversal 
		6.PostOrder Traversal 
		7.Small Node
		8.Large Node
		9.Total Nodes
		10.Quit :-""")

	ch=int(input())
	if(ch==1):
		n=int(input("Enter number of Nodes for insert="))
		for i in range(n):
			x=int(input("Enter Node="))
			root.insert(x)
	elif(ch==2):
		x=int(input("Enter Node for Search="))
		root.search(x)
	elif(ch==3):
		x=int(input("Enter Node for delete="))
		if count(root)>1:     #if root node is not leaf node
			root.delete(x,root.key)
			print("After deleting node")
			root.preorder()
			print()
		else:                #if root node is leaf node i.e only 1 node in tree
			print("Can't delete node")
	elif(ch==4):
		print("PreOrder Traversal")
		root.preorder()
		print()
	elif(ch==5):
		print("InOrder Traversal")
		root.inorder()
		print()
	elif(ch==6):
		print("PostOrder Traversal")
		root.postorder()
		print()
	elif(ch==7):
		root.min_node()
	elif(ch==8):
		root.max_node()
	elif(ch==9):
		print("Total Number of nodes in tree",count(root))	
	else:
		break

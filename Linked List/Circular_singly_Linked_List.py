# ****************Circular Linked List********************************

class Node:                   #Creating Node
	def __init__(self,data):
		self.data=data
		self.ref=None

#Class Circular Singly Linked List*************************************************************
class Circular_SLL:
	def __init__(self):
		self.head=None

#printing data of each node===========================================================================
	def printLL(self):
		if self.head is None:#checking LL is empty
			print("Circular Linked List is empty!!!")
		else:
			print(self.head.data,"-->",end="") 
			n=self.head.ref
			if n is not None: #If LL contain more than one node
				while n is not self.head:
					print(n.data,"-->",end="")
					n=n.ref
			print()

#Insertion at begin in CSLL===========================================================================
	def add_begin(self,data):
		new_node=Node(data)
		if self.head is None: #If LL is empty
			self.head=new_node			
		else:
			if self.head.ref is None: #If LL contain only one node
				self.head.ref=new_node
			else:
				n=self.head
				while n.ref is not self.head:#going to last node
					n=n.ref
				n.ref=new_node

			new_node.ref=self.head
			self.head=new_node

#Insertion at begin in CSLL===========================================================================
	def add_end(self,data):
		new_node=Node(data)
		if self.head is None: #If LL is empty
			self.head=new_node		
		else:
			if self.head.ref is None: #If LL contain only one node
				self.head.ref=new_node
			else:
				n=self.head
				while n.ref is not self.head: #go to last node
					n=n.ref
				n.ref=new_node

			new_node.ref=self.head

#Insertion after given value(x) in CSLL===========================================================================
	def add_after(self,data,x):
		if self.head is None:#checking LL is empty
			print("Circular Linked List is empty can't find x.")
			return
		if self.head.ref is None: #If LL contain only 1 node
			if x==self.head.data:  #and if x is found at 1 node
				new_node=Node(data)
				new_node.ref=self.head
				self.head.ref=new_node
			else:
				print("x not found can't add node")
		else:                   
			n=self.head
			while n.ref is not self.head:#Go to given node
				if x==n.data:        #if x found at middle
					break
				n=n.ref

			if(n.data==x):        #this condition mainly for checking x at last node 
				new_node=Node(data)
				new_node.ref=n.ref
				n.ref=new_node
			else:
				print("x not found can't add node")

#Deletion at begin in CSLL===========================================================================
	def delete_begin(self):
		if self.head is None:
			print("Empty LL can't delete node")
			return
		if self.head.ref is None: #If LL contain only one node
			self.head=None
		else:
			n=self.head
			while n.ref is not self.head: #Go to last node
				n=n.ref

			self.head=self.head.ref
			n.ref=self.head

#Deletion at end in CSLL===========================================================================
	def delete_end(self):
		if self.head is None:
			print("Empty LL can't delete node")
			return
		if self.head.ref is None: #If LL contain only one node
			self.head=None
		else:
			n=self.head
			while n.ref.ref is not self.head: #Go to 2nd last node
				n=n.ref

			n.ref=self.head

#Deletion by value(x) in CSLL===========================================================================
	def delete_by_value(self,x):
		if self.head is None:
			print("Empty LL can't delete node")
			return
		if self.head.ref is None: #If LL contain only one node
			if(x==self.head.data):
				self.head=None
			else:
				print("X Not Present")
			return
		else:
			if self.head.data==x: #If x found at 1st node
				n=self.head
				while n.ref is not self.head: #Go to last node
					n=n.ref

				self.head=self.head.ref
				n.ref=self.head
				return

			n=self.head
			flag=0
			while n.ref.ref is not self.head: #Go to previous node of x
				if x==n.ref.data:
					flag=1
					break
				n=n.ref
			if n.ref.data==x and n.ref.ref==self.head:
				n.ref=self.head
			elif flag==1:
				n.ref=n.ref.ref
			else:
				print("X Not Present")

#Creating object of class Circular_SLL**************************************************************
cSLL=Circular_SLL()
cSLL.printLL()        #Circular Linked List is empty!!!

cSLL.add_begin(200)
cSLL.add_begin(100)
cSLL.add_end(300)
cSLL.add_end(500)
cSLL.add_after(400,300)

cSLL.printLL() #100 -->200 -->300 -->400 -->500 -->

cSLL.delete_begin()
cSLL.delete_end()

cSLL.printLL() #200 -->300 -->400 -->

cSLL.delete_by_value(300)
cSLL.printLL() #200 -->500 -->

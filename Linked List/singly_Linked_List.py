# ****************Singly Linked List********************************

class Node:                        #creating Node
	def __init__(self,data): 
		self.data=data
		self.ref=None

#Class LinkedList******************************************************************
class LinkedList:                  #For Linking Node
	def __init__(self):
		self.head=None
   
#printing data of each node==============================================================
	def print_LL(self):             #Traversing
		if self.head is None:
			print("Linked List is Empty!")
		else:
			n=self.head
			while n is not None:
				print(n.data,"-->",end=" ")
				n=n.ref
			print()

#Insertion at begining/Start of LL==============================================================
	def add_begin(self,data):
		new_node=Node(data)
		if self.head is None:#checking LL is empty or not
			self.head=new_node
		else:
			new_node.ref=self.head
			self.head=new_node

#Insertion at end of LL==============================================================
	def add_end(self,data):
		new_node=Node(data)
		if self.head == None:#checking LL is empty or not
			self.head=new_node
		else:
			n=self.head
			while n.ref is not None: #Going to last node
				n=n.ref
			n.ref=new_node

#Insertion after given node(x)==============================================================
	def add_after(self,data,x):
		if self.head is None:
			print("Linked List is empty can't find x")
			return
		n=self.head
		while n is not None: #Go to given node
			if x==n.data: 
				break
			n=n.ref
		if n is None: #Checking if n is none i.e x is not present in entire list 
			print("X is not Present in Linked List")
		else: #if x present
			new_node=Node(data)
			new_node.ref=n.ref
			n.ref=new_node

#Insertion before Given node(x)==============================================================
	def add_before(self,data,x):
		if self.head is None:
			print("Linked List is empty can't find x")
			return

		new_node=Node(data)
		if self.head.data==x: #checking given node is first node
			new_node.ref=self.head
			self.head=new_node
			return

		n=self.head
		while n.ref is not None: #Go to previous node of given node
			if n.ref.data==x:
				break
			n=n.ref
		if n.ref is None: #Checking if n is none i.e x is not present in entire list 
			print("X is not Present in Linked List")
		else:
			new_node.ref=n.ref
			n.ref=new_node

#Insertion in empty LL==============================================================
	def insert_empty(self,data):
		if self.head is None:
			new_node=Node(data)
			self.head=new_node
		else:
			print("Linked List is not Empty!!!")

#Deletion at begin==============================================================
	def delete_begin(self):
		if self.head is None:
			print("Linked List is empty so we cant delete node")
		else:
			self.head=self.head.ref

#Deletion at end==============================================================
	def delete_end(self):
		if self.head is None:
			print("Linked List is empty so we cant delete node")
		else:
			n=self.head
			while n.ref.ref is not None:
				n=n.ref
			n.ref=None

#Deletion by given value(x)==============================================================
	def delete_by_value(self,x):
		if self.head is None:
			print("Linked List is empty so we cant delete node")
			return
		if self.head.data==x:
			self.head=self.head.ref
		else:
			n=self.head
			while n.ref is not None:
				if x==n.ref.data:
					break
				n=n.ref
			if n.ref is None:
				print("X is not Present in Linked List")
			else:
				n.ref=n.ref.ref

#Creating object of class LinkedList===========================================================================
LL1=LinkedList()
LL1.print_LL()  #Linked List is Empty!

LL1.add_begin(20) 
LL1.add_begin(10)
LL1.add_end(30)
LL1.add_end(50)
LL1.add_after(60,50)
LL1.add_before(40,50)

LL1.print_LL() #10 --> 20 --> 30 --> 40 --> 50 --> 60 -->

# LL1.insert_empty(30) #Linked List is not Empty!!!
LL1.delete_begin()
LL1.delete_end()

LL1.print_LL()#20 --> 30 --> 40 --> 50 -->

LL1.delete_by_value(30)
LL1.print_LL() #20 --> 40 --> 50 -->
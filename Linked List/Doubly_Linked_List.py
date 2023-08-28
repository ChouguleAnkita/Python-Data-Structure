# ****************Doubly Linked List********************************

class Node:                    #Creating Node
	def __init__(self,data):
		self.data=data
		self.nref=None
		self.pref=None
		
#Class Doubly Linked List*************************************************************************************
class DoublyLL:                #For Linking Node
	def __init__(self):
		self.head=None

#printing data of each node==============================================================
	def printLL_forword(self):        #Traversing
		if self.head is None:
			print("Linked List is Empty!!!")
		else:
			n=self.head
			while n is not None:
				print(n.data,"-->",end=" ")
				n=n.nref
			print()

#printing data of each node in reverse==============================================================
	def printLL_reverse(self):
		if self.head is None:
			print("Linked List is Empty!!!")
		else:
			n=self.head
			while n.nref is not None: #Go to last node
				n=n.nref
			while n is not None:
				print(n.data,"-->",end=" ")
				n=n.pref
			print()

#Insertion at begin in DLL==============================================================
	def add_begin(self,data):
		new_node=Node(data)
		if self.head is None: #checking LL is empty or not
			self.head=new_node
		else:
			new_node.nref=self.head
			self.head.pref=new_node
			self.head=new_node

#Insertion at begin in DLL==============================================================
	def add_end(self,data):
		new_node=Node(data)
		if self.head is None:#checking LL is empty or not
			self.head=new_node
		else:
			n=self.head
			while n.nref is not None: #Go to last node
				n=n.nref
			n.nref=new_node
			new_node.pref=n

#Insertion after given node(x) in DLL==============================================================
	def add_after(self,data,x):
		if self.head is None:
			print("Linked List is empty can't find x")
			return
		n=self.head
		while n is not None:#Go to given node
			if x==n.data:
				break;
			n=n.nref
		if n is None:
			print("X is not Present in Linked List")
		else:
			new_node=Node(data) #creating new node
			new_node.nref=n.nref
			new_node.pref=n
			if n.nref is not None:#if given node is not last node
				n.nref.pref=new_node
			n.nref=new_node

#Insertion Given given node(x) in DLL==============================================================
	def add_before(self,data,x):
		if self.head is None:
			print("Linked List is empty can't find x")
			return
		n=self.head
		while n is not None: #Go to given node
			if x==n.data:
				break
			n=n.nref
		if n is None:
			print("X is not Present in Linked List")
		else:
			new_node=Node(data)
			new_node.nref=n
			new_node.pref=n.pref
			if n.pref is not None: #if given node is not first node
				n.pref.nref=new_node
			else:                 #if given node is first node
				self.head=new_node
			n.pref=new_node

#Deletion at begin of DLL======================================================================
	def delete_begin(self):
		if self.head is None:
			print("Linked List is Empty Can't delete")
			return
		if self.head.nref is None: #Checking LL contain only element
			self.head=None
			print("DLL is Empty after deleting node")
		else:
			self.head=self.head.nref
			self.head.pref=None

#Deletion at end of DLL======================================================================
	def delete_end(self):
		if self.head is None:
			print("Linked List is Empty Can't delete")
			return
		if self.head.nref is None: #Checking LL contain only one element
			self.head=None
			print("DLL is Empty after deleting node")
		else:
			n=self.head
			while n.nref is not None: #go to last node
				n=n.nref
			n.pref.nref=None

#Deletion by value in DLL======================================================================
	def delete_by_value(self,x):
		if self.head is None:       #Checking LL is empty
			print("Linked List is Empty Can't delete")
			return
		if self.head.nref is None: #Checking LL contain only one element
			if x==self.head.data: #if yes checking x matches to that node data
				self.head=None    
			else:                
				print("X is not Present in Linked List")
			return

		if self.head.data==x: #Checking x matches to first node data
			self.head=self.head.nref
			self.head.pref = None
			return
		else:           #if not matches to first node data
			n=self.head
			while n.nref is not None: #go to given node
				if x==n.data:
					break
				n=n.nref
			if n.nref is not None: #if given node is not last node
				n.pref.nref=n.nref
				n.nref.pref=n.pref
			else:                 #if given node is last node
				if n.data==x: 
					n.pref.nref=None
				else:
					print("X is not Present in DLL")

#Creating object of class DoublyLL========================================================================================
dLL1=DoublyLL()
# dLL1.printLL_forword()
# dLL1.printLL_reverse()
dLL1.add_begin(20)
dLL1.add_begin(10)
dLL1.add_end(30)
# dLL1.add_after(50,30)
# dLL1.add_before(40,50)
# dLL1.delete_begin()
# dLL1.delete_end()
dLL1.delete_by_value(30)
dLL1.printLL_forword()
dLL1.printLL_reverse()


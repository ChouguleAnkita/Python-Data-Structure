#========*Stack*====Using Singly Linked List==========

class Node:                        #creating Node
	def __init__(self,data): 
		self.data=data
		self.ref=None

#Class Stack******************************************************************
class Stack:                  #For Linking Node
	def __init__(self):
		self.head=None

#printing data of each node(printing stack element)==============================================================
	def printStack(self):             #Traversing
		if self.head is None:
			print("Stack is Empty!")
		else:
			n=self.head
			while n is not None:
				print(n.data,"-->",end=" ")
				n=n.ref
			print()

#Top of stack ===========================================================
	def top_of_Stack(self):            
		if self.head is None:
			print("Stack is Empty!")
		else:
			print("Top Element of Stack=",self.head.data)

#Insertion at begining/Start(push into stack)==============================================================
	def push_element(self,data):
		new_node=Node(data)
		if self.head is None:#checking stack is empty or not
			self.head=new_node
		else:
			new_node.ref=self.head
			self.head=new_node

#Deletion at begin(pop from stack)==============================================================
	def pop_element(self):
		if self.head is None:
			print("Stack is empty so we cant delete node")
		else:
			print(self.head.data,"removed from stack")
			self.head=self.head.ref

#Creating object of class Stack===========================================================================
stack=Stack()
while True:
	print("\nSelect Operation: \n1.add \n2.remove \n3.top of stack \n4.show \n5.Quit :-")
	ch=int(input())
	if(ch==1):
		ele=int(input("Enter Element to push="))
		for x in range(ele):
			n=input("Enter Element")
			stack.push_element(n)
	elif(ch==2):
		stack.pop_element()
	elif(ch==3):
		stack.top_of_Stack()
	elif(ch==4):
		stack.printStack()
	else:
		break

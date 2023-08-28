#========*Queue*====Using Singly Linked List==========

class Node:                        #creating Node
	def __init__(self,data): 
		self.data=data
		self.ref=None

#Class Queue******************************************************************
class Queue:                  #For Linking Node
	def __init__(self):
		self.head=None

#printing data of each node(printing queue element)==============================================================
	def printQueue(self):             #Traversing
		if self.head is None:
			print("Queue is Empty!")
		else:
			n=self.head
			while n is not None:
				print(n.data,end="  ")
				n=n.ref
			print()

#Insertion at begining(add into queue)==============================================================
	def enqueue(self,data):
		new_node=Node(data)
		if self.head is None:#checking queue is empty or not
			self.head=new_node
		else:
			new_node.ref=self.head
			self.head=new_node

#Deletion at end(remove element from queue)==============================================================
	def dequeue(self):
		if self.head is None:
			print("Queue is empty so we cant delete node")
			return
		if self.head.ref is None:
			print(self.head.data,"removed from Queue")
			self.head=None
		else:
			n=self.head
			while n.ref.ref is not None:
				n=n.ref
			print(n.ref.data,"removed from Queue")
			n.ref=None

#Front and rear element of Queue==============================================================
	def front_rear_element(self):
		if self.head is None:
			print("Queue is empty")
			return
		if self.head.ref is None:
			print("Front element of Queue",self.head.data)
			print("Rear(Last) element of Queue",self.head.data)
		else:
			n=self.head
			while n.ref.ref is not None:
				n=n.ref
			print("Front element of Queue",n.ref.data)
			print("Rear(Last) element of Queue",self.head.data)


#Creating object of class Stack===========================================================================
queue=Queue()
while True:
	print("\nSelect Operation: \n1.add \n2.remove \n3.front_rear_element \n4.show \n5.Quit :-")
	ch=int(input())
	if(ch==1):
		ele=int(input("Enter Element to add="))
		for x in range(ele):
			n=input("Enter Element")
			queue.enqueue(n)
	elif(ch==2):
		queue.dequeue()
	elif(ch==3):
		queue.front_rear_element()
	elif(ch==4):
		queue.printQueue()
	else:
		break

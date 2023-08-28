#========*Queue*=========== Using class deque from collection module=============

import collections

queue=collections.deque()
#append->popleft and appendleft->pop methods of class deque from collection module used for queue operations

#=======Enqueue Operation================================================
def enqueue():
	element=int(input("Enter Element to enqueue"))
	queue.append(element)      #Here we can write appendleft instead of append
	print(element," added into queue")

#=======Dequeue Operation==================
def dequeue():
	if not queue:
		print("queue is Empty")
	else:
		e=queue.popleft()      #Here we can write pop instead of popleft
		print(e,"removed from queue")

#=======Front of queue==================
def front_element():
	if not queue:
		print("queue is Empty")
	else:
		print("front_element of queue=",queue[0])

#=======Rear(last) of queue==================
def rear_element():
	if not queue:
		print("queue is Empty")
	else:
		print("last_element of queue=",queue[-1])

#=======show queue Operation==================
def show():
	print(queue)
	
while True:
	print("Select the Operation 1.add 2.remove 3.front_element 4.rear_element 5.show 6.Quit")
	ch=int(input())
	if(ch==1):
		enqueue()
	elif(ch==2):
		dequeue()
	elif(ch==3):
		front_element()
	elif(ch==4):
		rear_element()
	elif(ch==5):
		show()
	else:
		break



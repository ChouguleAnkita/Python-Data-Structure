#========*Queue*====Using List_insertMethod==========
queue=[]
#=======Enqueue Operation==================
def enqueue():
	element=int(input("Enter Element to enqueue"))
	queue.insert(0,element)
	print(element," added into queue")

#=======Dequeue Operation==================
def dequeue():
	if not queue:
		print("queue is Empty")
	else:
		e=queue.pop()
		print(e,"removed from queue")

#=======front of queue==================
def front_element():
	if not queue:
		print("queue is Empty")
	else:
		print("front_element of queue=",queue[-1])

#=======Rear(last) of queue==================
def rear_element():
	if not queue:
		print("queue is Empty")
	else:
		print("last_element of queue=",queue[0])

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


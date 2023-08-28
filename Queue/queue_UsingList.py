#========*Queue*====Using List==========

queue=[]
#=======Enqueue Operation==================
def enqueue():
	element=int(input("Enter Element to enqueue"))
	queue.append(element)
	print(element," added into queue")

#=======Dequeue Operation==================
def dequeue():
	if not queue:
		print("queue is Empty")
	else:
		e=queue.pop(0)
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
	print("Select the Operation \n1.add \n2.remove \n3.front_element \n4.rear_element \n5.show \n6.Quit")
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


#========*Queue*=======Using Queue class from queue module============

import queue

queue=queue.Queue(maxsize=2)
#=======enqueue Operation==================
def enqueue():
	if not queue.full():
		element=int(input("Enter Element to enqueue"))
		queue.put_nowait(element)
		print(element," added into queue")
	else:
		print("queue size=",queue.qsize())
		print("queue is Full Can't enqueue")

#=======dequeue Operation==================
def dequeue():
	if queue.empty():
		print("queue is Empty,can't remove")
	else:
		e=queue.get_nowait()
		print(e,"removed from queue")

#=======show queue Operation==================
def display():
	print(queue)

while True:
	print("Select Operation: \n1.add \n2.remove \n3.Quit :-")
	ch=int(input())
	if(ch==1):
		enqueue()
	elif(ch==2):
		dequeue()
	else:
		break

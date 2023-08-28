#=======*Stack*======Using LifoQueue class from queue module========

import queue
stack=queue.LifoQueue(maxsize=1)
#=======Push Operation==================
def push():
	if not stack.full():
		element=int(input("Enter Element to push"))
		stack.put_nowait(element)
		print(element," added into stack")
	else:
		print("Stack size=",stack.qsize())
		print("Stack is Full Can't Push")

#=======Pop Operation==================
def pop_element():
	if stack.empty():
		print("Stack is Empty,can't remove")
	else:
		e=stack.get_nowait()
		print(e,"removed from stack")

#=======Top of Stack==================
def top_element():
	if stack.empty():
		print("Stack is Empty")
	else:
		print("Top of Stack=",stack[-1])

#=======show stack Operation==================
def display():
	print(stack)
	
while True:
	print("Select Operation: \n1.add \n2.remove \n3.top of stack \n4.show \n5.Quit :-")
	ch=int(input())
	if(ch==1):
		push()
	elif(ch==2):
		pop_element()
	elif(ch==3):
		top_element()
	elif(ch==4):
		display()
	else:
		break

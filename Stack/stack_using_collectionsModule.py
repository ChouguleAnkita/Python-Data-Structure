#=====*Stack*===Using class deque from collection module========

import collections

stack=collections.deque()
print(stack)

#=======Push Operation==================
def push():
	element=int(input("Enter Element to push"))
	stack.append(element)
	print(element," added into stack")

#=======Pop Operation==================
def pop_element():
	if not stack:
		print("Stack is Empty")
	else:
		e=stack.pop()
		print(e,"removed from stack")

#=======Top of Stack==================
def top_element():
	if not stack:
		print("Stack is Empty")
	else:
		print("Top of Stack=",stack[-1])

#=======show stack Operation==================
def display():
	print(stack)
#============================
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
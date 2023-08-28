#========*Stack*====Using List==========

stack=[]
#=======Push Operation==================
def push():
	element=input("Enter Element to push")
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
		print("Size of Stack=",len(stack))
		print("Top of Stack=",stack[-1])


#=======show stack Operation==================
def display():
	print(stack)
	
while True:
	print("""Select Operation: 
		1.add 
		2.remove 
		3.top of stack 
		4.show 
		5.Quit :-""")
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
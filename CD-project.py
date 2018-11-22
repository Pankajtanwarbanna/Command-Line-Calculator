###########################################################

# Project Name - Command Line Calculator
# Project Author - Pankaj Tanwar &  Rahul Jangir

##############################  Program Start  #########################
# Used python3 libraries
import re
import sys
import math
# List of operators
operator = ['+','-','*','/','^']

# Solving equation part
def calculation(i ,operator):
	#print(SplitList)

	if(operator == '+'):
		SplitList[i-1] = str(int(SplitList[i-1]) + int(SplitList[i+1]))
	
	if(operator == '-'):
		SplitList[i-1] = str(int(SplitList[i-1]) - int(SplitList[i+1]))
		
	if(operator == '*'):
		SplitList[i-1] = str(int(SplitList[i-1]) * int(SplitList[i+1]))
		
	if(operator == '/'):
		SplitList[i-1] = str(int(int(SplitList[i-1]) / int(SplitList[i+1])))
		
	if(operator == '^'):
		SplitList[i-1] = str(int(SplitList[i-1]) ** int(SplitList[i+1]))
		
	del SplitList[i]
	del SplitList[i]
	

# Main Solve bracket function
def SolveBracket(m,n):
	p = len(SplitList[m:n+1])

	# Solving the equation in a bracket
	while(p != 1):
		maxPrecedanceIndex = 0
		for i in range(m,m+p):
			if(SplitList[i] in PrecedanceOrder): 

				if(maxPrecedanceIndex == 0):
					maxPrecedanceIndex = i
					operator = SplitList[i]
				else:
					if(PrecedanceOrder[SplitList[i]] > PrecedanceOrder[SplitList[maxPrecedanceIndex]]):
						maxPrecedanceIndex = i
						operator = SplitList[i]		
		try:
			calculation(maxPrecedanceIndex,operator)	
			p = p-2
		except ValueError:
			print("Incorrect Expression")
			sys.exit()
			

# Finding brackets in expression
def mainFunction():
	# Solving all brackets
	while(len(SplitList) != 1):
		#print(SplitList)
		openParenthesis = -1;
		closeParenthesis = -1;
		for i in range(len(SplitList)):
			if(SplitList[i] == '('):
				openParenthesis = i
			elif(SplitList[i] == ')'):
				closeParenthesis = i
				
			if(openParenthesis != -1 and closeParenthesis != -1):
				break

		if(openParenthesis == -1 and closeParenthesis == -1):
			SolveBracket(0,len(SplitList)-1)
		else:
			#print(SplitList)
			del SplitList[openParenthesis]
			del SplitList[closeParenthesis-1]
			SolveBracket(openParenthesis,closeParenthesis-2)

	
	# Print the result
	print(">>> " + str(SplitList[0]))
	
# welcome Screen
print("Welcome to Command Line Calculator")
command = int(input("Please select -\n1. Solve Quadratic Equation\n2. Solve Mathematical Equation\n3. Exit\n>>> "))


if(command == 1):
	# Solving Quadratic equation
	equa = input("Enter value of a,b and c\n>>> ")
	# Spliting the expression
	quad = equa.split()
	a = int(quad[0])
	b = int(quad[1])
	c = int(quad[2])

	x = b**2 - 4*a*c
	if(x>0):
		res1 = -b + math.sqrt(x)
		res2 = -b - math.sqrt(x)
		
		print(res1/(2*a))
		print(res2/(2*a))
			
	elif(x==0):
		print(-b/(2*a))
	else:
		print("Solution does not exist!")
		
elif(command == 2):

	# Define precedance order 
	PrecedanceOrder = {
		"-" : 1,
		"+" : 2,
		"/" : 4,
		"*" : 3,
		"^" : 5
	}
	# Ask for precedance order 
	ip = int(input("Want to change Precedence order? hit 1 otherwise enter 2\n>>> "))
	
	if(ip == 1):
		for i in operator:
			# Precedance order change input
			order = int(input("What should be precedance order of "+ i+ "\n>>> "))
			PrecedanceOrder[i] = order

		# Taking expression as input
		expr = input("Good! Please enter an expression!\n>>> ")

		# Split string into pieces using regular expression
		SplitList = re.findall('[+-/*^//()]|\d+',expr)
		#print(SplitList)
		mainFunction()
			
	else:
		# Taking expression as input
		expr = input("Good! Please enter an expression!\n>>> ")

		# Split string into pieces using regular expression
		SplitList = re.findall('[+-/*^//()]|\d+',expr)
		#print(SplitList)
		mainFunction()
	
elif(command == 3):
	# Exit command
	print("Thank you!")
else:
	# Invalid command
	print("Invalid Input")
	
	
###################### Program End #################################################
	



	
		





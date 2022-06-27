import random
class functions:
	'''
	negativeAddition: Simple addition with positive and negative numbers
	negativeSubtraction: Simple Subtraction with positive and negative nmbers
	negativeDivision: Dividing positive and negative numbers
	negativeMultiplication:Multplying positive and negative numbers
	negativeBidmas:Rules of Operations with negative numbers'''
	
	@staticmethod
	def do_negativeAddition(line):
		'''negative addition --|++ = + & +-|-+ = -'''
		number1 = random.randint(-9999,9999)
		number2 = random.randint(-9999,9999)
		ans1 = number1+number2
		ans=(f'{number1} + {number2} = ')
		return(ans,ans1)
	@staticmethod
	def do_negativeMultiplication(line):
		'''multiplications by 100
		can be broken down
		e.g. 230*200 == 230*100*100
		12*200 == 12*20*100'''
		number1 = random.randint(-9990,9990)
		number2 = random.randint(-990,990)
		
		ans1 = number1*number2
		questions = [f'{number1} X {number2} =', f'what is the product of {number1} by {number2}: ']
		ans = (random.choice(questions)) 
		return(ans,ans1)
		
	@staticmethod
	def do_negativeSubtraction(line):
		'''simple subtraction'''
		numbers = random.randint(-9999,9999),random.randint(-9999,9999)
		
		ans1 = max(numbers)-min(numbers)
		questions = [f'{max(numbers)} - {min(numbers)} = ',
		f"find the difference between {max(numbers)} and {min(numbers)}: ",
		f'what is {min(numbers)} less than {max(numbers)}: ',
		f'subtract {min(numbers)} from {max(numbers)}: ']
		ans = (random.choice(questions)) 
		return(ans,ans1)
	
	@staticmethod
	def do_negativeDivision(line):
		'''long division'''
		numbers = random.randint(-1000,1000),random.randint(12,10000)
		
		ans1 = max(numbers)/min(numbers)
		while True:
			if divmod(max(numbers),min(numbers))[1] == 0:
				break;
			else:
				numbers = random.randint(-1000,1000),random.randint(12,10000)
		ans1 = round(max(numbers)/min(numbers))
		ans=(f'{max(numbers)} / {min(numbers)} = ')
		return(ans,ans1)
	
	
	@staticmethod
	def do_negativeBidmas(line):
		'''Rules of operations:Brackets,Indices,Multiplication,Division,Addition,Subtraction'''
		operators=list('*/(+-')
		length = 7
		count = 0
		equation = []
		while count != length:	
			op=random.choice(operators)
			if op != '(':
				nums=random.randint(-100,100),random.randint(-100,100)	
				if op == '-':
					part = f'{max(nums)} {op} {min(nums)}'
				elif op == '/':
					while True:
						if divmod(max(nums),min(nums))[1] == 0:
							break;
						else:
							nums=random.randint(-100,100),random.randint(-100,100)
					part = f'{max(nums)} {op} {min(nums)}'
				else:
					part = f'{nums[0]} {op} {nums[1]}'
				equation.append(part)
				count+=1
			elif op == '(':
				nums=random.randint(-100,100),random.randint(-100,100)
				
				while op == '(':
					op=random.choice(operators)
					if op != "(":
						break;	
				if op == '-':
					part = f'({max(nums)} {op} {min(nums)})'
				elif op == '/':
					while True:
						if divmod(max(nums),min(nums))[1] == 0:
							break;
						else:
							nums=random.randint(-100,100),random.randint(-100,100)
					part = f'({max(nums)} {op} {min(nums)})'
				else:
					part = f'({nums[0]} {op} {nums[1]})'
				equation.append(part)
				count+=1
		x=equation[0]
		equation.pop(0)
		for n,i in enumerate(equation): 
			
			if eval(f'{x}') >= eval(f'{i}'):
				op=random.choice('*+')
			else:
				op=random.choice('*/+-')
				if op == '/' and divmod(eval(x),eval(i))[1] != 0:
					op=random.choice('*+-')
			x=f'{x}{op}{i}'
		ans=eval(x)
		ans1 = (f"{x} \n =")
		return(ans1,ans)

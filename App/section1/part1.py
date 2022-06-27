import random
class functions:
	'''spacing_ints: How to correctly format numbers
	place_value: Given the place value of a number (eg. place value of 4 in 1400 =400)
	evenOdd: Wether a number is even or odd:
	complement10: Find the complement of 10
	complement100: Find the complement of 100
	times_tables: Times tables up to 12*12
	addition: Simple addition
	subtraction: Simple Subtraction
	simpleDivision: Simple Division
	longivision: Long division
	multiply10: Multiplying by 10
	multiple100: Multiplying by 100
	multiply1000: Multiply by 1000
	bidmas: Rules of Operations'''
	
	@staticmethod		
	def do_spacing_ints(line):
		'''Numbers should be written with a comma every 3 spaces from the right'''
		number = random.randint(100000,10000000000000000)
		print
		length = len(str(number))
		x = []
		for pos,num in enumerate(str(number)):
			x.append(num)
			if (pos+1)%3 == 0 and pos+1 < length:
				x.append(',')
		ans1=''.join(x)
		ans2=''.join(x).replace(',',' ') 
		ans = (f'\nformat the number {number} so that it is more readable: \nAnswer:')
		if ans == ans1:
			ans1=ans1
		elif ans == ans2:
			ans1=ans2
		return ans,ans1
	
	@staticmethod
	def do_place_value(line):
		'''Tests on place value e.g the place value of 4 in 340 is 40, 4*10 = 40'''
		number = set(x for x in str(random.randint(100000,10000000000000000)))
		value = random.choice(list(number))
		pos=list(number).index(value)
		length=len(number)-1
		place = (length-pos)
		place = '0'*place
		ans1=str(value)+place
		ans = ('\ngive the place value of {0} in {1}: \nAnswer:'.format(value,''.join(number)))
		return(ans,ans1)
		
	
	@staticmethod
	def do_evenOdd(line):
		'''Tells whether or not a number is even or odd,Even numbers are divisible by 2'''
		number = random.randint(1,10000000000)
		if number %2 == 0:
			ans1='even'
		else:
			ans1='odd'
		ans=(f'\nIs {number} even or odd? ')
		return ans.lower(),ans1
	
	@staticmethod
	def do_complement10(line):
		'''The complement to 10 of 7 is 3 (10-7=3)'''
		number = random.randint(0,10)
		ans1 = 10-number
		ans=(f"\nWhat is the complement to 10 of {number}: ")
		return ans,ans1
	
	@staticmethod
	def do_complement100(line):
		'''The complement to 100 of 70 is 30 (100-70=30)'''
		number = random.randint(0,100)
		ans1 = 100-number
		ans=(f"\nWhat is the complement to 100 of {number}: ")
		return ans,ans1
	
	
	@staticmethod
	def do_times_tables(line):
		'''Multiplication up to 12x12'''
		number1 = random.randint(1,12)
		number2 = random.randint(1,12)
		ans1 = number1*number2
		ans=(f'{number1} X {number2} = ')
		return ans,ans1
	
	@staticmethod
	def do_addition(line):
		'''simple addition'''
		number1 = random.randint(1,9999)
		number2 = random.randint(1,9999)
		ans1 = number1+number2
		ans=(f'{number1} + {number2} = ')
		return(ans,ans1)
	
	@staticmethod
	def do_subtraction(line):
		'''simple subtraction'''
		numbers = random.randint(1,9999),random.randint(1,9999)
		
		ans1 = max(numbers)-min(numbers)
		questions = [f'{max(numbers)} - {min(numbers)} = ',
		f"find the difference between {max(numbers)} and {min(numbers)}: ",
		f'what is {min(numbers)} less than {max(numbers)}: ',
		f'subtract {min(numbers)} from {max(numbers)}: ']
		ans = (random.choice(questions)) 
		return(ans,ans1)
	
	@staticmethod
	def do_simpleDivision(line):
		'''Simple division'''
		numbers = random.randint(1,12),random.randint(12,100)
		
		ans1 = max(numbers)/min(numbers)
		while True:
			if divmod(max(numbers),min(numbers))[1] == 0:
				break;
			else:
				numbers = random.randint(1,12),random.randint(12,100)
		ans1 = round(max(numbers)/min(numbers))
		ans=(f'{max(numbers)} / {min(numbers)} = ')
		return(ans,ans1)
	@staticmethod
	def do_longDivision(line):
		'''long division'''
		numbers = random.randint(1,1000),random.randint(12,10000)
		
		ans1 = max(numbers)/min(numbers)
		while True:
			if divmod(max(numbers),min(numbers))[1] == 0:
				break;
			else:
				numbers = random.randint(1,1000),random.randint(12,10000)
		ans1 = round(max(numbers)/min(numbers))
		ans=(f'{max(numbers)} / {min(numbers)} = ')
		return(ans,ans1)
	
	
	
	@staticmethod
	def do_multiply10(line):
		'''multiplications by 10
		#can be broken down
		#e.g. 230*20 == 230*10*10
		#12*20 == 12*2*10'''
		number1 = random.randint(0,990)
		while number1 % 10 != 0:
			number1 = random.randint(0,990)
		number2 = random.randint(10,90)
		while number2 % 10 != 0:
			number2 = random.randint(10,90)
		
		ans1 = number1*number2
		questions = [f'{number1} X {number2} =', f'what is the product of {number1} by {number2}: ']
		ans = (random.choice(questions)) 
		return(ans,ans1)
	
	@staticmethod
	def do_multiply100(line):
		'''multiplications by 100
		can be broken down
		e.g. 230*200 == 230*100*100
		12*200 == 12*20*100'''
		number1 = random.randint(0,9990)
		while number1 % 10 != 0:
			number1 = random.randint(0,9990)
		number2 = random.randint(100,990)
		while number2 % 10 != 0:
			number2 = random.randint(100,990)
		
		ans1 = number1*number2
		questions = [f'{number1} X {number2} =', f'what is the product of {number1} by {number2}: ']
		ans = (random.choice(questions)) 
		return(ans,ans1)
	
	@staticmethod
	def do_multiply1000(line):
		'''multiplications by 100
		can be broken down
		e.g. 230*2000 == 230*1000*1000
		12*2000 == 12*20*1000'''
		number1 = random.randint(0,9990)
		while number1 % 10 != 0:
			number1 = random.randint(0,9990)
		number2 = random.randint(1000,9900)
		while number2 % 10 != 0:
			number2 = random.randint(1000,9900)
		
		ans1 = number1*number2
		questions = [f'{number1} X {number2} =', f'what is the product of {number1} by {number2}: ']
		ans = (random.choice(questions)) 
		return(ans,ans1)
		
	@staticmethod
	def do_bidmas(line):
		'''Rules of operations:Brackets,Indices,Multiplication,Division,Addition,Subtraction'''
		operators=list('*/(+-')
		length = 7
		count = 0
		equation = []
		while count != length:	
			op=random.choice(operators)
			if op != '(':
				nums=random.randint(1,100),random.randint(1,100)	
				if op == '-':
					part = f'{max(nums)} {op} {min(nums)}'
				elif op == '/':
					while True:
						if divmod(max(nums),min(nums))[1] == 0:
							break;
						else:
							nums=random.randint(1,100),random.randint(1,100)
					part = f'{max(nums)} {op} {min(nums)}'
				else:
					part = f'{nums[0]} {op} {nums[1]}'
				equation.append(part)
				count+=1
			elif op == '(':
				nums=random.randint(1,100),random.randint(1,100)
				
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
							nums=random.randint(1,100),random.randint(1,100)
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

#find the factors of two random numbers

import random
class Test:
	@staticmethod
	def factors():
		i = random.randint(1,100)
		answer=[n for n in range(1,i+1) if i%n==0]
		ans = input(f'find all the factors of {i}: ')
		ans = [int(x) for x in ans.rstrip().replace(" ","").split(',') if x.isdigit() and int(x) in answer]
		if all(x in ans for x in answer):
			print('well done')
			return 1,1
		else:
			print('wrong, the answer is {answer}')
			return(answer,ans)
	#write long numbers with a comma or space
	#numbers should be written with a comma every 3 spaces from the right
	@staticmethod		
	def spacing_ints():
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
		ans = input(f'\nformat the number {number} so that it is more readable: \nAnswer:')
		if ans == ans1:
			ans1=ans1
		elif ans == ans2:
			ans1=ans2
		return ans,ans1
	#tests on place value
	#e.g the place value of 4 in 340 is 40, 4*10 = 40
	@staticmethod
	def place_value():
		number = set(x for x in str(random.randint(100000,10000000000000000)))
		value = random.choice(list(number))
		pos=list(number).index(value)
		length=len(number)-1
		place = (length-pos)
		place = '0'*place
		ans1=str(value)+place
		ans = input('\ngive the place value of {0} in {1}: \nAnswer:'.format(value,''.join(number)))
		return(ans,ans1)
		'''	
		if ans == ans1:
			print('well done')
			return(1,1)
		else:
			print(f'wrong, the answer is {ans1}')
			return(0,1)'''
	#tells whether or not a number is even or odd
	#even numbers are divisible by 2
	@staticmethod
	def evenOdd():
		number = random.randint(1,10000000000)
		if number %2 == 0:
			ans1='even'
		else:
			ans1='odd'
		ans=input(f'\nIs {number} even or odd? ')
		return ans.lower(),ans1
	#finds the complement of 10
	#e.g the complement to 10 of 7 is 3 (10-7=3)
	@staticmethod
	def complement10():
		number = random.randint(0,10)
		ans1 = 10-number
		ans=input(f"\nWhat is the complement to 10 of {number}: ")
		return ans,ans1
	#finds the complement of 100
	#e.g the complement to 100 of 70 is 30 (100-70=30)
	@staticmethod
	def complement100():
		number = random.randint(0,100)
		ans1 = 100-number
		ans=input(f"\nWhat is the complement to 100 of {number}: ")
		return ans,ans1
	
	#multiplication up to 12x12
	@staticmethod
	def times_tables():
		number1 = random.randint(1,12)
		number2 = random.randint(1,12)
		ans1 = number1*number2
		ans=input(f'{number1} X {number2} = ')
		return ans,ans1
	#simple addition
	@staticmethod
	def addition():
		number1 = random.randint(1,9999)
		number2 = random.randint(1,9999)
		ans1 = number1+number2
		ans=input(f'{number1} + {number2} = ')
		return(ans,ans1)
	#simple subtraction
	@staticmethod
	def subtraction():
		numbers = random.randint(1,9999),random.randint(1,9999)
		
		ans1 = max(numbers)-min(numbers)
		questions = [f'{max(numbers)} - {min(numbers)} = ',
		f"find the difference between {max(numbers)} and {min(numbers)}: ",
		f'what is {min(numbers)} less than {max(numbers)}: ',
		f'subtract {min(numbers)} from {max(numbers)}: ']
		ans = input(random.choice(questions)) 
		return(ans,ans1)
	
	@staticmethod
	def simpleDivision():
		numbers = random.randint(1,12),random.randint(12,100)
		
		ans1 = max(numbers)/min(numbers)
		while True:
			if divmod(max(numbers),min(numbers))[1] == 0:
				break;
			else:
				numbers = random.randint(1,12),random.randint(12,100)
		ans1 = round(max(numbers)/min(numbers))
		ans=input(f'{max(numbers)} / {min(numbers)} = ')
		return(ans,ans1)
	@staticmethod
	def longDivision():
		numbers = random.randint(1,1000),random.randint(12,10000)
		
		ans1 = max(numbers)/min(numbers)
		while True:
			if divmod(max(numbers),min(numbers))[1] == 0:
				break;
			else:
				numbers = random.randint(1,1000),random.randint(12,10000)
		ans1 = round(max(numbers)/min(numbers))
		ans=input(f'{max(numbers)} / {min(numbers)} = ')
		return(ans,ans1)
	
	
	#multiplications by 10
	#can be broken down
	#e.g. 230*20 == 230*10*10
	#12*20 == 12*2*10
	@staticmethod
	def multiply10():
		number1 = random.randint(0,990)
		while number1 % 10 != 0:
			number1 = random.randint(0,990)
		number2 = random.randint(10,90)
		while number2 % 10 != 0:
			number2 = random.randint(10,90)
		
		ans1 = number1*number2
		questions = [f'{number1} X {number2} =', f'what is the product of {number1} by {number2}: ']
		ans = input(random.choice(questions)) 
		return(ans,ans1)
	#multiplications by 100
	#can be broken down
	#e.g. 230*200 == 230*100*100
	#12*200 == 12*20*100
	@staticmethod
	def multiply100():
		number1 = random.randint(0,9990)
		while number1 % 10 != 0:
			number1 = random.randint(0,9990)
		number2 = random.randint(100,990)
		while number2 % 10 != 0:
			number2 = random.randint(100,990)
		
		ans1 = number1*number2
		questions = [f'{number1} X {number2} =', f'what is the product of {number1} by {number2}: ']
		ans = input(random.choice(questions)) 
		return(ans,ans1)
		#multiplications by 100
	#can be broken down
	#e.g. 230*2000 == 230*1000*1000
	#12*2000 == 12*20*1000
	@staticmethod
	def multiply1000():
		number1 = random.randint(0,9990)
		while number1 % 10 != 0:
			number1 = random.randint(0,9990)
		number2 = random.randint(1000,9900)
		while number2 % 10 != 0:
			number2 = random.randint(1000,9900)
		
		ans1 = number1*number2
		questions = [f'{number1} X {number2} =', f'what is the product of {number1} by {number2}: ']
		ans = input(random.choice(questions)) 
		return(ans,ans1)
		
	@staticmethod
	def bidmas():
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
		ans1 = input(f"{x} \n =")
		return(ans1,ans)





#--------------------------------------------------------------------------------------------------------
class Score:	
	#increments score
	def __init__(self,func,q):
		res=self.answer(func[0],func[1])
		global results
		if res is True:
			results+=1
		print(f'score: {results}/{q}')
	#checks if answer is right
	def answer(self,ans,ans1):
		if ans == str(ans1):
			print('well done')
			return (True)
		else:
			print(f'wrong, the answer is {ans1}')
		
		
		
		
				
section1={'writing ints':Test().spacing_ints,'place_value':Test().place_value,
'even or odd':Test().evenOdd,'complement of 10':Test().complement10,'complement of 100':Test().complement100,'times tables':Test().times_tables,'addition':Test().addition,'subtraction':Test().subtraction,
'multiply by 10':Test().multiply10,'multiply by 100':Test().multiply100,'multiply by 1000':Test().multiply1000,'bidmas':Test().bidmas,'division':Test().simpleDivision,
'long division':Test().longDivision}
extra = {'factors':Test().factors}	
questions=input('How many questions: ')

try:
	int(questions)
except:
	questions=str(random.randint(0,100))
results=0
print('\nTopics')
for key in section1.keys():
	print(key)
print('\n')
topic = input("Choose a topic:")

for q in range(1,int(questions)+1):
	print(f'\nQuestion {q}:')
	if topic in section1.keys():
		Score(section1[topic](),questions)
	else:
		Score(section1[random.choice([keys for keys in section1.keys()])](),questions)
		
				
#thinking about splitting into sections and importing them into main
#need to add a "write the numbers as a word"
#want to add a timer for multiplication or add an arthmitic function
#maybe add an overall timer as an option
#need to clean up main
#add a range so that a topic, topic range or random can be selected
#add an individual timer for indv questions and and an overall timer
#add some worded questions and questions with irrelevant material

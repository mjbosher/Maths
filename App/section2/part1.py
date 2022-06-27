import pandas as pd
import random
import numpy as np
from fractions import Fraction
import math
class functions:
	'''section2 do something: How to correctly format numbers
	'''
	@staticmethod
	def do_addDecimals(line):
		'''add decimals'''
		decimals = np.random.rand(1,2)
		
		number1 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		number2 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		ans1 = number1+number2
		ans=(f'{number1} + {number2} = ')
		return ans,ans1
	@staticmethod
	def do_subtractDecimals(line):
		'''subtract decimals'''
		decimals = np.random.rand(1,2)
		
		number1 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		number2 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		ans1 = number1-number2
		ans=(f'{number1} - {number2} = ')
		return ans,ans1
	@staticmethod
	def do_MultiplyDecimals(line):
		'''Multiplication of decimals'''
		decimals = np.random.rand(1,2)
		
		number1 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		number2 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		ans1 = number1*number2
		ans=(f'{number1} x {number2} = ')
		return ans,ans1
	@staticmethod
	def do_decimalsTimes1000(line):
		'''Multiplication of decimals by 1000, move left according to number of 0s'''
		decimals = np.random.rand(1,1)
		number1 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		number2 = random.choice([10,100,1000])
		ans1 = number1*number2
		ans=(f'{number1} X {number2} = ')
		return ans,ans1
	@staticmethod
	def do_decimalsDivideBy1000(line):
		'''Move decimals right by number of 0s'''
		decimals = np.random.rand(1,1)
		number1 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		number2 = random.choice([10,100,1000])
		ans1 = number1/number2
		ans=(f'{number1} / {number2} = ')
		return ans,ans1
	@staticmethod
	def do_decimalOrder(line):
		'''sort decimal order'''
		len_=random.randint(2,5)
		decimals = np.random.rand(1,len_)
		numbers = [random.randint(0,100)+decimals[0][x] for x in range(len_)]
		[random.choice([str(number),str(number).zfill(random.randint(len(str(number))
		+2,len(str(number))+5)),str(number)+'0'*random.randint(1,4)]) for number in numbers]
		numbers=[round(n,7) for n in numbers]	
		ans1 = sorted(numbers)
		ans=(f'Put the following into order:\n {[x for x in numbers]}\n ')
		return ans,ans1
	@staticmethod
	def do_decimal2Fraction(line):
		'''0.345 = 345/1000 simplified'''
		decimals = np.random.rand(1,1)
		number1 = str(round(random.randint(0,0)+decimals[0][0],random.randint(3,7)))
		number2 = len(number1.split('.')[1])	
		
		number2=int(f'1{"0"*number2}')
		
		frac=Fraction(int(number1.split('.')[1]),number2)
		ans1 = f'{frac.numerator}/{frac.denominator}'
		ans=(f'{number1} as a fraction: ')
		return ans,ans1
	@staticmethod
	def do_fraction2Decimal(line):
		'''2/4 = 2 divided by 4 == decimal '''
		number1 = random.randint(1,1000)
		number2 = random.randint(1,1000)
		ans1 = number1/number2
		ans=(f'{number1}/{number2} as a Decimal: ')
		return ans,ans1
	@staticmethod
	def do_recurringDecimals(line):
		'''n = number of recurring decimals, x= recurring decimal
		nominator = (x*(x**n))-x
		denominator = (x**n)-1'''
		data=pd.read_csv('/home/michael/Downloads/Maths/App/section2/recurring_decimals.csv',sep='#').sample(1)
		fraction,decimal=data.fractions.values[0],data.decimals.values[0]	
		ans=(f'{decimal} as a fraction: ')
		return ans,fraction
	@staticmethod
	def do_divideDecimals(line):
		'''Division of decimals'''
		decimals = np.random.rand(1,2)
		
		number1 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		number2 =  round(random.randint(1,100)+decimals[0][0],random.randint(3,7))
		n = number1,number2
		ans1 = round(max(n)/min(n),3)
		ans=(f'{max(n)} / {min(n)} = ')
		return ans,ans1
	@staticmethod
	def do_roundDecimals(line):
		decimals = np.random.rand(1,2)
		number1 =  round(random.randint(1,100)+decimals[0][0],random.randint(4,7))
		n=random.randint(1,4)
		ans1 = round(number1,n)
		ans=(f'Round {number1} to {n} places: ')
		return(ans,ans1)

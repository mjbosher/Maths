import pandas as pd
import random
import numpy as np
from fractions import Fraction
import math
class functions:
	'''section2 do something: How to correctly format numbers
	'''
	@staticmethod
	def do_percent2Fraction(line):
		'''percent/100 then simplify it'''
		number1 =  random.randint(1,500)
		ans1 = Fraction(number1,100)
		ans1 = f'{ans1.numerator}/{ans1.denominator}'
		ans=(f'{number1}% as a fraction = ')
		return ans,ans1
	@staticmethod	
	def do_fraction2Percent(line):
		'''n/d , (n*100)/d = %'''
		f1=random.randint(1,50),random.randint(1,50)
		ans1 = f1[0]*100
		ans1 = ans1/f1[1]
		ans1 = f'{round(ans1,2)}%'
		ans=(f'{f1[0]}/{f1[1]} as a percent (2dp) = ')
		return ans,ans1
	@staticmethod	
	def do_percent2Quantity(line):
		'''x% of y, (x%/100(simplified)) == n/d, (n*y)/d == quantity'''
		f1=random.randint(1,50),random.randint(1,50)
		ans1 = Fraction(f1[0],100)
		ans2 = ans1.numerator*f1[1]
		ans1 = ans2/ans1.denominator
		ans=(f'Find {f1[0]}% of {f1[1]} = ')
		return ans,ans1
	@staticmethod	
	def do_percentIncrease(line):
		'''find 120% of 48, simplified(120/100)*48/1 = 288/5, 288/5 =57.6,
		'''
		f1=random.randint(100,500),random.randint(1,1000)
		frac1 = Fraction(f1[0],100)
		frac2 = Fraction(f1[1],1)
		frac = frac1*frac2
		ans1 = frac.numerator/frac.denominator
		ans=(f'Find {f1[0]}% of {f1[1]} = ')
		return ans,ans1
	@staticmethod	
	def do_percentReduction(line):
		'''((100-percent)/100)*n
		'''
		f1=random.randint(0,99),random.randint(1,1000)
		ans1=((100-f1[0])/100)*f1[1]
		ans=(f'Reduce {f1[1]} by {f1[0]}% = ')
		return ans,ans1
	@staticmethod	
	def do_comparingAsPercent(line):
		'''x gets 250 per week and spends 75 on rent, 
		what percent of income is spent on rent
		75/250 == 3/10
		3/10 * 100 = 300/10 == 30/1 == 30%'''
		f1=random.randint(0,99),random.randint(1,1000)
		frac = Fraction(min(f1),max(f1))
		percent = Fraction(100,1)
		ans1 = frac*percent
		ans1 = ans1.numerator/ans1.denominator
		ans1 = f'{round(ans1,2)}%'
		ans=(f'{min(f1)} as a percent of {max(f1)} = ')
		return ans,ans1
	@staticmethod
	def do_increaseDecreaseAsPercent(line):
		'''A 3m cloth shrunk to 2.91 how much did it shrink by as a percent:
			3-2.91/3 * 100/1 == inc|dec/orig *100'''
		orig = random.randint(0,9000)
		price= random.randint(0,9000)
		ans=f"A car costs {orig} and is sold for {price}.Find the % of increase/decrase:"
		if orig > price:
			price=orig-price
		else:
			price=price-orig
		ans1 = f'{round((price/orig)*100,1)}%'
		
		return(ans,ans1)
	@staticmethod
	def do_originalPriceFromPercent(line):
		'''A suit case in a sale has been reduced by 40% it is now 72%
what was the original price?
		original/(100-percent)*100/1
		'''
		orig = random.randint(0,9000)
		percent= random.randint(0,100)
		choice = random.choice(["increased","decreased"])
		ans=f"A car costs {orig} and has been {choice} by {percent}%.Find the original price"
		if choice == "decreased":
			percent=100-percent
		elif choice == "increased":
			percent=100+percent
		
		ans1=round((orig/percent)*100,2)
		
		return(ans,ans1)


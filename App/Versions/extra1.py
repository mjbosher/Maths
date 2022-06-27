import random
from math import gcd,sqrt
class Extra:
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
			print(f'wrong, the answer is {answer}')
			return(answer,ans)
	@staticmethod
	def commonFactors():
		x = random.randint(1,200)
		y = random.randint(1,200)
		answer1=[n for n in range(1,x+1) if x%n==0]
		answer2=[n for n in range(1,y+1) if y%n==0]
		answer = [x for x in answer1 if x in answer2]
		ans = input(f'find all the common factors of {x} and {y}: ')
		ans = [int(x) for x in ans.rstrip().replace(" ","").split(',') if x.isdigit() and int(x) in answer]
		if all(x in ans for x in answer):
			print('well done')
			return 1,1
		else:
			print(f'wrong, the answer is {answer}')
			return(answer,ans)
	@staticmethod
	def greatestCommonFactor():
		'''two methods: first the gcf can be no higher than x-y;
		second compare prime factors
		24 and 108 	2 × 2 × 2 × 3 = 24, and
				2 × 2 × 3 × 3 × 3 = 108 	2 × 2 × 3 = 12
		'''
		x = random.randint(1,200)
		y = random.randint(1,200)
		ans=f"Find the greatest common factor of {x} and {y}"
		ans1=gcd(x,y)
		return(ans,ans1)
		
	@staticmethod
	def lcm(x, y):
		'''two methods to find the lcm:
			first:
				x*y//gcd(x,y),
			second:
				find gcf of x,y
				divide gcf into easiest number
				then multiply it by the other number'''
				
		x = random.randint(1,200)
		y = random.randint(1,200)
		ans=f"Find the least common multiple of {x} and {y}"
		ans1=x * y // gcd(x, y)
		return(ans,ans1)
		
print(Extra().greatestCommonFactor())

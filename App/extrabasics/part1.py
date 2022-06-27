import random
from math import gcd,sqrt

class functions:
	'''
	factors: Finding factos
	commonFactors: finding common multiples of two numbers
	greatestCommonFactors: finding the greatest common multiple of two numbers	
	leastCommonMultiple: finding the least common multiple of two numbers
	primeNumbers: Find prime numbers in a given range
	primeFactors: Find the prime factors of a given number
	commonPrimeFactors: Find the common prime factors of 2 given numbers
	'''
	@staticmethod
	def do_factors(line):
		'''easiest way to do this is:
			A:find the prime factors of the number
				e.g 48 =2x2x2x2x3 == 2(4)*3(1)
			B:add one to each exponent
				e.g 2(4)+(1)*3(1)+(1)=2(5)*3(2)
			C:multiply exponents 5*2 = 10 (max number of factors = 10)'''
		i = random.randint(1,100)
		answer=[n for n in range(1,i+1) if i%n==0]
		ans = f'find all the factors of {i}: '
		return(ans,answer)
		
		
		
	@staticmethod
	def do_commonFactors(line):
		'''find all common factors between two numbers'''
		x = random.randint(1,200)
		y = random.randint(1,200)
		answer1=[n for n in range(1,x+1) if x%n==0]
		answer2=[n for n in range(1,y+1) if y%n==0]
		answer = [x for x in answer1 if x in answer2]
		ans = f'find all the common factors of {x} and {y}: '
		return(ans,answer)
		
		
	@staticmethod
	def do_greatestCommonFactor(line):
		'''two methods: first the gcf can be no higher than x-y;
		second compare prime factors
		24 and 108 	2 × 2 × 2 × 3 = 24, and
				2 × 2 × 3 × 3 × 3 = 108 	2 × 2 × 3 = 12
		'''
		x = random.randint(1,200)
		y = random.randint(1,200)
		ans=f"Find the greatest common factor of {x} and {y}\n>>"
		ans1=gcd(x,y)
		return(ans,ans1)
		
	@staticmethod
	def do_leastCommonMultiple(line):
		'''two methods to find the lcm:
			first:
				x*y//gcd(x,y),
			second:
				find gcf of x,y
				divide gcf into easiest number
				then multiply it by the other number'''
				
		x = random.randint(1,200)
		y = random.randint(1,200)
		ans=f"Find the least common multiple of {x} and {y}\n>>"
		ans1=x * y // gcd(x, y)
		return(ans,ans1)
	@staticmethod
	def do_primeNumbers(line):
		'''A prime number can only be divided by 1 and itself'''
		x = random.randint(10,50)
		ans=f"Find the prime numbers up to {x}:\n>>"
		ans1=Tools.primeNumbers(x)
		return(ans,ans1)
	@staticmethod
	def do_primeFactors(line):
		'''prime factors of 12 can be found as such: 12/2=6;6/2=3; factors=2x2x3'''
		x = random.randint(2,1000)
		ans1=Tools.primeFactor(x)
		ans=f"Find the prime factors of {x}\n>>"
		return(ans,ans1)
	@staticmethod
	def do_commonPrimeFactors(line):
		'''prime factors of 12 can be found as such: 12/2=6;6/2=3; factors=2x2x3
		16/2=8/2=4/2=2 factors=2x2x2x2 commonfactors=2x2'''
		#x = random.randint(2,1000)
		#y = random.randint(2,1000)
		x=9;y=27
		primex=Tools().primeFactor(x)
		primey=Tools().primeFactor(y)
		if isinstance(primex,int):
			primex=[primex]
		if isinstance(primey,int):
			primey=[primey]
		factors=[]
		count=0
		while True:
			if count >= len(primex):
				break;
			elif primex[count] in primey:
				primey.remove(primex[count])
				factors.append(primex[count])
			count+=1
		factors.append(1)
		ans1=factors
		ans=f"Find the prime factors of {x} and {y}\n>>"
		return(ans,ans1)
	@staticmethod
	def do_formulas(line):
		'''formulas'''
		data = random.choice([x.rstrip() for x in open("/home/michael/Downloads/Maths/App/extrabasics/formulas")]).split("|")
		answer=data[1]
		ans = f'formula for {data[0]}: '
		return(ans,answer)
			
		
class Tools:
	@staticmethod
	def isPrime(n):
		return n > 1 and all(n % i for i in range(2, n))
	@staticmethod
	def primeNumbers(stop):
		return([n for n in range(1,stop) if Tools.isPrime(n) == True])
	@staticmethod
	def primeFactor(n):
		factors = []
		if Tools().isPrime(n) == True:
			return(n)
		primes = Tools.primeNumbers(1000)
		while True:
			if n!=0 or n!=1  or n not in primes:
				res=Tools().getPrimeFactor(n,primes)
				try:
					factors.append(res[0])
					n=res[1]
				except:
					break
			elif n==0 or n==1 or n in primes:
				break;
		return(factors)
	@staticmethod
	def getPrimeFactor(n,primes):
		for prime in primes:
			if n%prime==0:
				return(prime,n/prime) 


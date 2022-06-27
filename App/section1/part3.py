import random
from math import gcd 
import fractions
class functions:
	'''
	equivalentFractions: Converting fractions into equivalent fractions
	simplifyingFractions: Simplifying fractions
	improper2mixed: Convert improper fractions to mixed numbers
	mixed2improper: Convert mixed numbers to improper fractions
	addingFractions: Adding fractions
	subtractingFractions: Subtracting fractions
	multiplyingFractions: Multiplying fractions
	dividingFractions: DividingFractions
	halfwayFractions: Find a fraction halfway between two fractions
	fractionOfNumber: Find a fraction of a number
	'''
	
	@staticmethod
	def do_equivalentFractions(line):
		'''negative addition --|++ = + & +-|-+ = -'''
		f1=random.randint(1,200),random.randint(1,100)
		f2=random.randint(1,200),random.randint(1,100)
		new_denominator=Tools().lcm(f1[1],f2[1])
		n1 = int(new_denominator/f1[1])
		n1 = n1*f1[0]
		n2 = int(new_denominator/f2[1])
		n2 = n2*f2[0]
		equiv_f1=n1,new_denominator
		equiv_f2=n2,new_denominator
		ans=f"Convert {f1[0]}/{f1[1]} and {f2[0]}/{f2[1]} into equivalent fractions: "
		ans1= f"{equiv_f1[0]}/{equiv_f1[1]} {equiv_f2[0]}/{equiv_f2[1]}"
		return(ans,ans1)
	@staticmethod
	def do_simplifyingFractions(line):
		'''Divide both the top and bottom of the fraction by the Greatest Common Factor'''
		f1=random.randint(1,200),random.randint(1,200)
		f1=min(f1),max(f1)
		ans1 = fractions.Fraction(f1[0],f1[1])
		ans=f"Simplify {f1[0]}/{f1[1]}: "
		ans1=f'{ans1.numerator}/{ans1.denominator}' 
		return(ans,ans1)
	@staticmethod
	def do_improper2mixed(line):
		'''divide the top by the bottom and represent the remainder as a fraction'''
		f1=random.randint(1,500),random.randint(1,500)
		f1=max(f1),min(f1)
		n=divmod(f1[0],f1[1])
		ans=f"Convert {f1[0]}/{f1[1]} to a mixed number and simplify the remainder: "
		f2=fractions.Fraction(n[1],f1[1])
		ans1=f'{n[0]} {f2.numerator}/{f2.denominator}'
		return(ans,ans1)
	@staticmethod
	def do_mixed2improper(line):
		'''convert mixed numbers to improper fractions'''
		f1=random.randint(1,200),random.randint(1,200)
		f1=min(f1),max(f1)
		n = random.randint(1,15)
		f2 = (n*f1[1])+f1[0], f1[1]
		f2=fractions.Fraction(f2[0],f2[1])
		ans=f"Convert {n} {f1[0]}/{f1[1]} to an improper fraction and simplify the remainder: "
		ans1=f'{f2.numerator}/{f2.denominator}'
		return(ans,ans1)
	@staticmethod
	def do_addingFractions(line):
		'''adding fractions by turning them into equivalent fractions and then simplifying them'''
		f1=random.randint(1,50),random.randint(1,50)
		f1=min(f1),max(f1)
		f2=random.randint(1,50),random.randint(1,50)
		f2=min(f2),max(f2)
		f3=fractions.Fraction(f1[0],f1[1])+fractions.Fraction(f2[0],f2[1])
		ans1 = f'{f3.numerator}/{f3.denominator}'
		if f3.numerator > f3.denominator:
			n=divmod(f3.numerator,f3.denominator)
			f4=fractions.Fraction(n[1],f3.denominator)
			ans1=f'{n[0]} {f4.numerator}/{f4.denominator}'
		ans=f"{f1[0]}/{f1[1]} + {f2[0]}/{f2[1]}= "
		return(ans,ans1)
	@staticmethod
	def do_subtractingFractions(line):
		'''subtracting fractions by turning them into equivalent fractions and then simplifying them'''
		f1=random.randint(1,50),random.randint(1,50)
		f1=min(f1),max(f1)
		f2=random.randint(1,50),random.randint(1,50)
		f2=min(f2),max(f2)
		if f1[1] > f2[1]:
			f3=fractions.Fraction(f1[0],f1[1])-fractions.Fraction(f2[0],f2[1])
			ans=f"{f1[0]}/{f1[1]} - {f2[0]}/{f2[1]}= "
			
		else:
			f3=fractions.Fraction(f2[0],f2[1])-fractions.Fraction(f1[0],f1[1])
			ans=f"{f2[0]}/{f2[1]} - {f1[0]}/{f1[1]}= "
		
		ans1 = f'{f3.numerator}/{f3.denominator}'
		if f3.numerator > f3.denominator:
			n=divmod(f3.numerator,f3.denominator)
			f4=fractions.Fraction(n[1],f3.denominator)
			ans1=f'{n[0]} {f4.numerator}/{f4.denominator}'
		return(ans,ans1)
	@staticmethod
	def do_multiplyingFractions(line):
		'''multiplying fractions by multiplying the top numbers and then the bottom and then simplifying them'''
		f1=random.randint(1,50),random.randint(1,50)
		f1=min(f1),max(f1)
		f2=random.randint(1,50),random.randint(1,50)
		f2=min(f2),max(f2)
		
		f3=fractions.Fraction(f1[0],f1[1])*fractions.Fraction(f2[0],f2[1])
		ans=f"{f1[0]}/{f1[1]} * {f2[0]}/{f2[1]}= "
			
		ans1 = f'{f3.numerator}/{f3.denominator}'
		if f3.numerator > f3.denominator:
			n=divmod(f3.numerator,f3.denominator)
			f4=fractions.Fraction(n[1],f3.denominator)
			ans1=f'{n[0]} {f4.numerator}/{f4.denominator}'
		return(ans,ans1)
	@staticmethod
	def do_dividingFractions(line):
		'''dividing fractions: turn the right fraction upside down(reciprocal) and multiply it'''
		f1=random.randint(1,50),random.randint(1,50)
		f1=min(f1),max(f1)
		f2=random.randint(1,50),random.randint(1,50)
		f2=min(f2),max(f2)
		
		if f1[1] > f2[1]:
			f3=fractions.Fraction(f1[0],f1[1])/fractions.Fraction(f2[0],f2[1])
			ans=f"{f1[0]}/{f1[1]} / {f2[0]}/{f2[1]}= "
			
		else:
			f3=fractions.Fraction(f2[0],f2[1])/fractions.Fraction(f1[0],f1[1])
			ans=f"{f2[0]}/{f2[1]} / {f1[0]}/{f1[1]}= "
		
		ans1 = f'{f3.numerator}/{f3.denominator}'
		if f3.numerator > f3.denominator:
			n=divmod(f3.numerator,f3.denominator)
			f4=fractions.Fraction(n[1],f3.denominator)
			ans1=f'{n[0]} {f4.numerator}/{f4.denominator}'
		return(ans,ans1)
	@staticmethod
	def do_halfwayFractions(line):
		'''Which fraction is halfway between two fractions; add both together and then divide by two'''
		f1=random.randint(1,50),random.randint(1,50)
		f1=min(f1),max(f1)
		f2=random.randint(1,50),random.randint(1,50)
		f2=min(f2),max(f2)
		f3=(fractions.Fraction(f1[0],f1[1])+fractions.Fraction(f2[0],f2[1]))
		ans=f"Which fraction is halfway between {f1[0]}/{f1[1]} and {f2[0]}/{f2[1]}: "
		f3 = f3/2
		ans1 = f'{f3.numerator}/{f3.denominator}'
		if f3.numerator > f3.denominator:
			n=divmod(f3.numerator,f3.denominator)
			f4=fractions.Fraction(n[1],f3.denominator)
			ans1=f'{n[0]} {f4.numerator}/{f4.denominator}'
		return(ans,ans1)
	@staticmethod
	def do_fractionOfNumber(line):
		'''divide denominator by numerator then times by number'''
		f1=random.randint(1,50),random.randint(1,50)
		f1=min(f1),max(f1)
		f2=random.randint(1,50)
		ans1=round((f1[0]/f1[1])*f2,1)
		ans=f"Find {f1[0]}/{f1[1]} of {f2}: "
		return(ans,ans1)
class Tools:
	@staticmethod
	def lcm(x, y):
		return x * y // gcd(x, y)

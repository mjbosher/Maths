import random
from fractions import Fraction
import math
class functions:
	'''section2 do something: How to correctly format numbers
	'''
	@staticmethod
	def do_simplifyRatios(line):
		'''percent/100 then simplify it'''
		x,y =  round(random.uniform(0,10),2),round(random.uniform(0,10),2)
		
		
		q=random.choice(['decimal','fraction'])
		if q == 'fraction':
			frac1=Fraction(x).limit_denominator(10)#return ans,ans1
			frac2=Fraction(y).limit_denominator(10)
		
			lcm=frac1.denominator*frac2.denominator//math.gcd(
			frac1.denominator, frac2.denominator)
		
			d1,d2 = (lcm/frac1.denominator),(lcm/frac2.denominator)
			n1,n2 = round(frac1.numerator*d1),round(frac2.numerator*d2)
			hcf=math.gcd(n1,n2)
		
			q=f'{frac1.numerator}/{frac1.denominator}:{frac2.numerator}/{frac2.denominator}'
			
		else:
			q=f'{x}:{y}'
			n1,n2 = round(x*100,2),round(y*100,2)
			hcf = math.gcd(int(n1),int(n2))
			
			ans1=''
		ans=f'Simplify the ratio {q}'
		ans1=f"{round(n1/hcf)}:{round(n2/hcf)}"
		return(ans,ans1)
	@staticmethod
	def do_relatingRatios(line):
		'''convert to a fraction and then use it to work out percent'''
		x1,y1 =  round(random.uniform(1,10),2),round(random.uniform(1,10),2)
		x2,y2 =  random.randint(1,99),random.randint(1,99)
		weights = [0.25,0.25,0.25,0.25]
		x,y = random.choices([x1,y1,x2,y2],weights,k=2)
		while x == y:
			x,y = random.choices([x1,y1,x2,y2],weights,k=2)
		if isinstance(x,float) or isinstance(y,float):
			x1,y1 = int(x*100),int(y*100)
			hcf = math.gcd(x1,y1)
			x1,y1 = int(x1/hcf),int(y1/hcf)
		else:
			x1,y1 = x,y
		q=random.choice(['percent','fraction'])
		frac1=Fraction(x1,y1)
		if q == 'fraction':	
			q=f'{x}:{y} first as a fraction of the second:'
			a=f"{frac1.numerator}/{frac1.denominator}"
		else:
			q=f'{x}:{y} first as a percent of the second:'
			a = f'{round((frac1.numerator/frac1.denominator)*100,2)}%'
		ans=q
		ans1=a
		return(ans,ans1)
	@staticmethod
	def do_convertingRatios(line):
		'''convert to a fraction and then use it to work out percent'''
		x1,y1 =  round(random.uniform(1,10),2),round(random.uniform(1,10),2)
		x2,y2 =  random.randint(1,99),random.randint(1,99)
		weights = [0.25,0.25,0.25,0.25]
		x,y = random.choices([x1,y1,x2,y2],weights,k=2)
		while x == y:
			x,y = random.choices([x1,y1,x2,y2],weights,k=2)
		if isinstance(x,float) or isinstance(y,float):
			x1,y1 = int(x*100),int(y*100)
			hcf = math.gcd(x1,y1)
			x1,y1 = int(x1/hcf),int(y1/hcf)
			
		else:
			x1,y1 = x,y
			
		q=random.choice(['percent','fraction'])
		frac1=Fraction(x1,x1+y1)
		if q == 'fraction':	
			q=f'{x}:{y} first as a fraction of the total:'
			a=f"{frac1.numerator}/{frac1.denominator}"
		else:
			q=f'{x}:{y} first as a percent of the total:'
			a = f'{round((frac1.numerator/frac1.denominator)*100,2)}%'
		ans=q
		ans1=a
		return(ans,ans1)
	@staticmethod
	def do_Amount2Ratio(line):
		'''if x,y,z are given 120 and share it in a ratio 1:2:3,
		 how much does y get
		formula = 120/sum(1,2,3)*y'''
		ratios = [random.randint(0,50) for x in range(random.randint(2,3))]
		amount = random.randint(1,1000)
		ratio = random.randint(0,len(ratios)-1)
		names=['x','y','z']
		ans1= round((amount/sum(ratios))*ratios[ratio],2)
		nStr=','.join([names[x] for x in range(len(ratios))])
		ratStr=":".join([str(x) for x in ratios])		
		ans=f'{nStr} get {amount} in a ratio of {ratStr} what will {names[ratio]} get?'
		
		return(ans,ans1)
	@staticmethod
	def do_RatiosWithOneQuantity(line):
		'''ratiox/total_parts*ratioy'''
		ratios = [random.randint(1,50) for x in range(random.randint(2,3))]
		animals = ["lynxes","seals","koalas"]
		animals = [animals[x] for x in range(len(ratios))]
		
		animal = random.randint(0,len(animals)-1)
		animal2 = random.randint(0,len(animals)-1)
		ratiopart = random.randint(2,1000)
		ratioStr = ':'.join([str(x) for x in ratios])
		animalStr = ','.join(animals)
		
		ans1= round(((ratiopart/ratios[animal]))*ratios[animal2],2)
		ansp1=f'If a pet shop has {animalStr} in a ratio of {ratioStr}'
		ansp2=f'and there are {ratiopart} {animals[animal]}'
		ansp3=f'How many {animals[animal2]} are there?'
		ans=' '.join([ansp1,ansp2,ansp3]) 
		
		return(ans,ans1)
	@staticmethod
	def do_applyingRatios1(line):
		'''turn it into a whole number;find the increase/decrease then divide it by hcf'''
		x1,y1 =  round(random.uniform(1,10),2),round(random.uniform(1,10),2)
		x2,y2 =  random.randint(1,50),random.randint(1,50)
		weights = [0.25,0.25,0.25,0.25]
		r1,r2 = random.choices([x1,y1,x2,y2],weights,k=2)
		p1,p2=random.randint(1,99),random.randint(1,99)
		c1,c2 = random.choices(['increase','decrease'],k=2)
		
		q1=f'(School A) and (School B) are funded in the ratio of {r1}:{r2}'
		q2=f'A will get a {p1}% {c1}, B get a {p2}% {c2}. New ratio (simplest form):'
		
		if isinstance(r1,float) or isinstance(r2,float):
			r1=int(round(r1*100,2))
			r2=int(round(r2*100,2))
		
		if c1 == "increase":
			p1+=100
		else:
			p1=100-p1
		if c2 == "increase":
			p2+=100
		else:
			p2=100-p2
			
		r1=round((r1/100)*p1,2)*100
		r2=round((r2/100)*p2,2)*100
		
		hcf=math.gcd(int(r1),int(r2))
		ans1=f"{r1/hcf}:{r2/hcf}"
		
		ans='\n'.join([q1,q2])
		 
		
		return(ans,ans1)
	@staticmethod
	def do_applyingRatios2(line):
		'''method1=10kg, 4:1, 1:4 4/1 = 4*4 = 16-part 16*2kg = 32 - (1*2kg) = 30kg 
		method2=ratio1.part1*perpart/ratio2.part1*ratio2.part2-ratio1.part1*perpart
		'''
		kg = random.randint(1,100)
		r1= random.randint(1,10),random.randint(1,10)
		while r1[0] == r1[1]:
			r1= random.randint(1,10),random.randint(1,10)	
		r2= max(r1),min(r1)
		correctratio=min(r1),max(r1)
		perpart=kg / sum(r2)
		ans1=((((r2[0]/correctratio[0])*correctratio[1])*perpart)-(r2[1]*perpart))
		q1=f'Anisha makes up a {kg}kg mixture of cement using'
		q2=f' mortar and sand in the ratio of {r2[0]}:{r2[1]}'#doing this now
		q3=' She then reads the instructions again, and realises'
		q4=f' she has made a mistake and the ratio should be'
		q5=f' {correctratio[0]}:{correctratio[1]} '
		q6='How much sand does she have to add to get the correct proportions'
		q7=' of mortar and sand?'
		q=[q1,q2,q3,q4,q5,q6,q7]
		ans = ''.join(q)
		ans1=f' She has to add {round(ans1,2)}kg of sand' 
		return(ans,ans1)
functions().do_applyingRatios2('')


import sys
import inspect
from cmd import Cmd
from section1.section1 import Section1
from section2.section2 import Section2
from section1.part1 import functions
from extrabasics.extrabasics1 import Extrabasics1
from extrastats.extrastats1 import Extrastats1
import random
from Tools import tools
import math
class Score:	
	#increments score
	def __init__(self,func,q):
		self.question=func[0]
		res=self.answer((input(func[0])),func[1])
		global results
		if res is True:
			results+=1
		print(f'score: {results}/{q}')
	#checks if answer is right
	def answer(self,ans,ans1):
		if not isinstance(ans1,list) and ans == str(ans1):
			print('well done')
			return (True)
		elif isinstance(ans1,list) and 'order' not in self.question:
			ans = [int(x) for x in ans.rstrip().replace(" ","").split(',') if x.isdigit()]
			if all(x in ans for x in ans1) and len(ans)==len(ans1):
				print('well done')
				return (True)
			else:
				print(f'wrong, the answer is {ans1}')
		elif isinstance(ans1,list) and 'order' in self.question:
		
			ans = [str(x) for x in ans.rstrip().replace(" ","").split(',')]
			res_=True
			for n,i in enumerate(ans):
				
				if str(i) == str(ans1[n]):
					if res_!=False:
						res_=True
				else:
					res_=False
			if res_==True:
				print('well done')
			elif res_==False:
				print(f'wrong, the answer is {ans1}')		
			return(res_)
		else:
			print(f'wrong, the answer is {ans1}')


class Test(Section1,Section2,Extrabasics1,Extrastats1):
	def __init__(self):
		super().__init__()
		
		
	def preloop(self):
		self.number_of_questions = input('\nHow many questions: ')
		try:
			self.number_of_questions=int(self.number_of_questions)
		except:
			self.number_of_questions=str(random.randint(0,100))
		
		self.doc_header = "Type one of the sections below: "
		sections=str(inspect.getclasstree([self.__class__])).split(',')
		sections={x.split('.')[1] for x in sections if x.split('.')[1].startswith('section') or x.split('.')[1].startswith('extra')}
		
		print('\n')
		for n,x in enumerate(sections):
			n=n+1
			if n != len(sections):
				print(x,end=', ')
			elif n == len(sections):
				print(x)
				
		
		section=input("\nType one of the sections above or press enter for all sections: ")
		
		if not section.lower().startswith('section') and not section.lower().startswith('extra'):
			self.do_help('')
			self.section = 'self'
		elif section.lower().startswith('section') or section.lower().startswith('extra'):
			eval(f'{section.title()}().do_help("")'
			)
			self.section=section.title()
			
	def precmd(self,func):
		if str(func) == "" and self.section != "self":
			mods=[x for x in eval(f'{self.section}().__dir__()') if x.startswith('do_') and x!='do_help']
			for q in range(1,int(self.number_of_questions)+1):
				print(f'\nQuestion {q}:')
				mod = random.choice(mods)
				Score(eval(f'self.{mod}("")'),self.number_of_questions)
	
		elif str(func) == "" and self.section == "self":
			mods=[x for x in self.__dir__() if x.startswith('do_') and x!='do_help']
			for q in range(1,int(self.number_of_questions)+1):
				print(f'\nQuestion {q}:')
				mod = random.choice(mods)
				Score(eval(f'self.{mod}("")'),self.number_of_questions)
		elif not str(func).startswith("help"):
			for q in range(1,int(self.number_of_questions)+1):
				print(f'\nQuestion {q}:')
				Score(eval(f'self.do_{func}("")'),self.number_of_questions)
		elif func.split(' ')[0] == 'help' and len(func.split(' '))>1:
			self.do_help(f"{func.split()[1]}")
		else:
			self.do_help('')
		return(' ')
		'''
		elif str(func) == "generateTest" and self.section == "self":
				#comm=generateTest : to make a worksheet for random and non random questions 
				mods=[x for x in eval(f'{self.section}().__dir__()') if x.startswith('do_') and x!='do_help']
				question_list=[]
				for q in range(1,int(self.number_of_questions)+1):
					mod = random.choice(mods)
					question_=([eval(f'self.{mod}("")'),self.number_of_questions])
					question_list.append(question_)
				tools.toHtml().generateTest(question_list)
				sys.exit()
		'''	
results=0
###########
#Important#
###########
#remember to make a function to test on what stats test such as variance tests the spread of data
#also the program must be able to test on the formula for certain functions such as the formula for variance


#Version 2:
	#seperate printing from the logical functions
	#make different classes for each section
	#migrate to cmd module					
#write an html/spreadsheet of questions that are randomnly generated to be printed out
#need to add a "write the numbers as a word"
#want to add a timer for multiplication or add an arthmitic function
#maybe add an overall timer as an option
#add a range so that a topic, topic range or random can be selected
#add an individual timer for indv questions and and an overall timer
#add some worded questions and questions with irrelevant material
Test().cmdloop()

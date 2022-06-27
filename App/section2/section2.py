from cmd import Cmd
from section2.part1 import functions as p1
from section2.part2 import functions as p2
from section2.part3 import functions as p3
class Section2(Cmd,p1,p2,p3):
	def __init__(self):
		super().__init__()
		self.doc_header = "Type one of the below categories"
	'''
	def postcmd(self,question,func):
		print(question,func)T
	'''


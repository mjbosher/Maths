from cmd import Cmd
from section1.part1 import functions as p1
from section1.part2 import functions as p2
from section1.part3 import functions as p3
class Section1(Cmd,p1,p2,p3):
	def __init__(self):
		super().__init__()
		self.ruler = "-"
		self.doc_header = "Type one of the below categories or press Enter for a random selection"
	'''
	def postcmd(self,question,func):
		print(question,func)T
	'''


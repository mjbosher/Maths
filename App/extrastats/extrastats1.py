from cmd import Cmd
from extrastats.part1 import functions as p1

class Extrastats1(Cmd,p1):
	def __init__(self):
		super().__init__()
		self.ruler = "-"
		self.doc_header = "Type one of the below categories or press Enter for a random selection"
	'''
	def postcmd(self,question,func):
		print(question,func)T
	'''


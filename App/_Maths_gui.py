from PyQt5.QtWidgets import (QApplication,QMainWindow,QFrame,QPushButton,QGridLayout)
from extrabasics.extrabasics1 import Extrabasics1
from PyQt5 import QtCore
import sys
import itertools
import inspect
from section1.section1 import Section1
from section2.section2 import Section2
class App(QMainWindow):
	def __init__(self):
		super().__init__()
		content=Frames().contentFrame()
		self.setCentralWidget(content)
		self.show()
		
class Frames(Section1):
	@staticmethod
	def contentFrame():
		frame=QFrame()
		grid=QGridLayout()
		frame.setLayout(grid)
		sections = {name:QPushButton(name) for name in sorted(Content().classNames())}
		positions = [(i,j) for i in range(5) for j in range(4)]
		for position,name in zip(positions,sections):
			sections[name].setGeometry(QtCore.QRect(500, 150, 93, 28))  
			grid.addWidget(sections[name],*position)
			'''here need to somehow create a function in main to change the frame but self is no longer in the main app but lies with the called function'''
			#sections[name].clicked.connect(pass)
		return(frame)
		
		
class Content(Section1,Section2,Extrabasics1):
	@staticmethod
	def classNames():
		sections=str(inspect.getclasstree([Content().__class__])).split(',')
		sections={x.split('.')[-1].split("'")[0]
		 for x in sections if 'Section' in x or 'Extra' in x}
		return(sections)
		
class Test(Section1,Section2,Extrabasics1):
	def __init__(self):
		sections=str(inspect.getclasstree([self.__class__])).split(',')
		sections={x.split('.')[-1].split("'")[0]
		 for x in sections if 'Section' in x or 'Extra' in x}
		#mods={x.replace('do_',''):x for x in eval(f'{self.__dir__()}') if x.startswith('do_') and x!='do_help'}
		print(sections)
	
app = QApplication(sys.argv)
ui = App()
sys.exit(app.exec_())

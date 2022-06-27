from PyQt5.QtWidgets import (QWidget,QApplication,QMainWindow,QFrame,QPushButton,QGridLayout)
from PyQt5 import QtGui,QtCore
import sys
import itertools
import inspect
from section1.section1 import Section1
from section2.section2 import Section2
from extrabasics.extrabasics1 import Extrabasics1

class App(QWidget):
	def __init__(self):
		super().__init__()
		content=Frames().contentFrame()
		self.grid=QGridLayout()
		self.grid.addWidget(content)
		self.setLayout(self.grid)
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
			
			sections[name].clicked.connect(lambda:Console().print_(name))
		return(frame)
class Console:
	@staticmethod
	def print_(x):
		print(x)
class Content(Section1,Section2,Extrabasics1):
	@staticmethod
	def classNames():
		sections=str(inspect.getclasstree([Content().__class__])).split(',')
		sections={x.split('.')[-1].split("'")[0]
		 for x in sections if 'Section' in x or 'Extra' in x}
		return(sections)
				
app = QApplication(sys.argv)
ui = App()
sys.exit(app.exec_())

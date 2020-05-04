import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QCoreApplication
 
class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'GUI'
		self.left = 50
		self.top = 50
		self.width = 570
		self.height = 450
		self.initUI()
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		button1 = QPushButton('Elbow', self)
		button2 = QPushButton('Wrist', self)
		button1.setToolTip('Forearm Movements')
		button1.move(170,60) 
		button2.setToolTip('Hand Movements')
		button2.move(300,60) 
		button1.clicked.connect(self.on_click1)
		button2.clicked.connect(self.on_click2)
		label = QLabel('Analysis of EMG Signals to Replicate Arm Movements', self)
		label.move(130,20)
		self.show()
 
	@pyqtSlot()
	def on_click1(self):
		os.system('python elbow_gui.py')
		image.setPixmap(pixmap)
		image.move(70,110)
	def on_click2(self):
		os.system('python wrist_gui.py')
		image.setPixmap(pixmap)
		image.move(70,110)
	
 
if __name__ == '__main__':
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


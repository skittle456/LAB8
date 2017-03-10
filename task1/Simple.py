import PySide
import sys
from PySide.QtGui import *
from PySide.QtCore import *


class Simple(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple2 Drawing")
        self.rabbit = QImage("images/ rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([QPoint(70,100) , QPoint(100,110), QPoint(130,100),QPoint(100,150)])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon([QPoint(50,200),QPoint(150,200),QPoint(100,400)])

        p.drawImage(QRect(200,100,320,320), self.rabbit)
        p.end()

'''
class Simple1(Simple):
'''

'''
class Simple2(Simple):
'''


class Simple3(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Ham Drawing")
        self.rabbit = QImage("images/rabbit.png")
        

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
       
        p.setPen(QColor(250,250,250))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100), QPoint(100,110,),
            QPoint(130,100), QPoint(100,150),
            ])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon([
            QPoint(50,200), QPoint(150,200),QPoint(100,400),
            ])

        p.drawImage(QRect(200,100,320,320),self.rabbit)
        p.drawImage(QRect(520,100,320,320),self.rabbit)
        p.end()


app = QApplication(sys.argv)
#s = Simple3()
s = Simple2()
s.show()
app.exec_()

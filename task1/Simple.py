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

class Simple1(Simple):
    def __init__(self):
        super().__init__()
        
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

        p.drawPolygon([QPoint(750,200),QPoint(150,200),QPoint(100,400)])

        p.drawImage(QRect(200,100,320,320), self.rabbit)
        p.end()

class Simple2(Simple):
    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(100,100,100))
        p.setBrush(QColor(0,0,255))
        p.drawPolygon([QPoint(70,100) , QPoint(100,110), QPoint(130,100),QPoint(100,150)])

        p.setPen(QColor(200,127,0))
        p.setBrush(QColor(200,127,0))
        p.drawPie(50,150,100,100,0,180*16)

        p.drawPolygon([QPoint(50,200),QPoint(150,200),QPoint(100,400)])

        p.drawImage(QRect(200,100,320,320), self.rabbit)
        p.end()    


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
s1  =Simple1()
s2 = Simple2()
s3 = Simple3()

s1.show()
s2.show()
s3.show()

app.exec_()

'''#button
class Paint(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        
        layout = QVBoxLayout()
        layout.addStretch(1)
        self.setWindowTitle('Drawing')
        self.setMinimumSize(600,600)
        draw_label = QLabel("\t\t\tDrag the mouse to draw")
        layout.addWidget(draw_label)
        
        #layout.addStretch(1)
        clear_button = QPushButton("Clear")
        layout.addWidget(clear_button)
        clear_button.clicked.connect(self.clear_screen)
        clear_button.setGeometry(300,300,300,300)
        #layout.addStretch(1)
        self.setLayout(layout)

    def clear_screen(self):
        "Insert Code Here"
        print("Clear")
'''


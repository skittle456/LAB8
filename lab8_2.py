import sys
from PySide import QtGui
from PySide.QtCore import*
from PySide.QtGui import*

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
        
def main():
    app = QApplication(sys.argv)

    w = Paint()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

orm_class = uic.loadUiType("baseball.ui")[0]

class BaseBall(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = BaseBall()
    myWindow.show()
    app.exec_()

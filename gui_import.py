import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("baseball.ui")[0]

class BaseBall(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initialize()
        self.butto.clicked.connect(self.check_answer)

    def initialize(self):
        self.inning = 1
        self.inning_label.setText("1회")
        while True:
            target = str(randrange(1000, 9999))
            result = check_validity(target, False)
            if (result):
                self.target = target
                break

    def check_answer(self):
        self.lineEdit.text()
        strike = 0
        ball = 0
        for i in range(4):


def check_validity(in_string, init=True):
    if not(in_string.isdigit()):
        if (init):
            print("숫자가 아닙니다")
        return False
    elif len(in_string) != 4:
        if (init):
            print("길이가 4가 아닙니다")
        return False
    else:
        for i in range(3):
            for j in range(i+1, 4):
                if in_string[i] == in_string[j]:
                    if (init):
                        print("중복되는 수가 있습니다")
                    return False
    return True

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = BaseBall()
    myWindow.show()
    app.exec_()

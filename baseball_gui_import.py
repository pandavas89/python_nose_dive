import sys
from random import randint

from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("baseball.ui")[0]

class BaseBall(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.check_button.clicked.connect(self.check_validity)
        self.initialize()


    def initialize(self):
        self.counter = 1
        self.generate_goal()
        self.result_textbox.clear()
        self.inning_label.setText("1회")

    def generate_goal(self):
        valid_check = False
        while not(valid_check):
            number = str(randint(1000, 9999))
            valid_check = self.check_goal(number)
            self.goal = number

    def check_goal(self, number):
        for i in range(3):
            for j in range(i+1, 4):
                if (number[i] == number[j]):
                    return False
        return True

    def check_validity(self):
        number = self.input_lineedit.text()
        if not(number.isdigit()):
            self.statusbar.text = "입력값이 숫자가 아닙니다"
            return
        elif len(number) != 4:
            self.statusbar.text = "입력값의 길이가 4가 아닙니다"
            return
        else:
            for i in range(3):
                for j in range(i+1, 4):
                    if (number[i] == number[j]):
                        self.statusbar.text = "중복되는 숫자가 있습니다"
                        return
        self.evaluate(str(number))

    def evaluate(self, number):
        strike = 0
        ball = 0
        for i in range(4):
            if number[i] in self.goal:
                if number[i] == self.goal[i]:
                    strike += 1
                else:
                    ball += 1
        if strike > 3:
            self.result_textbox.append("WIN!")
            self.initialize()
        elif self.counter > 8:
            self.result_textbox.append("LOSE!")
            self.initialize()
        else:
            self.result_textbox.append("%s회 : %s (%dB %dS)" %(self.counter, number, ball, strike))
            self.counter += 1

        self.inning_label.setText("%d회"%self.counter)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = BaseBall()
    myWindow.show()
    app.exec_()

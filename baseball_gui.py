# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baseball.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from random import randint

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.check_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_button.setGeometry(QtCore.QRect(180, 448, 93, 30))
        self.check_button.setObjectName("check_button")
        self.check_button.clicked.connect(self.check_validity)

        self.input_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.input_lineedit.setGeometry(QtCore.QRect(50, 450, 113, 21))
        self.input_lineedit.setObjectName("input_lineedit")

        self.result_textbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.result_textbox.setGeometry(QtCore.QRect(310, 10, 256, 471))
        self.result_textbox.setObjectName("result_textbox")

        self.inning_label = QtWidgets.QLabel(self.centralwidget)
        self.inning_label.setGeometry(QtCore.QRect(30, 20, 241, 51))
        self.inning_label.setAlignment(QtCore.Qt.AlignCenter)
        self.inning_label.setObjectName("inning_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.initialize()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.check_button.setText(_translate("MainWindow", "확인"))
        self.inning_label.setText(_translate("MainWindow", "TextLabel"))

    def __init__(self):
        super().__init__()

    def initialize(self):
        self.counter = 1
        self.generate_goal()
        self.result_textbox.clear()

    def generate_goal(self):
        valid_check = False
        while not(valid_check):
            number = randint(1000, 9999)
            valid_check = self.check_goal(str(number))
            self.goal = str(number)

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

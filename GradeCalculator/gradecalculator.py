# Form implementation generated from reading ui file 'gradecalculator.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblScore = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblScore.setGeometry(QtCore.QRect(130, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblScore.setFont(font)
        self.lblScore.setObjectName("lblScore")
        self.txtScore = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtScore.setGeometry(QtCore.QRect(260, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtScore.setFont(font)
        self.txtScore.setObjectName("txtScore")
        self.btnCalculate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCalculate.setGeometry(QtCore.QRect(250, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btnCalculate.setFont(font)
        self.btnCalculate.setObjectName("btnCalculate")
        self.lblGrade = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblGrade.setGeometry(QtCore.QRect(130, 310, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblGrade.setFont(font)
        self.lblGrade.setObjectName("lblGrade")
        self.txtGrade = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtGrade.setGeometry(QtCore.QRect(260, 320, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtGrade.setFont(font)
        self.txtGrade.setObjectName("txtGrade")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #When calculate grade button is clicked execute the grade_calculator function
        self.btnCalculate.clicked.connect(self.grade_calculator)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblScore.setText(_translate("MainWindow", "Enter Student Score"))
        self.btnCalculate.setText(_translate("MainWindow", "Calculate Grade"))
        self.lblGrade.setText(_translate("MainWindow", "Student Grade"))

    def grade_calculator(self):
        input_score = self.txtScore.toPlainText()
        grade = ""
        msg = QMessageBox()
        msg.setWindowTitle("Grade Calculator")
        if(input_score.isdigit()):
            input_score = int(input_score)
            if(input_score < 101):
                if(input_score >= 90):
                    grade = "A"
                elif(input_score >= 80):
                    grade = "B"
                elif(input_score >= 70):
                    grade = "C"
                elif(input_score >= 60):
                    grade = "D"
                else:
                    grade = "F"
                self.txtGrade.setText(grade)                
            else:
                msg.setText("Please enter a score between 0 and 100")
                msg.exec()
        else:             
                msg.setText("Please enter a valid score")
                msg.exec()
                      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

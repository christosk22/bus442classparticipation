# Form implementation generated from reading ui file 'averagescores.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblScore = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblScore.setGeometry(QtCore.QRect(30, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblScore.setFont(font)
        self.lblScore.setObjectName("lblScore")
        self.txtScore = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtScore.setGeometry(QtCore.QRect(150, 80, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.txtScore.setFont(font)
        self.txtScore.setObjectName("txtScore")
        self.btnAddScore = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAddScore.setGeometry(QtCore.QRect(170, 170, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btnAddScore.setFont(font)
        self.btnAddScore.setObjectName("btnAddScore")
        self.btnAverage = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAverage.setGeometry(QtCore.QRect(170, 260, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btnAverage.setFont(font)
        self.btnAverage.setObjectName("btnAverage")
        self.btnClear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(170, 360, 75, 24))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.lstScores = QtWidgets.QListWidget(parent=self.centralwidget)
        self.lstScores.setGeometry(QtCore.QRect(360, 90, 201, 351))
        self.lstScores.setObjectName("lstScores")
        self.lblStudentScores = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblStudentScores.setGeometry(QtCore.QRect(370, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lblStudentScores.setFont(font)
        self.lblStudentScores.setObjectName("lblStudentScores")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Create an empty list to store each student score
        self.student_scores_lst = []
        
        self.btnAddScore.clicked.connect(self.add_score)
        self.btnAverage.clicked.connect(self.calculate_average)
        self.btnClear.clicked.connect(self.clear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblScore.setText(_translate("MainWindow", "Enter Student Score"))
        self.btnAddScore.setText(_translate("MainWindow", "Add Score"))
        self.btnAverage.setText(_translate("MainWindow", "Average"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.lblStudentScores.setText(_translate("MainWindow", "Student Scores"))
        
    def add_score(self):
        if(self.txtScore.text().isnumeric()):
            #convert string input to float
            student_score = float(self.txtScore.text())
            #append the new score to the list
            self.student_scores_lst.append(student_score)
            #add the score to the list widget
            self.lstScores.addItem(str(student_score))
            
            self.txtScore.clear()
            self.txtScore.setFocus()
        else:
            #create a new message box instance
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Average Scores")
            msg.setText("Invalid student score")
            msg.exec()
            self.txtScore.clear()
            
    def calculate_average(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Average Scores")
        if(len(self.student_scores_lst) > 0):
            average_value = sum(self.student_scores_lst)/len(self.student_scores_lst)
            msg.setText("Average of all scores: " + str(average_value))
        else:
            msg.setText("No student scores added")
            
        msg.exec()
        
    def clear(self):
        self.txtScore.clear()
        self.lstScores.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

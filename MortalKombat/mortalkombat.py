# Form implementation generated from reading ui file 'mortalkombat.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

class Player:
    
    def __init__(self, name, speed, power, agility):
        self.player_name = name
        self.player_speed = speed
        self.player_power = power
        self.player_agility = agility
        
    def modify_stats(self, speed, power, agility):
        self.player_speed = speed
        self.player_power = power
        self.player_agility = agility

class Ui_mortalKombat(object):
    def setupUi(self, mortalKombat):
        mortalKombat.setObjectName("mortalKombat")
        mortalKombat.resize(1094, 801)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        mortalKombat.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=mortalKombat)
        self.centralwidget.setObjectName("centralwidget")
        self.tbPlayerCreation = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tbPlayerCreation.setGeometry(QtCore.QRect(10, 10, 1021, 611))
        self.tbPlayerCreation.setObjectName("tbPlayerCreation")
        self.tabCreatePlayer = QtWidgets.QWidget()
        self.tabCreatePlayer.setObjectName("tabCreatePlayer")
        self.lblName = QtWidgets.QLabel(parent=self.tabCreatePlayer)
        self.lblName.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.lblName.setObjectName("lblName")
        self.txtName = QtWidgets.QLineEdit(parent=self.tabCreatePlayer)
        self.txtName.setGeometry(QtCore.QRect(140, 40, 113, 22))
        self.txtName.setObjectName("txtName")
        self.lblSpeed = QtWidgets.QLabel(parent=self.tabCreatePlayer)
        self.lblSpeed.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.lblSpeed.setObjectName("lblSpeed")
        self.txtSpeed = QtWidgets.QLineEdit(parent=self.tabCreatePlayer)
        self.txtSpeed.setGeometry(QtCore.QRect(140, 100, 113, 22))
        self.txtSpeed.setObjectName("txtSpeed")
        self.lblPower = QtWidgets.QLabel(parent=self.tabCreatePlayer)
        self.lblPower.setGeometry(QtCore.QRect(10, 150, 121, 31))
        self.lblPower.setObjectName("lblPower")
        self.txtPower = QtWidgets.QLineEdit(parent=self.tabCreatePlayer)
        self.txtPower.setGeometry(QtCore.QRect(140, 150, 113, 22))
        self.txtPower.setObjectName("txtPower")
        self.lblAgility = QtWidgets.QLabel(parent=self.tabCreatePlayer)
        self.lblAgility.setGeometry(QtCore.QRect(10, 200, 121, 31))
        self.lblAgility.setObjectName("lblAgility")
        self.txtAgility = QtWidgets.QLineEdit(parent=self.tabCreatePlayer)
        self.txtAgility.setGeometry(QtCore.QRect(140, 210, 113, 22))
        self.txtAgility.setObjectName("txtAgility")
        self.btnCreatePlayer = QtWidgets.QPushButton(parent=self.tabCreatePlayer)
        self.btnCreatePlayer.setGeometry(QtCore.QRect(140, 270, 111, 31))
        self.btnCreatePlayer.setObjectName("btnCreatePlayer")
        self.tbPlayerCreation.addTab(self.tabCreatePlayer, "")
        self.tabModifyStats = QtWidgets.QWidget()
        self.tabModifyStats.setObjectName("tabModifyStats")
        self.lstCreatedPlayers = QtWidgets.QListWidget(parent=self.tabModifyStats)
        self.lstCreatedPlayers.setGeometry(QtCore.QRect(320, 90, 256, 192))
        self.lstCreatedPlayers.setObjectName("lstCreatedPlayers")
        self.lblCreatedPlayers = QtWidgets.QLabel(parent=self.tabModifyStats)
        self.lblCreatedPlayers.setGeometry(QtCore.QRect(400, 50, 121, 31))
        self.lblCreatedPlayers.setObjectName("lblCreatedPlayers")
        self.lblPlayerName = QtWidgets.QLabel(parent=self.tabModifyStats)
        self.lblPlayerName.setGeometry(QtCore.QRect(140, 340, 121, 31))
        self.lblPlayerName.setObjectName("lblPlayerName")
        self.lblModifySpeed = QtWidgets.QLabel(parent=self.tabModifyStats)
        self.lblModifySpeed.setGeometry(QtCore.QRect(280, 340, 121, 31))
        self.lblModifySpeed.setObjectName("lblModifySpeed")
        self.lblModifyPower = QtWidgets.QLabel(parent=self.tabModifyStats)
        self.lblModifyPower.setGeometry(QtCore.QRect(420, 340, 121, 31))
        self.lblModifyPower.setObjectName("lblModifyPower")
        self.lblModifyAgility = QtWidgets.QLabel(parent=self.tabModifyStats)
        self.lblModifyAgility.setGeometry(QtCore.QRect(560, 340, 121, 31))
        self.lblModifyAgility.setObjectName("lblModifyAgility")
        self.txtPlayerName = QtWidgets.QLineEdit(parent=self.tabModifyStats)
        self.txtPlayerName.setGeometry(QtCore.QRect(120, 390, 113, 22))
        self.txtPlayerName.setReadOnly(True)
        self.txtPlayerName.setObjectName("txtPlayerName")
        self.txtModifySpeed = QtWidgets.QLineEdit(parent=self.tabModifyStats)
        self.txtModifySpeed.setGeometry(QtCore.QRect(270, 390, 113, 22))
        self.txtModifySpeed.setReadOnly(True)
        self.txtModifySpeed.setObjectName("txtModifySpeed")
        self.txtModifyPower = QtWidgets.QLineEdit(parent=self.tabModifyStats)
        self.txtModifyPower.setGeometry(QtCore.QRect(410, 390, 113, 22))
        self.txtModifyPower.setReadOnly(True)
        self.txtModifyPower.setObjectName("txtModifyPower")
        self.txtModifyAgility = QtWidgets.QLineEdit(parent=self.tabModifyStats)
        self.txtModifyAgility.setGeometry(QtCore.QRect(550, 390, 113, 22))
        self.txtModifyAgility.setReadOnly(True)
        self.txtModifyAgility.setObjectName("txtModifyAgility")
        self.btnModifyStats = QtWidgets.QPushButton(parent=self.tabModifyStats)
        self.btnModifyStats.setGeometry(QtCore.QRect(390, 460, 111, 31))
        self.btnModifyStats.setObjectName("btnModifyStats")
        self.tbPlayerCreation.addTab(self.tabModifyStats, "")
        mortalKombat.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mortalKombat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 21))
        self.menubar.setObjectName("menubar")
        mortalKombat.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mortalKombat)
        self.statusbar.setObjectName("statusbar")
        mortalKombat.setStatusBar(self.statusbar)

        self.retranslateUi(mortalKombat)
        self.tbPlayerCreation.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mortalKombat)
        
        self.created_players = {}
        self.btnCreatePlayer.clicked.connect(self.create_player)
        self.lstCreatedPlayers.itemClicked.connect(self.display_stats)
        
        self.btnModifyStats.clicked.connect(self.modify_stats)

    def retranslateUi(self, mortalKombat):
        _translate = QtCore.QCoreApplication.translate
        mortalKombat.setWindowTitle(_translate("mortalKombat", "Mortal Kombat"))
        self.lblName.setText(_translate("mortalKombat", "Enter Player Name"))
        self.lblSpeed.setText(_translate("mortalKombat", "Enter Player Speed"))
        self.lblPower.setText(_translate("mortalKombat", "Enter Player Power"))
        self.lblAgility.setText(_translate("mortalKombat", "Enter Player Agility"))
        self.btnCreatePlayer.setText(_translate("mortalKombat", "Create Player"))
        self.tbPlayerCreation.setTabText(self.tbPlayerCreation.indexOf(self.tabCreatePlayer), _translate("mortalKombat", "Create Player"))
        self.lblCreatedPlayers.setText(_translate("mortalKombat", "Players Created"))
        self.lblPlayerName.setText(_translate("mortalKombat", "Player Name"))
        self.lblModifySpeed.setText(_translate("mortalKombat", "Player Speed"))
        self.lblModifyPower.setText(_translate("mortalKombat", "Player Power"))
        self.lblModifyAgility.setText(_translate("mortalKombat", "Player Agility"))
        self.btnModifyStats.setText(_translate("mortalKombat", "Modify Stats"))
        self.tbPlayerCreation.setTabText(self.tbPlayerCreation.indexOf(self.tabModifyStats), _translate("mortalKombat", "Modify Stats"))

    def create_player(self):
        name = self.txtName.text()
        speed = self.txtSpeed.text()
        power = self.txtPower.text()
        agility = self.txtAgility.text()
        
        player_object = Player(name, speed, power, agility)
        self.created_players[name] = player_object
        self.lstCreatedPlayers.addItem(name)
        
    def display_stats(self,item):
        selected_player = item.text()
        player_object = self.created_players.get(selected_player)
        self.txtPlayerName.setText(player_object.player_name)
        self.txtModifySpeed.setText(player_object.player_speed)
        self.txtModifyPower.setText(player_object.player_power)
        self.txtModifyAgility.setText(player_object.player_agility)
        
    def modify_stats(self):
        name = self.txtPlayerName.text()
        speed = self.txtModifySpeed.text()
        power = self.txtModifyPower.text()
        agility = self.txtModifyAgility.text()
        player_object = self.created_players.get(name)
        player_object.modify_stats(speed,power,agility)
        self.created_players[name] = player_object

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mortalKombat = QtWidgets.QMainWindow()
    ui = Ui_mortalKombat()
    ui.setupUi(mortalKombat)
    mortalKombat.show()
    sys.exit(app.exec())

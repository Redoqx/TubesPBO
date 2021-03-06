import Lokasi,Tampil
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(800, 600)
        Menu.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.Login_view = QtWidgets.QGroupBox(self.centralwidget)
        self.Login_view.setGeometry(QtCore.QRect(50, 60, 701, 481))
        self.Login_view.setAutoFillBackground(False)
        self.Login_view.setStyleSheet("background-color: rgb(0, 255, 127);\n"
"color: qlineargradient(spread:reflect, x1:1, y1:1, x2:1, y2:0.494, stop:0 rgba(54, 54, 54, 199), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.Login_view.setTitle("")
        self.Login_view.setObjectName("Login_view")
        self.label = QtWidgets.QLabel(self.Login_view)
        self.label.setGeometry(QtCore.QRect(170, 50, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.Login_view)
        self.frame.setGeometry(QtCore.QRect(70, 220, 561, 201))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Gedung = QtWidgets.QPushButton(self.frame)
        self.Gedung.setGeometry(QtCore.QRect(20, 110, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Gedung.setFont(font)
        self.Gedung.setStyleSheet("color: rgb(65, 65, 65);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.Gedung.setObjectName("Gedung")
        self.Ruang = QtWidgets.QPushButton(self.frame)
        self.Ruang.setGeometry(QtCore.QRect(20, 30, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Ruang.setFont(font)
        self.Ruang.setStyleSheet("color: rgb(65, 65, 65);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.Ruang.setObjectName("Ruang")
        self.label_2 = QtWidgets.QLabel(self.Login_view)
        self.label_2.setGeometry(QtCore.QRect(80, 196, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.LogOutButton = QtWidgets.QPushButton(self.Login_view)
        self.LogOutButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.LogOutButton.setStyleSheet("background-color: transparent;")
        self.LogOutButton.setText("")
        self.LogOutButton.setObjectName("LogOutButton")
        self.label_3 = QtWidgets.QLabel(self.Login_view)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icon/LogOut.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.LogOutButton.raise_()
        Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

        #code here
        self.Gedung.clicked.connect(lambda: self.Lihatlah(1,Menu))
        self.Ruang.clicked.connect(lambda: self.Lihatlah(2,Menu))

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.label.setText(_translate("Menu", "MENU"))
        self.Gedung.setText(_translate("Menu", "Gedung"))
        self.Ruang.setText(_translate("Menu", "Ruang"))
        self.label_2.setText(_translate("Menu", "Lihat Data invetaris berdasarkan:"))

    def Lihatlah(self, pilih, Menu):
        self.SubMenu = QtWidgets.QMainWindow()
        self.ui = Lokasi.Ui_PilihLokasi()
        self.ui.setupUi(self.SubMenu)
        self.ui.setUpin(pilih)
        self.SubMenu.show()
        self.ui.Ruang.clicked.connect(lambda: self.getLoc(pilih, Menu))

    def getLoc(self, pilih, AdminMenu):
        self.Loc = self.ui.comboBox.currentText()
        if self.Loc == "-Pilih Lokasi-":
            self.show_Popup("Harap pilih lokasi terlebih dahulu!")
            return 0
        self.SubMenu.hide()
        self.ui = Tampil.Ui_Tampilkan()
        self.ui.setupUi(self.SubMenu)
        if pilih == 0:
            self.ui.setUpin("BARANG",self.Loc)
        if pilih == 1:
            self.ui.setUpin("GEDUNG",self.Loc)
        if pilih == 2:
            self.ui.setUpin("RUANG",self.Loc)
        self.SubMenu.show()
        AdminMenu.hide()
        self.ui.BackButton.clicked.connect(lambda: self.RiseMeUp(AdminMenu))

    def RiseMeUp(self, AdminMenu):
        AdminMenu.show()
        self.SubMenu.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())

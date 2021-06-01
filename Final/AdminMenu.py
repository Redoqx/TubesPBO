import Peminjaman,Pengembalian,MenuTampil,TampilAdmin,Akun,Lokasi,Perolehan
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_AdminMenu(object):
    def setupUi(self, AdminMenu):
        AdminMenu.setObjectName("AdminMenu")
        AdminMenu.resize(800, 600)
        AdminMenu.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(AdminMenu)
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
        self.frame.setGeometry(QtCore.QRect(70, 160, 561, 271))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.Peminjaman = QtWidgets.QPushButton(self.frame)
        self.Peminjaman.setGeometry(QtCore.QRect(50, 30, 221, 61))
        self.Peminjaman.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.Peminjaman.setObjectName("Peminjaman")

        self.Pengembalian = QtWidgets.QPushButton(self.frame)
        self.Pengembalian.setGeometry(QtCore.QRect(290, 30, 221, 61))
        self.Pengembalian.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.Pengembalian.setObjectName("Pengembalian")

        self.LihatInvestaris = QtWidgets.QPushButton(self.frame)
        self.LihatInvestaris.setGeometry(QtCore.QRect(50, 110, 221, 61))
        self.LihatInvestaris.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.LihatInvestaris.setObjectName("LihatInvestaris")

        self.KelolaAkun = QtWidgets.QPushButton(self.frame)
        self.KelolaAkun.setGeometry(QtCore.QRect(290, 110, 221, 61))
        self.KelolaAkun.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.KelolaAkun.setObjectName("KelolaAkun")

        self.TerimaInventaris = QtWidgets.QPushButton(self.frame)
        self.TerimaInventaris.setGeometry(QtCore.QRect(170, 190, 221, 61))
        self.TerimaInventaris.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.TerimaInventaris.setObjectName("TerimaInventaris")

        self.label_2 = QtWidgets.QLabel(self.Login_view)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icon/LogOut.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.LogOutButton = QtWidgets.QPushButton(self.Login_view)
        self.LogOutButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.LogOutButton.setStyleSheet("background-color: transparent;")
        self.LogOutButton.setText("")
        self.LogOutButton.setObjectName("LogOutButton")
        AdminMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminMenu)
        QtCore.QMetaObject.connectSlotsByName(AdminMenu)

        #code here
        self.Peminjaman.pressed.connect(lambda: self.Pinjamkan(AdminMenu))
        self.Pengembalian.pressed.connect(lambda: self.Terima(AdminMenu))
        self.LihatInvestaris.pressed.connect(lambda: self.Lihatkan(AdminMenu))
        self.KelolaAkun.pressed.connect(lambda: self.Kelola(AdminMenu))
        self.TerimaInventaris.pressed.connect(lambda: self.Peroleh(AdminMenu))

    def retranslateUi(self, AdminMenu):
        _translate = QtCore.QCoreApplication.translate
        AdminMenu.setWindowTitle(_translate("AdminMenu", "Admin Menu"))
        self.label.setText(_translate("AdminMenu", "ADMIN MENU"))
        self.LihatInvestaris.setText(_translate("AdminMenu", "Lihat Inventaris"))
        self.KelolaAkun.setText(_translate("AdminMenu", "Kelola Akun"))
        self.Peminjaman.setText(_translate("AdminMenu", "Peminjaman"))
        self.Pengembalian.setText(_translate("AdminMenu", "Pengembalian"))
        self.TerimaInventaris.setText(_translate("AdminMenu", "Terima Inventaris"))

    def Pinjamkan(self, AdminMenu):
        self.SubMenu = QtWidgets.QMainWindow()
        self.ui = Peminjaman.Ui_Peminjaman()
        self.ui.setupUi(self.SubMenu)
        self.SubMenu.show()
        AdminMenu.hide()
        self.ui.BackButton.clicked.connect(lambda: self.RiseMeUp(AdminMenu))

    def Terima(self, AdminMenu):
        self.SubMenu = QtWidgets.QMainWindow()
        self.ui = Pengembalian.Ui_Pengembalian()
        self.ui.setupUi(self.SubMenu)
        self.SubMenu.show()
        AdminMenu.hide()
        self.ui.BackButton.clicked.connect(lambda: self.RiseMeUp(AdminMenu))

    def Lihatkan(self, AdminMenu):
        self.SubMenu = QtWidgets.QMainWindow()
        self.ui = MenuTampil.Ui_MenuTampil()
        self.ui.setupUi(self.SubMenu)
        self.SubMenu.show()
        # self.ui.Barang.clicked.connect(lambda: self.Lihatlah(0,AdminMenu))
        self.ui.Gedung.clicked.connect(lambda: self.Lihatlah(1,AdminMenu))
        self.ui.Ruang.clicked.connect(lambda: self.Lihatlah(2,AdminMenu))
        # AdminMenu.hide()

    def Lihatlah(self, pilih, AdminMenu):
        self.SubMenu.hide()
        self.ui = Lokasi.Ui_PilihLokasi()
        self.ui.setupUi(self.SubMenu)
        self.ui.setUpin(pilih)
        self.SubMenu.show()
        self.ui.Ruang.clicked.connect(lambda: self.getLoc(pilih, AdminMenu))

    def getLoc(self, pilih, AdminMenu):
        self.Loc = self.ui.comboBox.currentText()
        if self.Loc == "-Pilih Lokasi-":
            self.show_Popup("Harap pilih lokasi terlebih dahulu!")
            return 0
        self.SubMenu.hide()
        self.ui = TampilAdmin.Ui_Tampilkan()
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

    def Kelola(self, AdminMenu):
        self.SubMenu = QtWidgets.QMainWindow()
        self.ui = Akun.Ui_KelolaAkun()
        self.ui.setupUi(self.SubMenu)
        self.ui.setUpin()
        self.SubMenu.show()
        AdminMenu.hide()
        self.ui.BackButton.clicked.connect(lambda: self.RiseMeUp(AdminMenu))

    def Peroleh(self, AdminMenu):
        self.SubMenu = QtWidgets.QMainWindow()
        self.ui = Perolehan.Ui_Perolehan()
        self.ui.setupUi(self.SubMenu)
        self.SubMenu.show()
        AdminMenu.hide()
        self.ui.BackButton.clicked.connect(lambda: self.RiseMeUp(AdminMenu))

    def RiseMeUp(self, AdminMenu):
        AdminMenu.show()
        self.SubMenu.hide()

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText(message)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminMenu = QtWidgets.QMainWindow()
    ui = Ui_AdminMenu()
    ui.setupUi(AdminMenu)
    AdminMenu.show()
    sys.exit(app.exec_())

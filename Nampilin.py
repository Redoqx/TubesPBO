# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Nampilin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import Tampilan_Text
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from prettytable import PrettyTable

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()


class Ui_InventarisGedung(object):
    def setupUi(self, InventarisGedung):
        InventarisGedung.setObjectName("InventarisGedung")
        InventarisGedung.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(InventarisGedung)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 70, 671, 441))
        self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(150, 20, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(50, 100, 571, 271))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Pilih_Gedung = QtWidgets.QComboBox(self.frame)
        self.Pilih_Gedung.setGeometry(QtCore.QRect(280, 100, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std")
        font.setPointSize(12)
        self.Pilih_Gedung.setFont(font)
        self.Pilih_Gedung.setObjectName("Pilih_Gedung")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.Pilih_Gedung.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 215);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Input = QtWidgets.QPushButton(self.groupBox)
        self.Input.setGeometry(QtCore.QRect(510, 320, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
        self.Input.setSizePolicy(sizePolicy)
        self.Input.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"gridline-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.Input.setAutoDefault(False)
        self.Input.setDefault(False)
        self.Input.setFlat(False)
        self.Input.setObjectName("Input")
        self.BackButton = QtWidgets.QPushButton(self.groupBox)
        self.BackButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setKerning(False)
        self.BackButton.setFont(font)
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.BackButton.setMouseTracking(False)
        self.BackButton.setAutoFillBackground(False)
        self.BackButton.setStyleSheet("color: rgb(170, 255, 255);\n"
"background-color: transparent;\n"
"")
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")
        self.BackIcon = QtWidgets.QLabel(self.groupBox)
        self.BackIcon.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.BackIcon.setText("")
        self.BackIcon.setPixmap(QtGui.QPixmap("icon/BackIcon.png"))
        self.BackIcon.setScaledContents(True)
        self.BackIcon.setObjectName("BackIcon")
        self.label.raise_()
        self.frame.raise_()
        self.Input.raise_()
        self.BackIcon.raise_()
        self.BackButton.raise_()
        InventarisGedung.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InventarisGedung)
        self.statusbar.setObjectName("statusbar")
        InventarisGedung.setStatusBar(self.statusbar)

        self.retranslateUi(InventarisGedung)
        QtCore.QMetaObject.connectSlotsByName(InventarisGedung)

        #code here
        print(self.username)

        #Nginput
        self.Input.pressed.connect(lambda: self.Inputin(InventarisGedung))

    def retranslateUi(self, InventarisGedung):
        _translate = QtCore.QCoreApplication.translate
        InventarisGedung.setWindowTitle(_translate("InventarisGedung", "Daftar Inventaris Gedung"))
        self.label.setText(_translate("InventarisGedung", "Daftar Inventaris"))
        self.Pilih_Gedung.setCurrentText(_translate("InventarisGedung", "A"))
        self.Pilih_Gedung.setItemText(0, _translate("InventarisGedung", "A"))
        self.Pilih_Gedung.setItemText(1, _translate("InventarisGedung", "B"))
        self.Pilih_Gedung.setItemText(2, _translate("InventarisGedung", "C"))
        self.Pilih_Gedung.setItemText(3, _translate("InventarisGedung", "D"))
        self.Pilih_Gedung.setItemText(4, _translate("InventarisGedung", "E"))
        self.Pilih_Gedung.setItemText(5, _translate("InventarisGedung", "F"))
        self.Pilih_Gedung.setItemText(6, _translate("InventarisGedung", "GKU"))
        self.Pilih_Gedung.setItemText(7, _translate("InventarisGedung", "Labtek1"))
        self.Pilih_Gedung.setItemText(8, _translate("InventarisGedung", "Labtek2"))
        self.Pilih_Gedung.setItemText(9, _translate("InventarisGedung", "Labtek3"))
        self.label_2.setText(_translate("InventarisGedung", "Pilih Gedung"))
        self.Input.setText(_translate("InventarisGedung", "Input"))

    def getMeAName(self,username):
        self.username=username

    def Inputin(self,InventarisGedung):
        #terima data
        Gedung = self.Pilih_Gedung.currentText()
        perintah = f"select Nama_Pegawai,ID_Barang,Jumlah_barang,Tgl_Peminjaman,Tgl_Pengembalian, No_Ruangan from peminjaman LEFT OUTER JOIN pegawai on peminjaman.id_peminjam = pegawai.nip where Gedung = '{Gedung}'"
        try:
            mycursor.execute(perintah)
            tampilan = mycursor.fetchall()
            if not tampilan:
                self.show_Popup("Tidak ada inventaris di gedung ini")
            else:
                self.x = PrettyTable(['Nama_Pegawai','ID_Barang','Jumlah_barang','Tgl_Peminjaman','Tgl_Pengembalian','No_Ruangan'])
                for j in tampilan:
                    self.x.add_row(j)
                self.x = str(self.x)
                self.x = f'Daftar Inventaris Gedung {Gedung}:\n'+self.x

                self.Tampilkan(InventarisGedung)
        except mysql.connector.Error as error:
            self.show_Popup(f'Gagal Mengunggah Data Peminjaman\nError Code\n{error}')

    def Tampilkan(self,InventarisGedung):
        print("Program akan menerima barang")
        pass
        self.Tampilan = QtWidgets.QMainWindow()
        self.ui = Tampilan_Text.Ui_Tampilan_Text()
        self.ui.setupUi(self.Tampilan)
        self.ui.Tampilin(self.x)
        self.Tampilan.show()
        InventarisGedung.hide()
        self.ui.BackButton.clicked.connect(lambda: self.Muncullah(InventarisGedung))

    def Muncullah(self,InventarisGedung):
        self.Tampilan.hide()
        InventarisGedung.show()

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login info")
        msg.setText(message)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InventarisGedung = QtWidgets.QMainWindow()
    ui = Ui_InventarisGedung()
    ui.getMeAName("admin")
    ui.setupUi(InventarisGedung)
    InventarisGedung.show()
    sys.exit(app.exec_())

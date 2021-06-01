# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuTampil.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuTampil(object):
    def setupUi(self, MenuTampil):
        MenuTampil.setObjectName("MenuTampil")
        MenuTampil.resize(641, 331)
        MenuTampil.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(MenuTampil)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 601, 291))
        self.frame.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 26, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 50, 561, 201))
        self.frame_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Gedung = QtWidgets.QPushButton(self.frame_2)
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
        self.Ruang = QtWidgets.QPushButton(self.frame_2)
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
        MenuTampil.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuTampil)
        QtCore.QMetaObject.connectSlotsByName(MenuTampil)

    def retranslateUi(self, MenuTampil):
        _translate = QtCore.QCoreApplication.translate
        MenuTampil.setWindowTitle(_translate("MenuTampil", "Menu Tampil"))
        self.label_2.setText(_translate("MenuTampil", "Lihat Data invetaris berdasarkan:"))
        self.Gedung.setText(_translate("MenuTampil", "Gedung"))
        self.Ruang.setText(_translate("MenuTampil", "Ruang"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuTampil = QtWidgets.QMainWindow()
    ui = Ui_MenuTampil()
    ui.setupUi(MenuTampil)
    MenuTampil.show()
    sys.exit(app.exec_())
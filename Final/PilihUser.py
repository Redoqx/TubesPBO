from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()


class Ui_PilihUsername(object):
    def setupUi(self, PilihUsername):
        PilihUsername.setObjectName("PilihUsername")
        PilihUsername.resize(639, 330)
        PilihUsername.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(PilihUsername)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 601, 291))
        self.frame.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 26, 301, 20))
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
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(90, 40, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.Ruang = QtWidgets.QPushButton(self.frame_2)
        self.Ruang.setGeometry(QtCore.QRect(350, 120, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Ruang.setFont(font)
        self.Ruang.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.Ruang.setObjectName("Ruang")
        PilihUsername.setCentralWidget(self.centralwidget)

        self.retranslateUi(PilihUsername)
        QtCore.QMetaObject.connectSlotsByName(PilihUsername)

        #code here


    def retranslateUi(self, PilihUsername):
        _translate = QtCore.QCoreApplication.translate
        PilihUsername.setWindowTitle(_translate("PilihUsername", "Pilih Username"))
        self.label_2.setText(_translate("PilihUsername", "Pilih Username yang akan dihapus:"))
        self.comboBox.setItemText(0, _translate("PilihUsername", "-Pilih Username-"))
        self.Ruang.setText(_translate("PilihUsername", "Hapus Akun"))

    def setUpin(self):
        order = "select username from login_info"
        try:
            mycursor.execute(order)
            result = mycursor.fetchall()
            for i in result:
                self.comboBox.addItem(i[0])
        except mysql.connector.Error as error:
            self.show_Popup(f'Galat!\nError Code\n{error}')

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login info")
        msg.setText(message)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PilihUsername = QtWidgets.QMainWindow()
    ui = Ui_PilihUsername()
    ui.setupUi(PilihUsername)
    ui.setUpin()
    PilihUsername.show()
    sys.exit(app.exec_())

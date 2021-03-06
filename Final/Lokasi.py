from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()


class Ui_PilihLokasi(object):
    def setupUi(self, PilihLokasi):
        PilihLokasi.setObjectName("PilihLokasi")
        PilihLokasi.resize(640, 331)
        PilihLokasi.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(PilihLokasi)
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
        self.Ruang.setGeometry(QtCore.QRect(290, 120, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Ruang.setFont(font)
        self.Ruang.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.Ruang.setObjectName("Ruang")
        PilihLokasi.setCentralWidget(self.centralwidget)

        self.retranslateUi(PilihLokasi)
        QtCore.QMetaObject.connectSlotsByName(PilihLokasi)


    def retranslateUi(self, PilihLokasi):
        _translate = QtCore.QCoreApplication.translate
        PilihLokasi.setWindowTitle(_translate("PilihLokasi", "Pilih Lokasi"))
        self.label_2.setText(_translate("PilihLokasi", "Temukan data dari:"))
        self.comboBox.setItemText(0, _translate("PilihLokasi", "-Pilih Lokasi-"))
        self.Ruang.setText(_translate("PilihLokasi", "Lihat Data Inventaris"))

    def setUpin(self, Jenis):
        # self.comboBox.addItem("")
        if Jenis == 1:
            order = "select Nama_Gedung from gedung"
        elif Jenis == 2:
            order = "select No_Ruangan from ruangan"
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
    PilihLokasi = QtWidgets.QMainWindow()
    ui = Ui_PilihLokasi()
    ui.setupUi(PilihLokasi)
    ui.setUpin(1)
    PilihLokasi.show()
    sys.exit(app.exec_())

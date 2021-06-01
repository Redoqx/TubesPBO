from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()


class Ui_BuatAkun(object):
    def setupUi(self, BuatAkun):
        BuatAkun.setObjectName("BuatAkun")
        BuatAkun.resize(800, 600)
        BuatAkun.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(BuatAkun)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 741, 541))
        self.frame.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.BackIcon = QtWidgets.QLabel(self.frame)
        self.BackIcon.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.BackIcon.setText("")
        self.BackIcon.setPixmap(QtGui.QPixmap("icon/BackIcon.png"))
        self.BackIcon.setScaledContents(True)
        self.BackIcon.setObjectName("BackIcon")
        self.BackButton = QtWidgets.QPushButton(self.frame)
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 0, 481, 111))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 150, 661, 351))
        self.frame_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 611, 291))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border: transparent;\n"
"border-bottom: 1px solid;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border: transparent;\n"
"border-bottom: 1px solid;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Buat = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Buat.setFont(font)
        self.Buat.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius : 10px;")
        self.Buat.setObjectName("Buat")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Buat)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border: transparent;\n"
"border-bottom: 1px solid;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        BuatAkun.setCentralWidget(self.centralwidget)

        self.retranslateUi(BuatAkun)
        QtCore.QMetaObject.connectSlotsByName(BuatAkun)
        #code here
        self.Buat.clicked.connect(self.Buatin)

    def retranslateUi(self, BuatAkun):
        _translate = QtCore.QCoreApplication.translate
        BuatAkun.setWindowTitle(_translate("BuatAkun", "Buat Akun"))
        self.label.setText(_translate("BuatAkun", "DATA AKUN BARU"))
        self.label_2.setText(_translate("BuatAkun", "Username"))
        self.lineEdit.setPlaceholderText(_translate("BuatAkun", "Username"))
        self.label_3.setText(_translate("BuatAkun", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("BuatAkun", "Password"))
        self.label_4.setText(_translate("BuatAkun", "Role"))
        self.Buat.setText(_translate("BuatAkun", "Buat Akun Baru"))
        self.comboBox.setItemText(0, _translate("BuatAkun", "tamu"))
        self.comboBox.setItemText(1, _translate("BuatAkun", "admin"))

    def Buatin(self):
        UN = self.lineEdit.text()
        PS = self.lineEdit_2.text()
        TP = self.comboBox.currentText()
        if not (UN and PS):
            self.show_Popup("Pastikan semua data telah terisi!")
            return 0
        order = f"INSERT INTO login_info (username, password, Account_role) VALUES ('{UN}', '{PS}', '{TP}')"
        try:
            mycursor.execute(order)
            mydb.commit()
            self.show_Popup("Berhasil Membuat Akun!")
        except mysql.connector.Error as error:
            self.show_Popup(f'Galat!\nError Code:\n{error}')

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText(message)
        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BuatAkun = QtWidgets.QMainWindow()
    ui = Ui_BuatAkun()
    ui.setupUi(BuatAkun)
    BuatAkun.show()
    sys.exit(app.exec_())

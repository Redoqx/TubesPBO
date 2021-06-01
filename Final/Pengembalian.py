from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()


class Ui_Pengembalian(object):
    def setupUi(self, Pengembalian):
        Pengembalian.setObjectName("Pengembalian")
        Pengembalian.resize(800, 600)
        Pengembalian.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Pengembalian)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 60, 681, 441))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(60, 120, 571, 241))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Input = QtWidgets.QPushButton(self.frame)
        self.Input.setGeometry(QtCore.QRect(470, 200, 93, 28))
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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 551, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
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
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(150, 10, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame.raise_()
        self.BackIcon.raise_()
        self.BackButton.raise_()
        self.label_3.raise_()
        Pengembalian.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pengembalian)
        QtCore.QMetaObject.connectSlotsByName(Pengembalian)

        #code here
        self.Input.clicked.connect(self.Balikin)

    def retranslateUi(self, Pengembalian):
        _translate = QtCore.QCoreApplication.translate
        Pengembalian.setWindowTitle(_translate("Pengembalian", "Pengembalian"))
        self.Input.setText(_translate("Pengembalian", "Input"))
        self.label.setText(_translate("Pengembalian", "No. Surat BAST"))
        self.lineEdit.setPlaceholderText(_translate("Pengembalian", "No. Surat BAST"))
        self.label_2.setText(_translate("Pengembalian", "ID Barang"))
        self.lineEdit_2.setPlaceholderText(_translate("Pengembalian", "ID Barang"))
        self.label_3.setText(_translate("Pengembalian", "Form Pengembalian"))

    def Balikin(self):
        IDP = self.lineEdit.text()
        IDB = self.lineEdit_2.text()
        if not (IDP and IDB):
            self.show_Popup("Harap masukkan data dengan lengkap!")
            return 0
        order = f"select ID_Barang from peminjaman where ID_Peminjaman = '{IDP}'"
        try:
            mycursor.execute(order)
            result = mycursor.fetchall()
            if not result:
                self.show_Popup("Harap pastikan kembali data anda!\nNomor Surat tidak dapat ditemukan")
                return 0
            result = result[0][0]
            if result == IDB:
                masuk = 1
                try:
                    cek = f"select Jumlah_Barang from peminjaman where ID_Peminjaman = '{IDP}'"
                    mycursor.execute(cek)
                    jml_pinjam = mycursor.fetchall()
                    jml_pinjam = (jml_pinjam[0])[0]
                    jml_pinjam = int(jml_pinjam)

                    cek = f"select stok_tersedia from barang where ID_Barang = '{IDB}'"
                    mycursor.execute(cek)
                    jml_sekarang = mycursor.fetchall()
                    jml_sekarang = (jml_sekarang[0])[0]
                    jml_sekarang = int(jml_sekarang)

                    jml_sekarang = jml_sekarang + jml_pinjam

                    Update_barang=f"Update barang set stok_tersedia = '{jml_sekarang}' where barang.ID_Barang = '{IDB}'"
                    mycursor.execute(Update_barang)
                    mydb.commit()

                except mysql.connector.Error as error:
                    self.show_Popup("Gagal mengembalikan barang, harap periksa kembali data inputan anda")
                    masuk = 0

                order = f"DELETE FROM peminjaman WHERE peminjaman.ID_Peminjaman = '{IDP}'"
                mycursor.execute(order)
                mydb.commit()

        except mysql.connector.Error as error:
            self.show_Popup(f'Galat!\nError Code:\n{error}')
            masuk = 0

        if masuk:
            self.show_Popup("Berhasil Mengembalika Barang Pinjaman!")

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login info")
        msg.setText(message)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pengembalian = QtWidgets.QMainWindow()
    ui = Ui_Pengembalian()
    ui.setupUi(Pengembalian)
    Pengembalian.show()
    sys.exit(app.exec_())

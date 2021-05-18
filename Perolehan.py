from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

class Ui_Perolehan(object):
    def setupUi(self, Perolehan):
        Perolehan.setObjectName("Perolehan")
        Perolehan.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Perolehan)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 70, 681, 441))
        self.groupBox.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(150, 20, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(50, 100, 581, 271))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.ID_Barang = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ID_Barang.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.ID_Barang.setText("")
        self.ID_Barang.setClearButtonEnabled(False)
        self.ID_Barang.setObjectName("ID_Barang")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ID_Barang)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.NamaBarang = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NamaBarang.setEnabled(True)
        self.NamaBarang.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.NamaBarang.setInputMethodHints(QtCore.Qt.ImhTime)
        self.NamaBarang.setText("")
        self.NamaBarang.setClearButtonEnabled(False)
        self.NamaBarang.setObjectName("NamaBarang")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NamaBarang)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Jumlah_Barang = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Jumlah_Barang.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.Jumlah_Barang.setText("")
        self.Jumlah_Barang.setClearButtonEnabled(False)
        self.Jumlah_Barang.setObjectName("Jumlah_Barang")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Jumlah_Barang)
        self.FindDirectory = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.FindDirectory.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.FindDirectory.setObjectName("FindDirectory")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.FindDirectory)
        self.DirectoryFinderButton = QtWidgets.QToolButton(self.formLayoutWidget)
        self.DirectoryFinderButton.setObjectName("DirectoryFinderButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.DirectoryFinderButton)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Input = QtWidgets.QPushButton(self.frame)
        self.Input.setGeometry(QtCore.QRect(480, 230, 93, 28))
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
        self.BackIcon.raise_()
        self.BackButton.raise_()
        Perolehan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Perolehan)
        self.statusbar.setObjectName("statusbar")
        Perolehan.setStatusBar(self.statusbar)

        self.retranslateUi(Perolehan)
        QtCore.QMetaObject.connectSlotsByName(Perolehan)

        #code here
        self.DirectoryFinderButton.clicked.connect(self.CariinDung)
        #Nginput
        self.Input.clicked.connect(self.Inputin)

    def retranslateUi(self, Perolehan):
        _translate = QtCore.QCoreApplication.translate
        Perolehan.setWindowTitle(_translate("Perolehan", "Perolehan"))
        self.label.setText(_translate("Perolehan", "Form Perolehan"))
        self.label_2.setText(_translate("Perolehan", "ID_Barang"))
        self.ID_Barang.setPlaceholderText(_translate("Perolehan", "ID Barang"))
        self.label_3.setText(_translate("Perolehan", "Nama Barang"))
        self.NamaBarang.setPlaceholderText(_translate("Perolehan", "Nama Barang"))
        self.label_4.setText(_translate("Perolehan", "Jumlah"))
        self.Jumlah_Barang.setPlaceholderText(_translate("Perolehan", "Jumlah Barang"))
        self.DirectoryFinderButton.setText(_translate("Perolehan", "..."))
        self.FindDirectory.setPlaceholderText(_translate("Perolehan", "File Directory"))
        self.label_5.setText(_translate("Perolehan", "Scan BAST"))
        self.Input.setText(_translate("Perolehan", "Input"))

    def getMeAName(self,username):
        self.username=username

    def CariinDung(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        self.path = filename[0]
        print(self.path)
        self.FindDirectory.setText(self.path)

    def Inputin(self):
        #terima data
        ID_Barang = self.ID_Barang.text()
        Namonyo = self.NamaBarang.text()
        Banyak = self.Jumlah_Barang.text()
        Gambar = self.FindDirectory.text()
        if not (ID_Barang and Namonyo and Banyak and Gambar):
            self.show_Popup("Harap Isi Semua Kelengkapan Data")
        elif not(Banyak.isnumeric()) or int(Banyak)<1:
            self.show_Popup("Harap Pastikan ulang Data Yang Anda Masukkan Telah Benar!")
        else:
            Gambar = convertToBinaryData(Gambar)
            Banyak = int(Banyak)
            masuk=1

            #Memasukkan data
            try:
                sql_insert_blob_query = """ INSERT INTO barang
                              (ID_Barang, Nama_Barang, stok_total, stok_tersedia, BAST_Perolehan) VALUES (%s,%s,%s,%s,%s)"""
                datanya = (ID_Barang,Namonyo,Banyak,Banyak,Gambar)
                result = mycursor.execute(sql_insert_blob_query,datanya)
                mydb.commit()
            except mysql.connector.Error as error:
                self.show_Popup(f'Gagal Mengunggah Data Peminjaman\nError Code\n{error}')
                masuk = 0
            if masuk:
                self.show_Popup("Berhasil Mengunggah Data Peminjaman")

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login info")
        msg.setText(message)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Perolehan = QtWidgets.QMainWindow()
    ui = Ui_Perolehan()
    ui.getMeAName("admin")
    ui.setupUi(Perolehan)
    Perolehan.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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

def convertdate(tanggal):
    idx1 = tanggal.find('/')
    bulan = tanggal[0:idx1]
    if (len(bulan)!=2):
        bulan = '0'+bulan
    idx2 = tanggal.find('/',idx1+1)
    hari = tanggal[idx1+1:idx2]
    if (len(hari)!=2):
        hari = '0'+hari
    tahun = tanggal[idx2+1:]
    return f'{tahun}-{bulan}-{hari}'

class Ui_Peminjaman(object):
    def setupUi(self, Peminjaman):
        Peminjaman.setObjectName("Peminjaman")
        Peminjaman.resize(800, 600)
        Peminjaman.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Peminjaman)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 80, 681, 441))
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
        self.frame.setGeometry(QtCore.QRect(60, 90, 571, 331))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 280))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.No_Surat = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.No_Surat.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.No_Surat.setText("")
        self.No_Surat.setClearButtonEnabled(False)
        self.No_Surat.setObjectName("No_Surat")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.No_Surat)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.NIP = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NIP.setEnabled(True)
        self.NIP.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.NIP.setInputMethodHints(QtCore.Qt.ImhTime)
        self.NIP.setText("")
        self.NIP.setClearButtonEnabled(False)
        self.NIP.setObjectName("NIP")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NIP)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.ID_Barang = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ID_Barang.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.ID_Barang.setText("")
        self.ID_Barang.setClearButtonEnabled(False)
        self.ID_Barang.setObjectName("ID_Barang")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ID_Barang)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.Jumlah_Barang = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Jumlah_Barang.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.Jumlah_Barang.setText("")
        self.Jumlah_Barang.setClearButtonEnabled(False)
        self.Jumlah_Barang.setObjectName("Jumlah_Barang")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Jumlah_Barang)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Tgl_Peminjaman = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.Tgl_Peminjaman.setKeyboardTracking(True)
        self.Tgl_Peminjaman.setProperty("showGroupSeparator", False)
        self.Tgl_Peminjaman.setCalendarPopup(True)
        self.Tgl_Peminjaman.setObjectName("Tgl_Peminjaman")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Tgl_Peminjaman)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Tgl_Pengembalian = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.Tgl_Pengembalian.setCalendarPopup(True)
        self.Tgl_Pengembalian.setObjectName("Tgl_Pengembalian")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Tgl_Pengembalian)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Pilih_Gedung = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
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
        self.Pilih_Gedung.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Pilih_Gedung)
        self.No_Ruangan = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.No_Ruangan.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.No_Ruangan.setText("")
        self.No_Ruangan.setClearButtonEnabled(False)
        self.No_Ruangan.setObjectName("No_Ruangan")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.No_Ruangan)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.FindDirectory = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.FindDirectory.setStyleSheet("background:transparent;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:1px solid;")
        self.FindDirectory.setObjectName("FindDirectory")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.FindDirectory)
        self.DirectoryFinderButton = QtWidgets.QToolButton(self.formLayoutWidget)
        self.DirectoryFinderButton.setObjectName("DirectoryFinderButton")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.DirectoryFinderButton)
        self.Input = QtWidgets.QPushButton(self.frame)
        self.Input.setGeometry(QtCore.QRect(470, 300, 93, 28))
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
        Peminjaman.setCentralWidget(self.centralwidget)

        self.retranslateUi(Peminjaman)
        QtCore.QMetaObject.connectSlotsByName(Peminjaman)

        #code here
        #Dapetin alamat
        self.DirectoryFinderButton.pressed.connect(self.CariinDung)
        #Nginput
        self.Input.pressed.connect(self.Inputin)


    def retranslateUi(self, Peminjaman):
        _translate = QtCore.QCoreApplication.translate
        Peminjaman.setWindowTitle(_translate("Peminjaman", "Peminjaman"))
        self.label.setText(_translate("Peminjaman", "Form Peminjaman"))
        self.label_2.setText(_translate("Peminjaman", "No. Surat"))
        self.No_Surat.setPlaceholderText(_translate("Peminjaman", "No. Surat Peminjaman"))
        self.label_3.setText(_translate("Peminjaman", "NIP"))
        self.NIP.setPlaceholderText(_translate("Peminjaman", "NIP"))
        self.label_4.setText(_translate("Peminjaman", "ID_Barang"))
        self.ID_Barang.setPlaceholderText(_translate("Peminjaman", "ID_Barang"))
        self.label_6.setText(_translate("Peminjaman", "Tanggal Peminjaman"))
        self.label_7.setText(_translate("Peminjaman", "Tanggal Pengembalian"))
        self.label_8.setText(_translate("Peminjaman", "Lokasi Barang"))
        self.Pilih_Gedung.setCurrentText(_translate("Peminjaman", "- Pilih Gedung -"))
        self.Pilih_Gedung.setItemText(0, _translate("Peminjaman", "- Pilih Gedung -"))
        self.Pilih_Gedung.setItemText(1, _translate("Peminjaman", "A"))
        self.Pilih_Gedung.setItemText(2, _translate("Peminjaman", "B"))
        self.Pilih_Gedung.setItemText(3, _translate("Peminjaman", "C"))
        self.Pilih_Gedung.setItemText(4, _translate("Peminjaman", "D"))
        self.Pilih_Gedung.setItemText(5, _translate("Peminjaman", "E"))
        self.Pilih_Gedung.setItemText(6, _translate("Peminjaman", "F"))
        self.Pilih_Gedung.setItemText(7, _translate("Peminjaman", "GKU"))
        self.Pilih_Gedung.setItemText(8, _translate("Peminjaman", "Labtek1"))
        self.Pilih_Gedung.setItemText(9, _translate("Peminjaman", "Labtek2"))
        self.Pilih_Gedung.setItemText(10, _translate("Peminjaman", "Labtek3"))
        self.No_Ruangan.setPlaceholderText(_translate("Peminjaman", "Nomor Ruang"))
        self.label_5.setText(_translate("Peminjaman", "Scan BAST"))
        self.FindDirectory.setPlaceholderText(_translate("Peminjaman", "File Directory"))
        self.DirectoryFinderButton.setText(_translate("Peminjaman", "..."))
        self.label_9.setText(_translate("Peminjaman", "Jumlah Barang"))
        self.Jumlah_Barang.setPlaceholderText(_translate("Peminjaman", "Jumlah Barang"))
        self.Input.setText(_translate("Peminjaman", "Input"))

    def CariinDung(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.FindDirectory.setText(self.path)

    def Inputin(self):
        #terima data
        no_surek = self.No_Surat.text()
        self.ID = self.NIP.text()
        ID_Barang = self.ID_Barang.text()
        Banyak = self.Jumlah_Barang.text()
        Bilo_Pinjam = self.Tgl_Peminjaman.text()
        Bilo_Pinjam = convertdate(str(Bilo_Pinjam))
        Bilo_Baliak = self.Tgl_Pengembalian.text()
        Bilo_Baliak = convertdate(str(Bilo_Baliak))
        Gedung = self.Pilih_Gedung.currentText()
        Biliak = self.No_Ruangan.text()
        Gambar = self.FindDirectory.text()
        if not (no_surek and ID_Barang and Banyak and Bilo_Pinjam and Bilo_Baliak and Gedung and Biliak and Gambar) or Gedung == '- Pilih Gedung -' or Bilo_Pinjam == '1/1/2000' or Bilo_Baliak == '1/1/2000':
            self.show_Popup("Harap Isi Semua Kelengkapan Data")
        elif not(Banyak.isnumeric()) or (Gedung != Biliak[0]):
            self.show_Popup("Harap Pastikan ulang Data Yang Anda Masukkan Telah Benar!")
        else:
            Gambar = convertToBinaryData(Gambar)
            Banyak = int(Banyak)
            masuk=1
            bisa = self.cek_Barang(ID_Barang,Banyak)
            if bisa:
                #Memasukkan data
                try:
                    sql_insert_blob_query = """ INSERT INTO peminjaman
                                  (ID_Peminjaman, ID_Peminjam, ID_Barang, Jumlah_Barang, Tgl_Peminjaman, Tgl_Pengembalian, Gedung, No_Ruangan, BAST_Disposisi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                    datanya = (no_surek,self.ID,ID_Barang,Banyak,Bilo_Pinjam,Bilo_Baliak,Gedung,Biliak,Gambar)
                    result = mycursor.execute(sql_insert_blob_query,datanya)
                    mydb.commit()
                except mysql.connector.Error as error:
                    self.show_Popup(f'Gagal Mengunggah Data Peminjaman\nError Code\n{error}')
                    masuk = 0

            if masuk and bisa:
                self.show_Popup("Berhasil Mengunggah Data Peminjaman")

    def cek_Barang(self,ID_Barang,Banyak):
        try:
            cek = f"select stok_tersedia from barang where ID_Barang = '{ID_Barang}'"
            mycursor.execute(cek)
            result = mycursor.fetchall()
            if not result:
                self.show_Popup("Barang yang anda pilih tidak tersedia")
                return 0
            print(result)
            result = (result[0])[0]
            result = int(result)
            if (result-Banyak) >= 0:
                result = result-Banyak
                ubah = f"UPDATE barang SET stok_tersedia = '{result}' WHERE barang.ID_Barang = '{ID_Barang}'"
                mycursor.execute(ubah)
                mydb.commit()
                return 1
            else:
                self.show_Popup("Barang yang ingin anda pinjam tidak tersedia")
                return 0
        except mysql.connector.Error as error:
            self.show_Popup("Barang tidak ditemukan!")

    def show_Popup(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("Login info")
        msg.setText(message)
        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Peminjaman = QtWidgets.QMainWindow()
    ui = Ui_Peminjaman()
    ui.setupUi(Peminjaman)
    Peminjaman.show()
    sys.exit(app.exec_())

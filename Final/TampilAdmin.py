from prettytable import PrettyTable
from fpdf import FPDF
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database ="tubes_pbo"
)
mycursor = mydb.cursor()

def get_data_from_prettytable(data):
    """
    Get a list of list from pretty_data table
    Arguments:
        :param data: data table to process
        :type data: PrettyTable
    """

    def remove_space(liste):
        """
        Remove space for each word in a list
        Arguments:
            :param liste: list of strings
        """
        list_without_space = []
        for mot in liste:                                       # For each word in list
            word_without_space = mot.replace(' ', '')           # word without space
            list_without_space.append(word_without_space)       # list of word without space
        return list_without_space

    # Get each row of the table
    string_x = str(data).split('\n')                               # Get a list of row
    header = string_x[1].split('|')[1: -1]                      # Columns names
    rows = string_x[3:len(string_x) - 1]                        # List of rows

    list_word_per_row = []
    for row in rows:                                            # For each word in a row
        row_resize = row.split('|')[1:-1]                       # Remove first and last arguments
        list_word_per_row.append(remove_space(row_resize))      # Remove spaces

    return header, list_word_per_row


def export_to_pdf(header, data, path, Judul):
    """
    Create a a table in PDF file from a list of row
        :param header: columns name
        :param data: List of row (a row = a list of cells)
        :param spacing=1:
    """
    pdf = FPDF()                                # New  pdf object

    pdf.set_font("Arial", size=12)              # Font style
    epw = pdf.w - 2*pdf.l_margin                # Witdh of document
    col_width = pdf.w / 6                       # Column width in table
    row_height = pdf.font_size * 1.5            # Row height in table
    spacing = 1.3                               # Space in each cell

    pdf.add_page()                              # add new page

    pdf.cell(epw, 0.0, Judul, align='C')   # create title cell
    pdf.ln(row_height*spacing)                  # Define title line style

    # Add header
    i=0
    for item in header:                         # for each column
        w = col_width
        if i == 1:
            w = 46.7
        pdf.cell(w, row_height*spacing, # Add a new cell
                 txt=item, border=1)
        i+=1
    pdf.ln(row_height*spacing)                  # New line after header

    for row in data:                            # For each row of the table
        i=0
        for item in row:                        # For each cell in row
            w = col_width
            if i == 1:
                w = 46.7
            pdf.cell(w, row_height*spacing, # Add cell
                    txt=item, border=1)
            i+=1
        pdf.ln(row_height*spacing)              # Add line at the end of row

    pdf.output(path)               # Create pdf file
    pdf.close()                                 # Close file


class Ui_Tampilkan(object):
    def setupUi(self, Tampilkan):
        Tampilkan.setObjectName("Tampilkan")
        Tampilkan.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        Tampilkan.setFont(font)
        Tampilkan.setStyleSheet("background-color: rgb(255, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Tampilkan)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 741, 541))
        self.widget.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon/BackIcon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.BackButton = QtWidgets.QPushButton(self.widget)
        self.BackButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.BackButton.setStyleSheet("background-color: transparent;")
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")

        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 90, 661, 371))
        self.tableWidget.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        self.Judul = QtWidgets.QLabel(self.widget)
        self.Judul.setGeometry(QtCore.QRect(140, 20, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Judul.setFont(font)
        self.Judul.setAlignment(QtCore.Qt.AlignCenter)
        self.Judul.setObjectName("Judul")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 470, 631, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(700, 470, 21, 20))
        self.pushButton.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 500, 93, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.pushButton_2.setObjectName("pushButton_2")
        Tampilkan.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tampilkan)
        QtCore.QMetaObject.connectSlotsByName(Tampilkan)

        #code here
        self.havePath = False
        self.pushButton.clicked.connect(self.CariinDung)
        self.pushButton_2.clicked.connect(self.cetak)


    def retranslateUi(self, Tampilkan):
        _translate = QtCore.QCoreApplication.translate
        Tampilkan.setWindowTitle(_translate("Tampilkan", "Data Inventaris"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Tampilkan", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Tampilkan", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Tampilkan", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Tampilkan", "ID Peminjaman"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Tampilkan", "NIP Peminjam"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Tampilkan", "ID Barang"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Tampilkan", "Lokasi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Tampilkan", "Gedung"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Tampilkan", "!ID"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Tampilkan", "!NIP"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Tampilkan", "!IDB"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Tampilkan", "!Lok"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Tampilkan", "!Gedu"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Tampilkan", "@ID"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Tampilkan", "@NIP"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Tampilkan", "@DB"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Tampilkan", "@Lok"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("Tampilkan", "@Gedu"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Tampilkan", "#ID"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Tampilkan", "#NIP"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Tampilkan", "#DB"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("Tampilkan", "#Lok"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("Tampilkan", "#Gedu"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.Judul.setText(_translate("Tampilkan", "DATA INVENTARIS ......"))
        self.lineEdit.setPlaceholderText(_translate("Tampilkan", "Lokasi Penyimpanan Laporan"))
        self.pushButton.setText(_translate("Tampilkan", "..."))
        self.pushButton_2.setText(_translate("Tampilkan", "Buat Laporan"))

    def CariinDung(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory()
        self.path = folderpath+'\LaporanInventaris.pdf'
        self.lineEdit.setText(self.path)
        self.havePath = True

    def cetak(self):
        import webbrowser
        if not self.havePath:
            self.show_Popup("Tentukan path terlebih dahulu\n\nSilahkan klik tombol '...' di samping kanan kolom lokasi penyimpanan laporan!")
            return 0
        header, data = get_data_from_prettytable(self.data_tabel)
        if self.Judul.text() == "DATA INVENTARIS RUANG":
            self.Loc = "Ruang "+self.Loc
        export_to_pdf(header, data, self.path, "Laporan Inventaris "+self.Loc)
        path = r'file://'+self.path
        webbrowser.open_new(path)

    def setUpin(self,Judul,Loc):
        self.Judul.setText(f"DATA INVENTARIS {Judul}")
        self.Loc = Loc

        if Judul == "GEDUNG":
            order = f"""select ID_Peminjaman,ID_Peminjam,ID_Barang,Gedung,No_Ruangan
                    from gedung right outer join peminjaman on peminjaman.gedung = gedung.Kode_Gedung
                    where Nama_Gedung = '{Loc}'"""
        if Judul == "RUANG":
            order = f"""select ID_Peminjaman,ID_Peminjam,ID_Barang,Gedung,peminjaman.No_Ruangan
                    from ruangan right outer join peminjaman on peminjaman.No_Ruangan = ruangan.No_Ruangan
                    where ruangan.No_Ruangan = '{Loc}'"""
        try:
            mycursor.execute(order)
            data = mycursor.fetchall()
            if not data:
                self.tableWidget.setColumnCount(1)
                self.tableWidget.setRowCount(1)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(0, 0, item)
                item = self.tableWidget.item(0, 0)
                item.setText("NULL")
                self.show_Popup("Tidak terdapat data inventaris apapun di lokasi ini!")
            else:
                self.tableWidget.setRowCount(len(data))
                x=PrettyTable(['ID_Peminjaman','ID_Peminjam','ID_Barang','Gedung','No_Ruangan'])
                ci=0
                for i in data:
                    cj=0
                    x.add_row(i)
                    for j in i:
                        item = QtWidgets.QTableWidgetItem()
                        self.tableWidget.setItem(ci, cj, item)
                        item = self.tableWidget.item(ci,cj)
                        item.setText(j)
                        cj+=1
                    ci+=1
                self.data_tabel = x
                print(self.data_tabel)

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
    Tampilkan = QtWidgets.QMainWindow()
    ui = Ui_Tampilkan()
    ui.setupUi(Tampilkan)
    ui.setUpin("GEDUNG","Gedung D")
    Tampilkan.show()
    sys.exit(app.exec_())

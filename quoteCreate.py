from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_QuoteCreate(object):
    def setupUi(self, QuoteCreate):
        QuoteCreate.setObjectName("QuoteCreate")
        QuoteCreate.resize(592, 356)
        self.lineEditAuthor = QtWidgets.QLineEdit(QuoteCreate)
        self.lineEditAuthor.setGeometry(QtCore.QRect(10, 170, 571, 20))
        self.lineEditAuthor.setObjectName("lineEditAuthor")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(QuoteCreate)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 571, 101))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(QuoteCreate)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(QuoteCreate)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(QuoteCreate)
        self.radioButton.setGeometry(QtCore.QRect(130, 280, 141, 21))
        self.radioButton.setObjectName("radioButton")
        self.label_2 = QtWidgets.QLabel(QuoteCreate)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 111, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(QuoteCreate)
        self.comboBox.setGeometry(QtCore.QRect(10, 280, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.lineEditRating = QtWidgets.QLineEdit(QuoteCreate)
        self.lineEditRating.setGeometry(QtCore.QRect(10, 220, 31, 20))
        self.lineEditRating.setText("")
        self.lineEditRating.setObjectName("lineEditRating")
        self.label_3 = QtWidgets.QLabel(QuoteCreate)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(QuoteCreate)
        self.label.setGeometry(QtCore.QRect(10, 260, 47, 13))
        self.label.setObjectName("label")

        self.retranslateUi(QuoteCreate)
        QtCore.QMetaObject.connectSlotsByName(QuoteCreate)

        #событие сохранения цитаты
        self.pushButton.clicked.connect(self.CreateQuote)

        #вывод тем в comboBox
        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        topics = cur.execute('SELECT titile FROM topics').fetchall()
        list_titles = [title[0] for title in topics]
        for i in list_titles:
            self.comboBox.addItem(str(i))

        con.commit()
        con.close()

    #создание цитаты
    def CreateQuote(self):
        topic = self.comboBox.currentText()
        quote = self.plainTextEdit.toPlainText()
        author = self.lineEditAuthor.text()
        rating = self.lineEditRating.text()
        if rating == '0' or rating == '1' or rating == '2' or rating == '3' or rating == '4' or rating == '5':
            rating = int(self.lineEditRating.text())
        else:
            rating = 0
        favourite = 0
        if self.radioButton.isChecked():
            favourite = 1

        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        cur.execute("INSERT INTO quotes (topic, quote, author, rating, favourite) VALUES (?, ?, ?, ?, ?)", (topic, quote, author, rating, favourite,))

        con.commit()
        con.close()

    def retranslateUi(self, QuoteCreate):
        _translate = QtCore.QCoreApplication.translate
        QuoteCreate.setWindowTitle(_translate("QuoteCreate", "Dialog"))
        self.pushButton.setText(_translate("QuoteCreate", "Сохранить"))
        self.label_4.setText(_translate("QuoteCreate", "Цитата"))
        self.radioButton.setText(_translate("QuoteCreate", "Избранное"))
        self.label_2.setText(_translate("QuoteCreate", "Автор"))
        self.label_3.setText(_translate("QuoteCreate", "Рейтинг (от 0 до 5)"))
        self.label.setText(_translate("QuoteCreate", "Раздел"))

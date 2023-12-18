from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_QuoteEdit(object):
    def setupUi(self, QuoteEdit, quote_id):
        QuoteEdit.setObjectName("QuoteEdit")
        QuoteEdit.resize(593, 356)
        self.labelQuote = QtWidgets.QLabel(QuoteEdit)
        self.labelQuote.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.labelQuote.setObjectName("labelQuote")
        self.radioButtonFav = QtWidgets.QRadioButton(QuoteEdit)
        self.radioButtonFav.setGeometry(QtCore.QRect(130, 280, 141, 21))
        self.radioButtonFav.setObjectName("radioButtonFav")
        self.labelAuthor = QtWidgets.QLabel(QuoteEdit)
        self.labelAuthor.setGeometry(QtCore.QRect(10, 150, 111, 16))
        self.labelAuthor.setObjectName("labelAuthor")
        self.labelRating = QtWidgets.QLabel(QuoteEdit)
        self.labelRating.setGeometry(QtCore.QRect(10, 200, 101, 16))
        self.labelRating.setObjectName("labelRating")
        self.comboBoxCategory = QtWidgets.QComboBox(QuoteEdit)
        self.comboBoxCategory.setGeometry(QtCore.QRect(10, 280, 101, 22))
        self.comboBoxCategory.setObjectName("comboBoxCategory")
        self.lineEditAuthor = QtWidgets.QLineEdit(QuoteEdit)
        self.lineEditAuthor.setGeometry(QtCore.QRect(10, 170, 571, 20))
        self.lineEditAuthor.setObjectName("lineEditAuthor")
        self.lineEditRating = QtWidgets.QLineEdit(QuoteEdit)
        self.lineEditRating.setGeometry(QtCore.QRect(10, 220, 31, 20))
        self.lineEditRating.setText("")
        self.lineEditRating.setObjectName("lineEditRating")
        self.pushButtonSave = QtWidgets.QPushButton(QuoteEdit)
        self.pushButtonSave.setGeometry(QtCore.QRect(10, 320, 111, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.label = QtWidgets.QLabel(QuoteEdit)
        self.label.setGeometry(QtCore.QRect(10, 260, 47, 13))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(QuoteEdit)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 571, 101))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButtonDelete = QtWidgets.QPushButton(QuoteEdit)
        self.pushButtonDelete.setGeometry(QtCore.QRect(470, 320, 111, 23))
        self.pushButtonDelete.setObjectName("pushButtonDelete")

        self.retranslateUi(QuoteEdit)
        QtCore.QMetaObject.connectSlotsByName(QuoteEdit)
        self.pushButtonSave.clicked.connect(lambda: self.SaveEditQuote(quote_id))
        self.pushButtonDelete.clicked.connect(lambda: self.DeleteQuote(quote_id))

        #заполнение textEdit и plainTextEdit информацией о цитате из БД для удобста редактирования
        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        cur.execute('SELECT quote FROM quotes WHERE quote_id=(?)', (quote_id,))
        quote = cur.fetchone()[0]
        cur.execute('SELECT author FROM quotes WHERE quote_id=(?)', (quote_id,))
        author = cur.fetchone()[0]
        cur.execute('SELECT rating FROM quotes WHERE quote_id=(?)', (quote_id,))
        rating = cur.fetchone()[0]
        cur.execute('SELECT favourite FROM quotes WHERE quote_id=(?)', (quote_id,))
        fav = cur.fetchone()[0]
        self.plainTextEdit.setPlainText(quote)
        self.lineEditAuthor.setText(author)
        self.lineEditRating.setText(str(rating))
        if fav == 1:
            self.radioButtonFav.setChecked(True)


        topics = cur.execute('SELECT titile FROM topics').fetchall()
        list_titles = [title[0] for title in topics]
        for i in list_titles:
            self.comboBoxCategory.addItem(str(i))

        con.commit()
        con.close()

    #сохранение изменений
    def SaveEditQuote(self, quote_id):
        topic = self.comboBoxCategory.currentText()
        quote = self.plainTextEdit.toPlainText()
        author = self.lineEditAuthor.text()
        rating = self.lineEditRating.text()
        if rating == '0' or rating == '1' or rating == '2' or rating == '3' or rating == '4' or rating == '5':
            rating = int(self.lineEditRating.text())
        else:
            rating = 0
        favourite = 0
        if self.radioButtonFav.isChecked():
            favourite = 1

        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        cur.execute("UPDATE quotes SET topic=?, quote=?, author=?, rating=?, favourite=? WHERE quote_id=?", (topic, quote, author, rating, favourite, quote_id,))

        con.commit()
        con.close()
    
    #удаление цитаты
    def DeleteQuote(self, quote_id):
        print('проверка')
        print(quote_id)

        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        cur.execute('DELETE FROM quotes WHERE quote_id=(?)', (quote_id,))

        con.commit()
        con.close()

    def retranslateUi(self, QuoteEdit):
        _translate = QtCore.QCoreApplication.translate
        QuoteEdit.setWindowTitle(_translate("QuoteEdit", "Dialog"))
        self.labelQuote.setText(_translate("QuoteEdit", "Цитата"))
        self.radioButtonFav.setText(_translate("QuoteEdit", "Избранное"))
        self.labelAuthor.setText(_translate("QuoteEdit", "Автор"))
        self.labelRating.setText(_translate("QuoteEdit", "Рейтинг (от 0 до 5)"))
        self.pushButtonSave.setText(_translate("QuoteEdit", "Сохранить"))
        self.label.setText(_translate("QuoteEdit", "Раздел"))
        self.pushButtonDelete.setText(_translate("QuoteEdit", "Удалить"))

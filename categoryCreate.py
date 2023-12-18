from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_CategoryCreate(object):
    def setupUi(self, CategoryCreate):
        CategoryCreate.setObjectName("CategoryCreate")
        CategoryCreate.resize(591, 139)
        self.pushButtonSave = QtWidgets.QPushButton(CategoryCreate)
        self.pushButtonSave.setGeometry(QtCore.QRect(10, 90, 111, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.lineEditQuote = QtWidgets.QLineEdit(CategoryCreate)
        self.lineEditQuote.setGeometry(QtCore.QRect(10, 40, 571, 20))
        self.lineEditQuote.setText("")
        self.lineEditQuote.setObjectName("lineEditQuote")
        self.labelQuote = QtWidgets.QLabel(CategoryCreate)
        self.labelQuote.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.labelQuote.setObjectName("labelQuote")

        self.retranslateUi(CategoryCreate)
        QtCore.QMetaObject.connectSlotsByName(CategoryCreate)

    #создание категории
    def CreateCategory(self):
        title = self.lineEditQuote.text()

        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        if (title != '' and title != ' '):
            cur.execute("INSERT INTO topics (titile) VALUES (?)", (title,))

        con.commit()
        con.close()      

    def retranslateUi(self, CategoryCreate):
        _translate = QtCore.QCoreApplication.translate
        CategoryCreate.setWindowTitle(_translate("CategoryCreate", "Dialog"))
        self.pushButtonSave.setText(_translate("CategoryCreate", "Сохранить"))
        self.labelQuote.setText(_translate("CategoryCreate", "Название раздела"))


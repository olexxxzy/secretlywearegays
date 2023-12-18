import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QPushButton, QAction, QWidget
import sqlite3
from quoteCreate import Ui_QuoteCreate
from quoteEdit import Ui_QuoteEdit
from categoryCreate import Ui_CategoryCreate
from mainPage import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #открытие окна для создания цитаты
    def OpenQuoteCreate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_QuoteCreate()
        self.ui.setupUi(self.window)
        self.window.setWindowTitle('Создание цитаты')
        self.window.show()

    #открытие окна редактирования цитаты
    def OpenQuoteEdit(self, quote_id):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_QuoteEdit()
        self.ui.setupUi(self.window, quote_id)
        self.window.setWindowTitle('Редактирование цитаты')
        self.window.show()

    #открытие окна для создания категории
    def OpenCategoryCreate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CategoryCreate()
        self.ui.setupUi(self.window)
        self.window.setWindowTitle('Создание раздела')
        self.window.show()

    #удалении категории
    def DeleteCategory(self, title):
        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        cur.execute('UPDATE quotes SET topic = "Общее" WHERE topic = (?)', (title,))
        cur.execute('DELETE FROM topics WHERE titile = (?)', (title,))

        con.commit()
        con.close()

        self.Updating()

    #обновление грида
    def Updating(self):
        while self.gridLayout.count() > 4:
            item = self.gridLayout.takeAt(4)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle('Индивидуальный цитатник')
    w.show()
    sys.exit(app.exec_())
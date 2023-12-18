from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, QLabel, QPushButton
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font-size: 16px;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 1500, 800))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelAuthor = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelAuthor.setObjectName("labelAuthor")
        self.gridLayout.addWidget(self.labelAuthor, 0, 1, 1, 1)
        self.labelQuote = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelQuote.setObjectName("labelQuote")
        self.gridLayout.addWidget(self.labelQuote, 0, 0, 1, 1)
        self.labelRating = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelRating.setObjectName("labelRating")
        self.gridLayout.addWidget(self.labelRating, 0, 2, 1, 1)
        self.labeZerolEditing = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labeZerolEditing.setText("")
        self.labeZerolEditing.setObjectName("labeZerolEditing")
        self.gridLayout.addWidget(self.labeZerolEditing, 0, 3, 1, 1)
        self.labelCategory = QtWidgets.QLabel(self.centralwidget)
        self.labelCategory.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.labelCategory.setText("")
        self.labelCategory.setObjectName("labelCategory")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.actionNewQuote = QtWidgets.QAction(MainWindow)
        self.actionNewQuote.setObjectName("actionNewQuote")
        self.actionNewCategory = QtWidgets.QAction(MainWindow)
        self.actionNewCategory.setObjectName("actionNewCategory")
        self.actionGeneralCategory = QtWidgets.QAction(MainWindow)
        self.actionGeneralCategory.setObjectName("actionGeneralCategory")
        self.actionFavCategory = QtWidgets.QAction(MainWindow)
        self.actionFavCategory.setObjectName("actionFavCategory")
        self.menu.addAction(self.actionNewQuote)
        self.menu_3.addAction(self.actionNewCategory)
        self.menu_3.addAction(self.actionFavCategory)
        self.menu_3.addAction(self.actionGeneralCategory)
        self.menu_3.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #события
        self.actionNewQuote.triggered.connect(MainWindow.OpenQuoteCreate)
        self.actionNewCategory.triggered.connect(MainWindow.OpenCategoryCreate)
        self.actionGeneralCategory.triggered.connect(self.GoToGeneral)
        self.actionFavCategory.triggered.connect(self.GoToFav)

        #вывод тем в menu_3
        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        topics = cur.execute('SELECT titile FROM topics WHERE topic_id > 1').fetchall()
        list_titles = [title[0] for title in topics]
        for title in list_titles:
            sub_menu = self.menu_3.addMenu(title)
            open_action = QAction("Открыть", sub_menu)
            open_action.triggered.connect(lambda checked, title=title: self.GoToCategory(title))
            sub_menu.addAction(open_action)
            delete_action = QAction("Удалить", sub_menu)
            delete_action.triggered.connect(lambda checked, title=title: self.DeleteCategory(title))
            sub_menu.addAction(delete_action)

        con.commit()
        con.close()

    #открытие определённой категории
    def GoToCategory(self, title):
        self.Updating()
        self.labelCategory.setText(title)

        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        quotes = cur.execute('SELECT quote FROM quotes WHERE topic = (?)', (title,)).fetchall()
        list_quote = [quote[0] for quote in quotes]
        for quote in list_quote:
            text = QLabel(str(quote))
            self.gridLayout.addWidget(text, list_quote.index(quote)+1, 0)

        authors = cur.execute('SELECT author FROM quotes WHERE topic = (?)', (title,)).fetchall()
        list_author = [author[0] for author in authors]
        for author in list_author:
            label = QLabel(str(author))
            self.gridLayout.addWidget(label, list_author.index(author)+1, 1)

        ratings = cur.execute('SELECT rating FROM quotes WHERE topic = (?)', (title,)).fetchall()
        list_rating = [rating[0] for rating in ratings]
        for rating in list_rating:
            if rating == 0:
                label = QLabel(str('☆☆☆☆☆'))
            if rating == 1:
                label = QLabel(str('★☆☆☆☆'))
            if rating == 2:
                label = QLabel(str('★★☆☆☆'))
            if rating == 3:
                label = QLabel(str('★★★☆☆'))
            if rating == 4:
                label = QLabel(str('★★★★☆'))
            if rating == 5:
                label = QLabel(str('★★★★★'))
            self.gridLayout.addWidget(label, list_rating.index(rating)+1, 2)

        edits = cur.execute('SELECT quote_id, author FROM quotes WHERE topic = (?)', (title,)).fetchall()
        list_edit = [edit[1] for edit in edits]
        for edit in edits:
            quote_id = edit[0]
            button = QPushButton(self)
            button.setText('Редактировать')
            button.clicked.connect(lambda checked, quote_id=quote_id: self.OpenQuoteEdit(quote_id))
            self.gridLayout.addWidget(button, list_edit.index(edit[1])+1, 3)

        con.commit()
        con.close()

    #отерытие избранных цитат
    def GoToFav(self):
        self.Updating()
        self.labelCategory.setText('Избранное')

        con = sqlite3.connect(r'C:\Users\Alex Khripunkov\Desktop\projectmy\Project\project.sqlite')
        cur = con.cursor()

        quotes = cur.execute('SELECT quote FROM quotes WHERE favourite = 1').fetchall()
        list_quote = [quote[0] for quote in quotes]
        for quote in list_quote:
            text = QLabel(str(quote))
            self.gridLayout.addWidget(text, list_quote.index(quote)+1, 0)

        authors = cur.execute('SELECT author FROM quotes WHERE favourite = 1').fetchall()
        list_author = [author[0] for author in authors]
        for author in list_author:
            label = QLabel(str(author))
            self.gridLayout.addWidget(label, list_author.index(author)+1, 1)

        ratings = cur.execute('SELECT rating FROM quotes WHERE favourite = 1').fetchall()
        list_rating = [rating[0] for rating in ratings]
        for rating in list_rating:
            if rating == 0:
                label = QLabel(str('☆☆☆☆☆'))
            if rating == 1:
                label = QLabel(str('★☆☆☆☆'))
            if rating == 2:
                label = QLabel(str('★★☆☆☆'))
            if rating == 3:
                label = QLabel(str('★★★☆☆'))
            if rating == 4:
                label = QLabel(str('★★★★☆'))
            if rating == 5:
                label = QLabel(str('★★★★★'))
            self.gridLayout.addWidget(label, list_rating.index(rating)+1, 2)

        edits = cur.execute('SELECT quote_id, author FROM quotes WHERE favourite = 1').fetchall()
        list_edit = [edit[1] for edit in edits]
        for edit in edits:
            quote_id = edit[0]
            button = QPushButton(self)
            button.setText('Редактировать')
            button.clicked.connect(lambda checked, quote_id=quote_id: self.OpenQuoteEdit(quote_id))
            self.gridLayout.addWidget(button, list_edit.index(edit[1])+1, 3)

    #открытие категории "Общее"
    def GoToGeneral(self):
        self.GoToCategory('Общее')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelAuthor.setText(_translate("MainWindow", "Автор"))
        self.labelQuote.setText(_translate("MainWindow", "Цитата"))
        self.labelRating.setText(_translate("MainWindow", "Рейтинг"))
        self.menu.setTitle(_translate("MainWindow", "Цитаты"))
        self.menu_3.setTitle(_translate("MainWindow", "Разделы"))
        self.actionNewQuote.setText(_translate("MainWindow", "Новая цитата"))
        self.actionNewCategory.setText(_translate("MainWindow", "Новый раздел"))
        self.actionGeneralCategory.setText(_translate("MainWindow", "Общее"))
        self.actionFavCategory.setText(_translate("MainWindow", "Избранное"))

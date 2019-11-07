# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QDialog
from untitled3 import Ui_Dialog


class Ui_MainWindow2(object):

    def openWindow1(self):
        self.window1=QtWidgets.QDialog()
        self.ui1=Ui_Dialog()
        self.ui1.setupUi3(self.window1)
        #MainWindow2.hide()
        self.window1.show()


    def setupUi2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1779, 827)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(225, 70, 651, 91))
        self.textBrowser.setStyleSheet("background-color: rgb(170, 255, 43);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(440, 220, 171, 71))
        self.pushButton2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(158, 255, 47);")
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton2.clicked.connect(self.pushButton_handler)



        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(342, 427, 381, 61))
        self.pushButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(133, 255, 33);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.openWindow1)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1779, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def pushButton_handler(self):
        print("button pressed")
        self.open_dialog_box()

    def open_dialog_box(self):
        filename=QFileDialog.getOpenFileName()
        print(filename)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">Please Upload your Resume</span></p></body></html>"))
        self.pushButton2.setText(_translate("MainWindow", "Upload"))
        self.pushButton_2.setText(_translate("MainWindow", "Click here to continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi2(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())

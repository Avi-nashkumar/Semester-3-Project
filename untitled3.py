# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from parser4 import recommend
from parser5 import name_ext
from parser6 import extract_image



class Ui_Dialog(object):
    def setupUi3(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 806)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        Dialog.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"background-image: url(:/images1.jpg/images1.jpg);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 670, 341, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(175, 255, 46);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton3 = QtWidgets.QPushButton(Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(410, 250, 221, 51))
        self.pushButton3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(189, 255, 46);")
        self.pushButton3.setObjectName("pushButton3")

        self.pushButton3.clicked.connect(self.Projectnames)


        self.textBrowser3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser3.setGeometry(QtCore.QRect(140, 370, 841, 271))
        self.textBrowser3.setStyleSheet("background-color: rgb(168, 255, 38);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.textBrowser3.setObjectName("textBrowser3")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(345, 51, 381, 161))
        self.textBrowser.setStyleSheet("background-color: rgb(153, 255, 57);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.textBrowser.setObjectName("textBrowser")
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(10, 10, 311, 321))
        self.image.setText("")
        #self.image.setPixmap(QtGui.QPixmap("BeautyPlus_20191006160526096_save (1).jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def Projectnames(self):
        name1=extract_image()
        self.image.setPixmap(QtGui.QPixmap("detected_face.jpg"))
        name1=name_ext()
        name2= "Hi"+" "+str(name1)
        self.textBrowser.setText(name2)
        project= recommend()
        pro_ject= "Try this project :"+ str(project)
        self.textBrowser3.setText(pro_ject)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton3.setText(_translate("Dialog", "Recommend"))
        self.textBrowser3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi3(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

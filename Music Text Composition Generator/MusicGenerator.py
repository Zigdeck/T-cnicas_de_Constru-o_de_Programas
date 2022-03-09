# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MusicGenerator.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 705)
        MainWindow.setStyleSheet("background-color: rgb(134, 233, 191);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_7.setStyleSheet("QFrame{\n"
"    background-color: rgb(50, 208, 132);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setStyleSheet("font: 63 22pt \"Yu Gothic UI Semibold\";")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setMaximumSize(QtCore.QSize(381, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 63 15pt \"Yu Gothic UI Semibold\";")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setStyleSheet("font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.FileNameTxt = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.FileNameTxt.setFont(font)
        self.FileNameTxt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FileNameTxt.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    padding-left: 15px;\n"
"}\n"
"")
        self.FileNameTxt.setObjectName("FileNameTxt")
        self.verticalLayout_4.addWidget(self.FileNameTxt)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setMaximumSize(QtCore.QSize(381, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        self.label_4.setMaximumSize(QtCore.QSize(381, 16777215))
        self.label_4.setStyleSheet("font: 63 15pt \"Yu Gothic UI Semibold\";")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_5.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.TextTxt = QtWidgets.QTextEdit(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(11)
        self.TextTxt.setFont(font)
        self.TextTxt.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    padding-left: 10px;\n"
"}\n"
"")
        self.TextTxt.setObjectName("TextTxt")
        self.horizontalLayout_7.addWidget(self.TextTxt)
        self.horizontalLayout_5.addWidget(self.frame_10)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setMaximumSize(QtCore.QSize(381, 16777215))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_13)
        self.label_5.setStyleSheet("font: 63 15pt \"Yu Gothic UI Semibold\";")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.horizontalLayout_8.addWidget(self.frame_13)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.BPMTxt = QtWidgets.QLineEdit(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.BPMTxt.setFont(font)
        self.BPMTxt.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    padding-left: 15px;\n"
"}")
        self.BPMTxt.setObjectName("BPMTxt")
        self.horizontalLayout_10.addWidget(self.BPMTxt)
        self.horizontalLayout_8.addWidget(self.frame_12)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_15 = QtWidgets.QFrame(self.frame_6)
        self.frame_15.setMaximumSize(QtCore.QSize(381, 16777215))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.frame_15)
        self.label_6.setStyleSheet("font: 63 15pt \"Yu Gothic UI Semibold\";")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.horizontalLayout_11.addWidget(self.frame_15)
        self.frame_14 = QtWidgets.QFrame(self.frame_6)
        self.frame_14.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.InstrumentComboBox = QtWidgets.QComboBox(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.InstrumentComboBox.setFont(font)
        self.InstrumentComboBox.setStyleSheet("QComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.InstrumentComboBox.setObjectName("InstrumentComboBox")
        self.InstrumentComboBox.addItem("")
        self.InstrumentComboBox.addItem("")
        self.InstrumentComboBox.addItem("")
        self.InstrumentComboBox.addItem("")
        self.InstrumentComboBox.addItem("")
        self.InstrumentComboBox.addItem("")
        self.horizontalLayout_12.addWidget(self.InstrumentComboBox)
        self.horizontalLayout_11.addWidget(self.frame_14)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GenerateButton = QtWidgets.QPushButton(self.frame_5)
        self.GenerateButton.setMaximumSize(QtCore.QSize(300, 16777215))
        self.GenerateButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.GenerateButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.GenerateButton.setStyleSheet("QPushButton{\n"
"    font: 63 16pt \"Yu Gothic UI Semibold\";\n"
"    border-radius: 15px;\n"
"    background-color: rgb(50, 208, 132);\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    font: 63 16pt \"Yu Gothic UI Semibold\";\n"
"    border-radius: 15px;\n"
"    background-color: rgb(39, 163, 103);\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    font: 63 16pt \"Yu Gothic UI Semibold\";\n"
"    border-radius: 15px;\n"
"    background-color: rgb(22, 94, 59);\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"}\n"
"")
        self.GenerateButton.setObjectName("GenerateButton")
        self.horizontalLayout_2.addWidget(self.GenerateButton)
        self.verticalLayout.addWidget(self.frame_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Music Text Composition Generator"))
        self.label_2.setText(_translate("MainWindow", "File Name:"))
        self.label_3.setText(_translate("MainWindow", "Don\'t use the characters below \n"
" (“”, “/”, “|”, “?”, “<”, “>”, “*”, “:” , ‘ ” ’)"))
        self.label_4.setText(_translate("MainWindow", "Text:"))
        self.label_5.setText(_translate("MainWindow", "BPM:"))
        self.label_6.setText(_translate("MainWindow", "Instrument:"))
        self.InstrumentComboBox.setItemText(0, _translate("MainWindow", "Guitarra"))
        self.InstrumentComboBox.setItemText(1, _translate("MainWindow", "Violão"))
        self.InstrumentComboBox.setItemText(2, _translate("MainWindow", "Bateria"))
        self.InstrumentComboBox.setItemText(3, _translate("MainWindow", "Teclado"))
        self.InstrumentComboBox.setItemText(4, _translate("MainWindow", "Saxofone"))
        self.InstrumentComboBox.setItemText(5, _translate("MainWindow", "Violino"))
        self.GenerateButton.setText(_translate("MainWindow", "Generate Music"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
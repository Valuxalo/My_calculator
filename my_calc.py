# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 551)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_res = QtWidgets.QLabel(self.centralwidget)
        self.label_res.setGeometry(QtCore.QRect(0, 0, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(30)
        font.setStrikeOut(False)
        self.label_res.setFont(font)
        self.label_res.setStyleSheet("QLabel{\n"
"color: white;\n"
"background: #8FD589;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}")
        self.label_res.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_res.setObjectName("label_res")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 390, 200, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_0.setFont(font)
        self.btn_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_0.setAutoFillBackground(False)
        self.btn_0.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_0.setAutoDefault(False)
        self.btn_0.setDefault(True)
        self.btn_0.setFlat(False)
        self.btn_0.setObjectName("btn_0")
        self.btn_ravno = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ravno.setGeometry(QtCore.QRect(200, 390, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_ravno.setFont(font)
        self.btn_ravno.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #898ED5;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"background: #9196DA;\n"
"}\n"
"")
        self.btn_ravno.setAutoDefault(False)
        self.btn_ravno.setDefault(True)
        self.btn_ravno.setFlat(False)
        self.btn_ravno.setObjectName("btn_ravno")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 280, 131, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_1.setAutoDefault(False)
        self.btn_1.setDefault(True)
        self.btn_1.setFlat(False)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(130, 280, 133, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_2.setFont(font)
        self.btn_2.setAutoFillBackground(False)
        self.btn_2.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_2.setAutoDefault(True)
        self.btn_2.setDefault(True)
        self.btn_2.setFlat(False)
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(260, 280, 131, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_3.setFont(font)
        self.btn_3.setMouseTracking(False)
        self.btn_3.setTabletTracking(False)
        self.btn_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_3.setAutoFillBackground(False)
        self.btn_3.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_3.setAutoDefault(True)
        self.btn_3.setDefault(True)
        self.btn_3.setFlat(False)
        self.btn_3.setProperty("color", QtGui.QColor(0, 0, 0))
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 170, 131, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_4.setDefault(True)
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(130, 170, 133, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_5.setDefault(True)
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(260, 170, 131, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_6.setAutoDefault(False)
        self.btn_6.setDefault(True)
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 60, 131, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_7.setDefault(True)
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(130, 60, 133, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_8.setDefault(True)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(260, 60, 131, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(35)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_9.setDefault(True)
        self.btn_9.setObjectName("btn_9")
        self.btn_c = QtWidgets.QPushButton(self.centralwidget)
        self.btn_c.setGeometry(QtCore.QRect(0, 500, 391, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_c.setFont(font)
        self.btn_c.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #898ED5;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"background: #9196DA;\n"
"}")
        self.btn_c.setAutoRepeat(True)
        self.btn_c.setAutoDefault(False)
        self.btn_c.setDefault(True)
        self.btn_c.setFlat(False)
        self.btn_c.setObjectName("btn_c")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(390, 60, 50, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_plus.setDefault(True)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(390, 170, 50, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_minus.setDefault(True)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult.setGeometry(QtCore.QRect(390, 280, 50, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_mult.setDefault(True)
        self.btn_mult.setObjectName("btn_mult")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(390, 390, 50, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_divide.setFont(font)
        self.btn_divide.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_divide.setDefault(True)
        self.btn_divide.setObjectName("btn_divide")
        self.btn_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sqrt.setGeometry(QtCore.QRect(440, 390, 50, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_sqrt.setDefault(True)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.btn_sqr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sqr.setGeometry(QtCore.QRect(440, 170, 50, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_sqr.setFont(font)
        self.btn_sqr.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_sqr.setDefault(True)
        self.btn_sqr.setObjectName("btn_sqr")
        self.btn_fact = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fact.setGeometry(QtCore.QRect(440, 60, 50, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_fact.setFont(font)
        self.btn_fact.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_fact.setDefault(True)
        self.btn_fact.setObjectName("btn_fact")
        self.btn_pi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pi.setGeometry(QtCore.QRect(440, 280, 50, 111))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_pi.setFont(font)
        self.btn_pi.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #E78A9A;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #ED96A5;\n"
"}")
        self.btn_pi.setDefault(True)
        self.btn_pi.setObjectName("btn_pi")
        self.btn_delete1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete1.setGeometry(QtCore.QRect(390, 500, 101, 50))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(20)
        self.btn_delete1.setFont(font)
        self.btn_delete1.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background: #898ED5;\n"
"border: 1px solid;\n"
"border-color: white;\n"
"border-radius: 5;\n"
"}\n"
"QPushButton:hover {\n"
"background: #9196DA;\n"
"}")
        self.btn_delete1.setAutoDefault(False)
        self.btn_delete1.setDefault(True)
        self.btn_delete1.setFlat(False)
        self.btn_delete1.setObjectName("btn_delete1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label_res.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_ravno.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_c.setText(_translate("MainWindow", "C"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_sqrt.setText(_translate("MainWindow", "√"))
        self.btn_sqr.setText(_translate("MainWindow", "^"))
        self.btn_fact.setText(_translate("MainWindow", "!"))
        self.btn_pi.setText(_translate("MainWindow", "π"))
        self.btn_delete1.setText(_translate("MainWindow", "<"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 801)
        MainWindow.setStyleSheet("QScrollBar:horizontal{\n"
                                 "    height:8px;\n"
                                 "    background:rgba(0,0,0,0%);\n"
                                 "border-radius:4px;\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::handle:horizontal{\n"
                                 "    background:rgba(125,125,125,50%);\n"
                                 "border-radius:4px;\n"
                                 "}\n"
                                 "QScrollBar::handle:horizontal:hover{\n"
                                 "    background:rgba(125,125,125,100%);\n"
                                 "    min-width:0;\n"
                                 "}\n"
                                 "QScrollBar::add-line:horizontal{\n"
                                 "    height:0px;width:0px;\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::sub-line:horizontal{\n"
                                 "    height:0px;width:0px;\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::add-line:horizontal:hover{\n"
                                 "    height:0px;width:0px;\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::sub-line:horizontal:hover{\n"
                                 "    height:0px;width:0px;\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal\n"
                                 "{\n"
                                 "    background:rgba(0,0,0,10%);\n"
                                 "    border-radius:4px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:vertical{\n"
                                 "    width:8px;\n"
                                 "    background:rgba(0,0,0,0%);\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::handle:vertical{\n"
                                 "    width:0px;\n"
                                 "    background:rgba(125,125,125,50%);\n"
                                 "    border-radius:4px;\n"
                                 "}\n"
                                 "QScrollBar::handle:vertical:hover{\n"
                                 "    width:0px;\n"
                                 "    background:rgba(125,125,125,100%);\n"
                                 "    border-radius:4px;\n"
                                 "    min-width:20;\n"
                                 "}\n"
                                 "QScrollBar::add-line:vertical{\n"
                                 "    height:0px;width:0px;\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::sub-line:vertical{\n"
                                 "    height:0px;width:0px;\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::add-line:vertical:hover{\n"
                                 "    height:0px;width:0px;\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::sub-line:vertical:hover{\n"
                                 "    height:0px;width:0px;\n"
                                 "\n"
                                 "}\n"
                                 "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
                                 "{\n"
                                 "    background:rgba(0,0,0,10%);\n"
                                 "    border-radius:4px;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame#frame{\n"
                                 "    background-color: rgba(255, 255, 255, 150);\n"
                                 "    border-radius:20px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
                                   "    background-color: rgba(255, 255, 255, 255);\n"
                                   "    border-radius:20px;\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(8, 0, 8, 12)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 12, 2, 12)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_close = QtWidgets.QPushButton(self.frame_2)
        self.btn_close.setMinimumSize(QtCore.QSize(36, 36))
        self.btn_close.setMaximumSize(QtCore.QSize(36, 36))
        self.btn_close.setStyleSheet("QPushButton {\n"
                                     "    color: #FFFFFF;\n"
                                     "    border-radius: 18px;\n"
                                     "    border-style: outset;\n"
                                     "    border: 2px solid rgb(255, 0, 0);\n"
                                     "    font-color: rgb(255, 0, 0);\n"
                                     "    font: 15pt \"Bauhaus 93\";\n"
                                     "    }\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(255, 0, 0);\n"
                                     "}")
        self.btn_close.setIconSize(QtCore.QSize(20, 20))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.btn_enlarge = QtWidgets.QPushButton(self.frame_2)
        self.btn_enlarge.setMinimumSize(QtCore.QSize(36, 36))
        self.btn_enlarge.setMaximumSize(QtCore.QSize(36, 36))
        self.btn_enlarge.setStyleSheet("QPushButton {\n"
                                       "    color: #FFFFFF;\n"
                                       "    border-radius: 18px;\n"
                                       "    border-style: outset;\n"
                                       "    border: 2px solid rgb(255, 170, 0);\n"
                                       "    font-color: rgb(85, 170, 0);\n"
                                       "    font: 15pt \"Bauhaus 93\";\n"
                                       "    }\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(255, 170, 0);\n"
                                       "}")
        self.btn_enlarge.setIconSize(QtCore.QSize(20, 20))
        self.btn_enlarge.setObjectName("btn_enlarge")
        self.horizontalLayout.addWidget(self.btn_enlarge)
        self.btn_contract = QtWidgets.QPushButton(self.frame_2)
        self.btn_contract.setMinimumSize(QtCore.QSize(36, 36))
        self.btn_contract.setMaximumSize(QtCore.QSize(36, 36))
        self.btn_contract.setStyleSheet("QPushButton {\n"
                                        "    color: #FFFFFF;\n"
                                        "    border-radius: 18px;\n"
                                        "    border-style: outset;\n"
                                        "    border: 2px solid rgb(85, 170, 0);\n"
                                        "    font-color: rgb(85, 170, 0);\n"
                                        "    font: 15pt \"Bauhaus 93\";\n"
                                        "    }\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(85, 170, 0);\n"
                                        "}")
        self.btn_contract.setObjectName("btn_contract")
        self.horizontalLayout.addWidget(self.btn_contract)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_select = QtWidgets.QPushButton(self.frame_2)
        self.btn_select.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_select.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_select.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_select.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(170, 170, 255);\n"
                                      "    color: #FFFFFF;\n"
                                      "    border-radius: 40px;\n"
                                      "    border-style: outset;\n"
                                      "\n"
                                      "    font: bold 15px;\n"
                                      "    border-color: rgb(255, 0, 0);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: lightgreen;\n"
                                      "}")
        self.btn_select.setText("")
        self.btn_select.setObjectName("btn_select")
        self.verticalLayout.addWidget(self.btn_select)
        self.btn_save_path = QtWidgets.QPushButton(self.frame_2)
        self.btn_save_path.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_save_path.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_save_path.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_save_path.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(170, 170, 255);\n"
                                         "    color: #FFFFFF;\n"
                                         "    border-radius: 40px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "    font: bold 15px;\n"
                                         "    border-color: rgb(255, 0, 0);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: lightgreen;\n"
                                         "}")
        self.btn_save_path.setText("")
        self.btn_save_path.setObjectName("btn_save_path")
        self.verticalLayout.addWidget(self.btn_save_path)
        self.btn_cond1 = QtWidgets.QPushButton(self.frame_2)
        self.btn_cond1.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_cond1.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_cond1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_cond1.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgb(170, 170, 255);\n"
                                     "    color: #FFFFFF;\n"
                                     "    border-radius: 40px;\n"
                                     "    border-style: outset;\n"
                                     "\n"
                                     "    font: bold 15px;\n"
                                     "    border-color: rgb(255, 0, 0);\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: lightgreen;\n"
                                     "}")
        self.btn_cond1.setText("")
        self.btn_cond1.setObjectName("btn_cond1")
        self.verticalLayout.addWidget(self.btn_cond1)
        self.btn_col1 = QtWidgets.QPushButton(self.frame_2)
        self.btn_col1.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_col1.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_col1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_col1.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(170, 170, 255);\n"
                                    "    color: #FFFFFF;\n"
                                    "    border-radius: 40px;\n"
                                    "    border-style: outset;\n"
                                    "\n"
                                    "    font: bold 15px;\n"
                                    "    border-color: rgb(255, 0, 0);\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: lightgreen;\n"
                                    "}")
        self.btn_col1.setText("")
        self.btn_col1.setObjectName("btn_col1")
        self.verticalLayout.addWidget(self.btn_col1)
        self.btn_run = QtWidgets.QPushButton(self.frame_2)
        self.btn_run.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_run.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_run.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_run.setStyleSheet("QPushButton {\n"
                                   "    background-color: rgb(170, 170, 255);\n"
                                   "    color: #FFFFFF;\n"
                                   "    border-radius: 40px;\n"
                                   "    border-style: outset;\n"
                                   "\n"
                                   "    font: bold 15px;\n"
                                   "    border-color: rgb(255, 0, 0);\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: lightgreen;\n"
                                   "}")
        self.btn_run.setText("")
        self.btn_run.setObjectName("btn_run")
        self.verticalLayout.addWidget(self.btn_run)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_about = QtWidgets.QPushButton(self.frame_2)
        self.btn_about.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_about.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_about.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgb(170, 170, 255);\n"
                                     "    color: #FFFFFF;\n"
                                     "    border-radius: 40px;\n"
                                     "    border-style: outset;\n"
                                     "\n"
                                     "    font: bold 15px;\n"
                                     "    border-color: rgb(255, 0, 0);\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: lightgreen;\n"
                                     "}")
        self.btn_about.setText("")
        self.btn_about.setObjectName("btn_about")
        self.verticalLayout.addWidget(self.btn_about)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7.addWidget(self.frame_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet(".QFrame{\n"
                                   "    background-color: rgba(255, 255, 255, 0);\n"
                                   "    border-radius:20px;\n"
                                   "}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(-1, 24, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    background-color: rgba(245, 244, 246,200);\n"
                                    "    border:0px solid red;\n"
                                    "    border-radius:14px;\n"
                                    "    \n"
                                    "    font: 75 14pt \"Calibri\";\n"
                                    "}")
        self.lineEdit.setMaxLength(200)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_sep = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_sep.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_sep.setStyleSheet("QLineEdit{\n"
                                        "    background-color: rgba(245, 244, 246,200);\n"
                                        "    border:0px solid red;\n"
                                        "    border-radius:14px;\n"
                                        "    \n"
                                        "    font: 75 14pt \"Calibri\";\n"
                                        "}")
        self.lineEdit_sep.setObjectName("lineEdit_sep")
        self.horizontalLayout_2.addWidget(self.lineEdit_sep)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet(".QFrame{\n"
                                   "    background-color: rgba(255, 255, 255, 0);\n"
                                   "    border-radius:20px;\n"
                                   "}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setStyleSheet("QWidget{\n"
                                      "border:none;\n"
                                      "    background-color: rgba(255, 255, 255, 0);\n"
                                      "}")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 498, 702))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setContentsMargins(36, 36, 124, 36)
        self.verticalLayout_13.setSpacing(24)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setMinimumSize(QtCore.QSize(200, 500))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
                                       "    background-color: rgba(245, 244, 246,200);\n"
                                       "    border:0px solid red;\n"
                                       "    border-radius:14px;\n"
                                       "    font: 75 16pt \"Calibri\";\n"
                                       "}")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_13.addWidget(self.textBrowser)
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    font-size: 20px;\n"
                                       "    border: 2px solid grey;\n"
                                       "    border-radius: 5px;\n"
                                       "    color: rgb(0, 0, 0);\n"
                                       "    background-color: rgba(245, 244, 246,200);\n"
                                       "    text-align: center;\n"
                                       "}\n"
                                       "QProgressBar:: chunk {\n"
                                       "    background-color: rgba(245, 244, 246,200);\n"
                                       "    border-radius: 10px;\n"
                                       "    margin: 0.1px;\n"
                                       "    width: 1px;\n"
                                       "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_13.addWidget(self.progressBar)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_13.addWidget(self.scrollArea)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.verticalLayout_6.setStretch(1, 1)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_7.setStretch(1, 4)
        self.horizontalLayout_8.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_close.setText(_translate("MainWindow", "×"))
        self.btn_enlarge.setText(_translate("MainWindow", "+"))
        self.btn_contract.setText(_translate("MainWindow", "-"))

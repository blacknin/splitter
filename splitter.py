# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splitter.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Splitter(object):
    def setupUi(self, Splitter):
        Splitter.setObjectName("Splitter")
        Splitter.resize(800, 600)
        Splitter.setMinimumSize(QtCore.QSize(800, 600))
        Splitter.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(Splitter)
        self.centralwidget.setObjectName("centralwidget")
        self.scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(20, 110, 350, 370))
        self.scroll_area.setMinimumSize(QtCore.QSize(350, 370))
        self.scroll_area.setMaximumSize(QtCore.QSize(350, 350))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 331, 386))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.end_doc_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_10.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_10.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_10.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_10.setObjectName("end_doc_10")
        self.gridLayout.addWidget(self.end_doc_10, 9, 2, 1, 1)
        self.end_doc_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_4.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_4.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_4.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_4.setObjectName("end_doc_4")
        self.gridLayout.addWidget(self.end_doc_4, 3, 2, 1, 1)
        self.name_doc_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_12.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_12.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_12.setObjectName("name_doc_12")
        self.gridLayout.addWidget(self.name_doc_12, 11, 3, 1, 1)
        self.end_doc_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_7.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_7.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_7.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_7.setObjectName("end_doc_7")
        self.gridLayout.addWidget(self.end_doc_7, 6, 2, 1, 1)
        self.name_doc_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_3.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_3.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_3.setObjectName("name_doc_3")
        self.gridLayout.addWidget(self.name_doc_3, 2, 3, 1, 1)
        self.name_doc_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_5.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_5.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_5.setObjectName("name_doc_5")
        self.gridLayout.addWidget(self.name_doc_5, 4, 3, 1, 1)
        self.name_doc_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_8.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_8.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_8.setObjectName("name_doc_8")
        self.gridLayout.addWidget(self.name_doc_8, 7, 3, 1, 1)
        self.begin_doc_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_9.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_9.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_9.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_9.setObjectName("begin_doc_9")
        self.gridLayout.addWidget(self.begin_doc_9, 8, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.end_doc_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_6.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_6.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_6.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_6.setObjectName("end_doc_6")
        self.gridLayout.addWidget(self.end_doc_6, 5, 2, 1, 1)
        self.end_doc_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_9.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_9.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_9.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_9.setObjectName("end_doc_9")
        self.gridLayout.addWidget(self.end_doc_9, 8, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.name_doc_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_2.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_2.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_2.setObjectName("name_doc_2")
        self.gridLayout.addWidget(self.name_doc_2, 1, 3, 1, 1)
        self.end_doc_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_2.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_2.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_2.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_2.setObjectName("end_doc_2")
        self.gridLayout.addWidget(self.end_doc_2, 1, 2, 1, 1)
        self.begin_doc_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_10.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_10.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_10.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_10.setObjectName("begin_doc_10")
        self.gridLayout.addWidget(self.begin_doc_10, 9, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.begin_doc_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_6.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_6.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_6.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_6.setObjectName("begin_doc_6")
        self.gridLayout.addWidget(self.begin_doc_6, 5, 1, 1, 1)
        self.end_doc_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_8.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_8.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_8.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_8.setObjectName("end_doc_8")
        self.gridLayout.addWidget(self.end_doc_8, 7, 2, 1, 1, QtCore.Qt.AlignVCenter)
        self.name_doc_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_9.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_9.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_9.setObjectName("name_doc_9")
        self.gridLayout.addWidget(self.name_doc_9, 8, 3, 1, 1, QtCore.Qt.AlignVCenter)
        self.name_doc_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_10.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_10.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_10.setObjectName("name_doc_10")
        self.gridLayout.addWidget(self.name_doc_10, 9, 3, 1, 1)
        self.begin_doc_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_3.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_3.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_3.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_3.setObjectName("begin_doc_3")
        self.gridLayout.addWidget(self.begin_doc_3, 2, 1, 1, 1)
        self.begin_doc_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_5.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_5.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_5.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_5.setObjectName("begin_doc_5")
        self.gridLayout.addWidget(self.begin_doc_5, 4, 1, 1, 1)
        self.end_doc_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_1.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_1.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_1.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_1.setObjectName("end_doc_1")
        self.gridLayout.addWidget(self.end_doc_1, 0, 2, 1, 1)
        self.name_doc_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_4.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_4.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_4.setObjectName("name_doc_4")
        self.gridLayout.addWidget(self.name_doc_4, 3, 3, 1, 1)
        self.end_doc_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_3.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_3.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_3.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_3.setObjectName("end_doc_3")
        self.gridLayout.addWidget(self.end_doc_3, 2, 2, 1, 1)
        self.begin_doc_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_2.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_2.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_2.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_2.setObjectName("begin_doc_2")
        self.gridLayout.addWidget(self.begin_doc_2, 1, 1, 1, 1)
        self.end_doc_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_12.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_12.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_12.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_12.setObjectName("end_doc_12")
        self.gridLayout.addWidget(self.end_doc_12, 11, 2, 1, 1)
        self.begin_doc_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_8.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_8.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_8.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_8.setObjectName("begin_doc_8")
        self.gridLayout.addWidget(self.begin_doc_8, 7, 1, 1, 1)
        self.end_doc_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_11.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_11.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_11.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_11.setObjectName("end_doc_11")
        self.gridLayout.addWidget(self.end_doc_11, 10, 2, 1, 1)
        self.begin_doc_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_7.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_7.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_7.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_7.setObjectName("begin_doc_7")
        self.gridLayout.addWidget(self.begin_doc_7, 6, 1, 1, 1)
        self.name_doc_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_1.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_1.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_1.setObjectName("name_doc_1")
        self.gridLayout.addWidget(self.name_doc_1, 0, 3, 1, 1)
        self.begin_doc_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_1.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_1.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_1.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_1.setObjectName("begin_doc_1")
        self.gridLayout.addWidget(self.begin_doc_1, 0, 1, 1, 1)
        self.name_doc_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_6.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_6.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_6.setObjectName("name_doc_6")
        self.gridLayout.addWidget(self.name_doc_6, 5, 3, 1, 1)
        self.begin_doc_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_4.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_4.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_4.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_4.setObjectName("begin_doc_4")
        self.gridLayout.addWidget(self.begin_doc_4, 3, 1, 1, 1)
        self.name_doc_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_7.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_7.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_7.setObjectName("name_doc_7")
        self.gridLayout.addWidget(self.name_doc_7, 6, 3, 1, 1)
        self.begin_doc_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_11.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_11.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_11.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_11.setObjectName("begin_doc_11")
        self.gridLayout.addWidget(self.begin_doc_11, 10, 1, 1, 1)
        self.name_doc_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.name_doc_11.setMinimumSize(QtCore.QSize(215, 25))
        self.name_doc_11.setMaximumSize(QtCore.QSize(215, 25))
        self.name_doc_11.setObjectName("name_doc_11")
        self.gridLayout.addWidget(self.name_doc_11, 10, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.end_doc_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.end_doc_5.setMinimumSize(QtCore.QSize(25, 25))
        self.end_doc_5.setMaximumSize(QtCore.QSize(25, 25))
        self.end_doc_5.setAlignment(QtCore.Qt.AlignCenter)
        self.end_doc_5.setObjectName("end_doc_5")
        self.gridLayout.addWidget(self.end_doc_5, 4, 2, 1, 1)
        self.begin_doc_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.begin_doc_12.setMinimumSize(QtCore.QSize(25, 25))
        self.begin_doc_12.setMaximumSize(QtCore.QSize(25, 25))
        self.begin_doc_12.setAlignment(QtCore.Qt.AlignCenter)
        self.begin_doc_12.setObjectName("begin_doc_12")
        self.gridLayout.addWidget(self.begin_doc_12, 11, 1, 1, 1)
        self.section_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_1.setMinimumSize(QtCore.QSize(25, 25))
        self.section_1.setMaximumSize(QtCore.QSize(25, 25))
        self.section_1.setAlignment(QtCore.Qt.AlignCenter)
        self.section_1.setObjectName("section_1")
        self.gridLayout.addWidget(self.section_1, 0, 0, 1, 1)
        self.section_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_2.setMinimumSize(QtCore.QSize(25, 25))
        self.section_2.setMaximumSize(QtCore.QSize(25, 25))
        self.section_2.setAlignment(QtCore.Qt.AlignCenter)
        self.section_2.setObjectName("section_2")
        self.gridLayout.addWidget(self.section_2, 1, 0, 1, 1)
        self.section_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_3.setMinimumSize(QtCore.QSize(25, 25))
        self.section_3.setMaximumSize(QtCore.QSize(25, 25))
        self.section_3.setAlignment(QtCore.Qt.AlignCenter)
        self.section_3.setObjectName("section_3")
        self.gridLayout.addWidget(self.section_3, 2, 0, 1, 1)
        self.section_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_4.setMinimumSize(QtCore.QSize(25, 25))
        self.section_4.setMaximumSize(QtCore.QSize(25, 25))
        self.section_4.setAlignment(QtCore.Qt.AlignCenter)
        self.section_4.setObjectName("section_4")
        self.gridLayout.addWidget(self.section_4, 3, 0, 1, 1)
        self.section_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_5.setMinimumSize(QtCore.QSize(25, 25))
        self.section_5.setMaximumSize(QtCore.QSize(25, 25))
        self.section_5.setAlignment(QtCore.Qt.AlignCenter)
        self.section_5.setObjectName("section_5")
        self.gridLayout.addWidget(self.section_5, 4, 0, 1, 1)
        self.section_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_6.setMinimumSize(QtCore.QSize(25, 25))
        self.section_6.setMaximumSize(QtCore.QSize(25, 25))
        self.section_6.setAlignment(QtCore.Qt.AlignCenter)
        self.section_6.setObjectName("section_6")
        self.gridLayout.addWidget(self.section_6, 5, 0, 1, 1)
        self.section_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_7.setMinimumSize(QtCore.QSize(25, 25))
        self.section_7.setMaximumSize(QtCore.QSize(25, 25))
        self.section_7.setAlignment(QtCore.Qt.AlignCenter)
        self.section_7.setObjectName("section_7")
        self.gridLayout.addWidget(self.section_7, 6, 0, 1, 1)
        self.section_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_8.setMinimumSize(QtCore.QSize(25, 25))
        self.section_8.setMaximumSize(QtCore.QSize(25, 25))
        self.section_8.setAlignment(QtCore.Qt.AlignCenter)
        self.section_8.setObjectName("section_8")
        self.gridLayout.addWidget(self.section_8, 7, 0, 1, 1)
        self.section_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_9.setMinimumSize(QtCore.QSize(25, 25))
        self.section_9.setMaximumSize(QtCore.QSize(25, 25))
        self.section_9.setAlignment(QtCore.Qt.AlignCenter)
        self.section_9.setObjectName("section_9")
        self.gridLayout.addWidget(self.section_9, 8, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.section_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_10.setMinimumSize(QtCore.QSize(25, 25))
        self.section_10.setMaximumSize(QtCore.QSize(25, 25))
        self.section_10.setAlignment(QtCore.Qt.AlignCenter)
        self.section_10.setObjectName("section_10")
        self.gridLayout.addWidget(self.section_10, 9, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.section_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_11.setMinimumSize(QtCore.QSize(25, 25))
        self.section_11.setMaximumSize(QtCore.QSize(25, 25))
        self.section_11.setAlignment(QtCore.Qt.AlignCenter)
        self.section_11.setObjectName("section_11")
        self.gridLayout.addWidget(self.section_11, 10, 0, 1, 1)
        self.section_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.section_12.setMinimumSize(QtCore.QSize(25, 25))
        self.section_12.setMaximumSize(QtCore.QSize(25, 25))
        self.section_12.setAlignment(QtCore.Qt.AlignCenter)
        self.section_12.setObjectName("section_12")
        self.gridLayout.addWidget(self.section_12, 11, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.line_input = QtWidgets.QLineEdit(self.centralwidget)
        self.line_input.setGeometry(QtCore.QRect(20, 30, 270, 25))
        self.line_input.setMinimumSize(QtCore.QSize(270, 25))
        self.line_input.setMaximumSize(QtCore.QSize(270, 25))
        self.line_input.setWhatsThis("")
        self.line_input.setObjectName("line_input")
        self.button_input = QtWidgets.QPushButton(self.centralwidget)
        self.button_input.setGeometry(QtCore.QRect(300, 30, 75, 25))
        self.button_input.setMinimumSize(QtCore.QSize(75, 25))
        self.button_input.setMaximumSize(QtCore.QSize(75, 25))
        self.button_input.setObjectName("button_input")
        self.label_preview = QtWidgets.QLabel(self.centralwidget)
        self.label_preview.setGeometry(QtCore.QRect(410, 30, 360, 450))
        self.label_preview.setMinimumSize(QtCore.QSize(360, 450))
        self.label_preview.setMaximumSize(QtCore.QSize(360, 450))
        self.label_preview.setText("")
        self.label_preview.setObjectName("label_preview")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(240, 520, 350, 20))
        self.progress_bar.setMinimumSize(QtCore.QSize(350, 20))
        self.progress_bar.setMaximumSize(QtCore.QSize(350, 20))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(380, 550, 50, 25))
        self.button_start.setMinimumSize(QtCore.QSize(50, 25))
        self.button_start.setMaximumSize(QtCore.QSize(50, 25))
        self.button_start.setObjectName("button_start")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(20, 480, 25, 25))
        self.button_add.setMinimumSize(QtCore.QSize(25, 25))
        self.button_add.setMaximumSize(QtCore.QSize(25, 25))
        self.button_add.setObjectName("button_add")
        self.button_previous = QtWidgets.QPushButton(self.centralwidget)
        self.button_previous.setGeometry(QtCore.QRect(530, 480, 25, 25))
        self.button_previous.setMinimumSize(QtCore.QSize(25, 25))
        self.button_previous.setMaximumSize(QtCore.QSize(25, 25))
        self.button_previous.setObjectName("button_previous")
        self.last_page = QtWidgets.QLineEdit(self.centralwidget)
        self.last_page.setEnabled(False)
        self.last_page.setGeometry(QtCore.QRect(600, 480, 25, 25))
        self.last_page.setMinimumSize(QtCore.QSize(25, 25))
        self.last_page.setMaximumSize(QtCore.QSize(25, 25))
        self.last_page.setFrame(True)
        self.last_page.setObjectName("last_page")
        self.current_page = QtWidgets.QLineEdit(self.centralwidget)
        self.current_page.setGeometry(QtCore.QRect(560, 480, 25, 25))
        self.current_page.setMinimumSize(QtCore.QSize(25, 25))
        self.current_page.setMaximumSize(QtCore.QSize(25, 25))
        self.current_page.setObjectName("current_page")
        self.label_separator = QtWidgets.QLabel(self.centralwidget)
        self.label_separator.setGeometry(QtCore.QRect(590, 480, 5, 25))
        self.label_separator.setMinimumSize(QtCore.QSize(5, 25))
        self.label_separator.setMaximumSize(QtCore.QSize(5, 25))
        self.label_separator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_separator.setObjectName("label_separator")
        self.line_output = QtWidgets.QLineEdit(self.centralwidget)
        self.line_output.setGeometry(QtCore.QRect(20, 65, 270, 25))
        self.line_output.setMinimumSize(QtCore.QSize(270, 25))
        self.line_output.setMaximumSize(QtCore.QSize(270, 25))
        self.line_output.setObjectName("line_output")
        self.button_output = QtWidgets.QPushButton(self.centralwidget)
        self.button_output.setGeometry(QtCore.QRect(300, 65, 75, 25))
        self.button_output.setMinimumSize(QtCore.QSize(75, 25))
        self.button_output.setMaximumSize(QtCore.QSize(75, 25))
        self.button_output.setObjectName("button_output")
        self.button_remove = QtWidgets.QPushButton(self.centralwidget)
        self.button_remove.setGeometry(QtCore.QRect(50, 480, 25, 25))
        self.button_remove.setMinimumSize(QtCore.QSize(25, 25))
        self.button_remove.setMaximumSize(QtCore.QSize(25, 25))
        self.button_remove.setObjectName("button_remove")
        self.button_next = QtWidgets.QPushButton(self.centralwidget)
        self.button_next.setGeometry(QtCore.QRect(630, 480, 25, 25))
        self.button_next.setMinimumSize(QtCore.QSize(25, 25))
        self.button_next.setMaximumSize(QtCore.QSize(25, 25))
        self.button_next.setObjectName("button_next")
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(320, 480, 50, 25))
        self.button_reset.setMinimumSize(QtCore.QSize(50, 25))
        self.button_reset.setMaximumSize(QtCore.QSize(50, 25))
        self.button_reset.setObjectName("button_reset")
        Splitter.setCentralWidget(self.centralwidget)
        self.status_bar = QtWidgets.QStatusBar(Splitter)
        self.status_bar.setObjectName("status_bar")
        Splitter.setStatusBar(self.status_bar)

        self.retranslateUi(Splitter)
        QtCore.QMetaObject.connectSlotsByName(Splitter)

    def retranslateUi(self, Splitter):
        _translate = QtCore.QCoreApplication.translate
        Splitter.setWindowTitle(_translate("Splitter", "Splitter"))
        self.name_doc_12.setText(_translate("Splitter", "forma de ingresso"))
        self.name_doc_3.setText(_translate("Splitter", "certidão de nascimento"))
        self.name_doc_5.setText(_translate("Splitter", "cpf"))
        self.name_doc_8.setText(_translate("Splitter", "comprovante de residencia"))
        self.name_doc_2.setText(_translate("Splitter", "contrato de prestação de serviço"))
        self.name_doc_9.setText(_translate("Splitter", "declaração de quitação eleitoral"))
        self.name_doc_10.setText(_translate("Splitter", "histórico escolar de ensino médio"))
        self.name_doc_4.setText(_translate("Splitter", "rg"))
        self.name_doc_1.setText(_translate("Splitter", "requerimento de matricula"))
        self.name_doc_6.setText(_translate("Splitter", "titulo de eleitor"))
        self.name_doc_7.setText(_translate("Splitter", "carteira de reservista"))
        self.name_doc_11.setText(_translate("Splitter", "certificado de conclusão de ensino médio"))
        self.section_1.setText(_translate("Splitter", "1"))
        self.section_2.setText(_translate("Splitter", "1"))
        self.section_3.setText(_translate("Splitter", "2"))
        self.section_4.setText(_translate("Splitter", "2"))
        self.section_5.setText(_translate("Splitter", "2"))
        self.section_6.setText(_translate("Splitter", "2"))
        self.section_7.setText(_translate("Splitter", "2"))
        self.section_8.setText(_translate("Splitter", "2"))
        self.section_9.setText(_translate("Splitter", "2"))
        self.section_10.setText(_translate("Splitter", "3"))
        self.section_11.setText(_translate("Splitter", "3"))
        self.section_12.setText(_translate("Splitter", "4"))
        self.line_input.setToolTip(_translate("Splitter", "<html><head/><body><p>caminho para o pdf</p></body></html>"))
        self.button_input.setText(_translate("Splitter", "select file"))
        self.button_start.setText(_translate("Splitter", "start"))
        self.button_add.setText(_translate("Splitter", "+"))
        self.button_previous.setText(_translate("Splitter", "<"))
        self.label_separator.setText(_translate("Splitter", "/"))
        self.line_output.setToolTip(_translate("Splitter", "<html><head/><body><p>pasta destino</p></body></html>"))
        self.button_output.setText(_translate("Splitter", "select folder"))
        self.button_remove.setText(_translate("Splitter", "-"))
        self.button_next.setText(_translate("Splitter", ">"))
        self.button_reset.setText(_translate("Splitter", "reset"))

        self.button_input.clicked.connect(self.select_file)
        self.button_output.clicked.connect(self.select_folder)
        self.button_next.clicked.connect(self.load_next_page)
        self.button_previous.clicked.connect(self.load_previous_page)
        self.button_reset.clicked.connect(self.reset_docs)
        self.button_add.clicked.connect(self.add_doc_fields)
        self.button_remove.clicked.connect(self.remove_doc_fields)
        self.button_start.clicked.connect(self.split)

        self.docs = []

    def select_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), "Select Pdf", "", "pdf (*.pdf)")

        path = file[0]

        if is_valid_path(path):
            self.line_input.setText(path)
            self.load_preview(0)
        else:
            self.line_input.setText('')

    def select_folder(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QFileDialog(), "Select Folder")

        if is_valid_path(path):
            self.line_output.setText(path)

    def load_previous_page(self):
        current_page = self.current_page.text()
        last_page = self.last_page.text()

        if are_valid_pages(current_page, last_page):
            current_page = int(current_page)
            current_page -= 1
            last_page = int(last_page)

            if 0 < current_page <= last_page:
                self.current_page.setText(str(current_page))
            elif current_page <= 0:
                current_page = 1
                self.current_page.setText(str(current_page))
            elif current_page > last_page:
                current_page = last_page
                self.current_page.setText(str(last_page))

            self.load_preview(current_page - 1)

    def load_next_page(self):
        current_page = self.current_page.text()
        last_page = self.last_page.text()

        if are_valid_pages(current_page, last_page):
            current_page = int(current_page)
            current_page += 1
            last_page = int(last_page)

            if 0 < current_page < last_page:
                self.current_page.setText(str(current_page))
            elif current_page <= 0:
                current_page = 1
                self.current_page.setText(str(current_page))
            elif current_page > last_page:
                current_page = last_page
                self.current_page.setText(str(last_page))

            self.load_preview(current_page - 1)

    def load_preview(self, page_number):
        import fitz

        pdf = fitz.open(self.line_input.text())

        page = pdf.loadPage(page_number)
        pix = page.getPixmap(alpha = False)
        fmt = QtGui.QImage.Format_RGBA8888 if pix.alpha else QtGui.QImage.Format_RGB888
        qt_img = QtGui.QImage(pix.samples, pix.width, pix.height, pix.stride, fmt)

        self.label_preview.setPixmap(QtGui.QPixmap.fromImage(qt_img))
        self.current_page.setText(str(page_number + 1))
        self.last_page.setText(str(pdf.pageCount))

        pdf.close()

    def reset_docs(self):
        self.section_1.setText('1')
        self.section_2.setText('1')
        self.section_3.setText('2')
        self.section_4.setText('2')
        self.section_5.setText('2')
        self.section_6.setText('2')
        self.section_7.setText('2')
        self.section_8.setText('2')
        self.section_9.setText('2')
        self.section_10.setText('3')
        self.section_11.setText('3')
        self.section_12.setText('4')
        self.begin_doc_1.setText('')
        self.begin_doc_2.setText('')
        self.begin_doc_3.setText('')
        self.begin_doc_4.setText('')
        self.begin_doc_5.setText('')
        self.begin_doc_6.setText('')
        self.begin_doc_7.setText('')
        self.begin_doc_8.setText('')
        self.begin_doc_9.setText('')
        self.begin_doc_10.setText('')
        self.begin_doc_11.setText('')
        self.begin_doc_12.setText('')
        self.end_doc_1.setText('')
        self.end_doc_2.setText('')
        self.end_doc_3.setText('')
        self.end_doc_4.setText('')
        self.end_doc_5.setText('')
        self.end_doc_6.setText('')
        self.end_doc_7.setText('')
        self.end_doc_8.setText('')
        self.end_doc_9.setText('')
        self.end_doc_10.setText('')
        self.end_doc_11.setText('')
        self.end_doc_12.setText('')
        self.name_doc_1.setText('requerimento de matricula')
        self.name_doc_2.setText('contrato de prestação de serviço')
        self.name_doc_3.setText('certidão de nascimento')
        self.name_doc_4.setText('rg')
        self.name_doc_5.setText('cpf')
        self.name_doc_6.setText('titulo de eleitor')
        self.name_doc_7.setText('carteira de reservista')
        self.name_doc_8.setText('comprovante de residencia')
        self.name_doc_9.setText('declaração de quitação eleitoral')
        self.name_doc_10.setText('histórico escolar de ensino médio')
        self.name_doc_11.setText('certificado de conclusão de ensino médio')
        self.name_doc_12.setText('forma de ingresso')
        self.progress_bar.setValue(0)

    def add_doc_fields(self):
        # sector
        self.docs.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
        # begin page
        self.docs.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
        # end page
        self.docs.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))
        # doc name
        self.docs.append(QtWidgets.QLineEdit(self.scrollAreaWidgetContents))

        row = 11 + int((len(self.docs) / 4))

        # sector
        self.docs[-4].setMinimumSize(QtCore.QSize(25, 25))
        self.docs[-4].setMaximumSize(QtCore.QSize(25, 25))
        self.docs[-4].setAlignment(QtCore.Qt.AlignCenter)
        self.docs[-4].setObjectName(f"section_{row}")

        # begin page
        self.docs[-3].setMinimumSize(QtCore.QSize(25, 25))
        self.docs[-3].setMaximumSize(QtCore.QSize(25, 25))
        self.docs[-3].setAlignment(QtCore.Qt.AlignCenter)
        self.docs[-4].setObjectName(f"begin_doc_{row}")

        # end page
        self.docs[-2].setMinimumSize(QtCore.QSize(25, 25))
        self.docs[-2].setMaximumSize(QtCore.QSize(25, 25))
        self.docs[-2].setAlignment(QtCore.Qt.AlignCenter)
        self.docs[-4].setObjectName(f"end_doc_{row}")

        # doc name
        self.docs[-1].setMinimumSize(QtCore.QSize(215, 25))
        self.docs[-1].setMaximumSize(QtCore.QSize(215, 25))
        self.docs[-4].setObjectName(f"name_doc_{row}")

        self.gridLayout.addWidget(self.docs[-4], row, 0, 1, 1)
        self.gridLayout.addWidget(self.docs[-3], row, 1, 1, 1)
        self.gridLayout.addWidget(self.docs[-2], row, 2, 1, 1)
        self.gridLayout.addWidget(self.docs[-1], row, 3, 1, 1)

    def remove_doc_fields(self):
        if len(self.docs) > 0:
            # sector
            self.scrollAreaWidgetContents.layout().removeWidget(self.docs[-1])
            self.docs[-1].deleteLater()

            # begin page
            self.scrollAreaWidgetContents.layout().removeWidget(self.docs[-2])
            self.docs[-2].deleteLater()

            # end page
            self.scrollAreaWidgetContents.layout().removeWidget(self.docs[-3])
            self.docs[-3].deleteLater()

            # doc name
            self.scrollAreaWidgetContents.layout().removeWidget(self.docs[-4])
            self.docs[-4].deleteLater()

            self.docs.pop()
            self.docs.pop()
            self.docs.pop()
            self.docs.pop()

    def split(self):
        import os

        input_path = self.line_input.text()
        output_path = self.line_output.text()

        if is_valid_path(input_path) and is_valid_path(output_path):
            folder = input_path.split('/')
            folder = folder[-1]
            folder = folder[:-4]
            folder = output_path + '/' + folder

            if not os.path.exists(folder):
                os.mkdir(folder)

            if not split_doc(input_path, output_path, self.section_1.text(), self.begin_doc_1.text(), self.end_doc_1.text(), self.name_doc_1.text()):
                print("warning - Faltando argumentos no 1º documento")

            self.progress_bar.setValue(10)

            if not split_doc(input_path, output_path, self.section_2.text(), self.begin_doc_2.text(), self.end_doc_2.text(), self.name_doc_2.text()):
                print("warning - Faltando argumentos no 2º documento")

            self.progress_bar.setValue(15)

            if not split_doc(input_path, output_path, self.section_3.text(), self.begin_doc_3.text(), self.end_doc_3.text(), self.name_doc_3.text()):
                print("warning - Faltando argumentos no 3º documento")

            self.progress_bar.setValue(20)

            if not split_doc(input_path, output_path, self.section_4.text(), self.begin_doc_4.text(), self.end_doc_4.text(), self.name_doc_4.text()):
                print("warning - Faltando argumentos no 4º documento")

            self.progress_bar.setValue(25)

            if not split_doc(input_path, output_path, self.section_5.text(), self.begin_doc_5.text(), self.end_doc_5.text(), self.name_doc_5.text()):
                print("warning - Faltando argumentos no 5º documento")

            self.progress_bar.setValue(30)

            if not split_doc(input_path, output_path, self.section_6.text(), self.begin_doc_6.text(), self.end_doc_6.text(), self.name_doc_6.text()):
                print("warning - Faltando argumentos no 6º documento")

            self.progress_bar.setValue(35)

            if not split_doc(input_path, output_path, self.section_7.text(), self.begin_doc_7.text(), self.end_doc_7.text(), self.name_doc_7.text()):
                print("warning - Faltando argumentos no 7º documento")

            self.progress_bar.setValue(40)

            if not split_doc(input_path, output_path, self.section_8.text(), self.begin_doc_8.text(), self.end_doc_8.text(), self.name_doc_8.text()):
                print("warning - Faltando argumentos no 8º documento")

            self.progress_bar.setValue(45)

            if not split_doc(input_path, output_path, self.section_9.text(), self.begin_doc_9.text(), self.end_doc_9.text(), self.name_doc_9.text()):
                print("warning - Faltando argumentos no 9º documento")

            self.progress_bar.setValue(50)

            if not split_doc(input_path, output_path, self.section_10.text(), self.begin_doc_10.text(), self.end_doc_10.text(),
                             self.name_doc_10.text()):
                print("warning - Faltando argumentos no 10º documento")

            self.progress_bar.setValue(55)

            if not split_doc(input_path, output_path, self.section_11.text(), self.begin_doc_11.text(), self.end_doc_11.text(),
                             self.name_doc_11.text()):
                print("warning - Faltando argumentos no 11º documento")

            self.progress_bar.setValue(60)

            if not split_doc(input_path, output_path, self.section_12.text(), self.begin_doc_12.text(), self.end_doc_12.text(),
                             self.name_doc_12.text()):
                print("warning - Faltando argumentos no 12º documento")

            self.progress_bar.setValue(100 - len(self.docs))

            if len(self.docs) > 0:
                for i in range(0, len(self.docs), 4):
                    if not split_doc(input_path, output_path, self.docs[i].text(), self.docs[i + 1].text(), self.docs[i + 2].text(),
                                     self.docs[i + 3].text()):
                        print(f"warning - Faltando argumentos no {13 + i - 4}º documento")
                    self.progress_bar.setValue(self.progress_bar.value() + i)

            self.progress_bar.setValue(100)

            print("Finished")


def is_valid_section(section):
    import re

    if section is not None:
        if section is not str:
            section = str(section)

        if re.match(r"-?[0-9]+", section):
            return True
    else:
        return False


def split_doc(input_path, output_path, section, begin_page, end_page, name):
    import os
    import fitz

    if is_valid_path(input_path) and is_valid_path(output_path) and are_valid_pages(begin_page, end_page) and is_valid_section(section):
        if begin_page is not int:
            begin_page = int(begin_page)
        if end_page is not int:
            end_page = int(end_page)

        folder = input_path.split("/")
        folder = folder[-1]
        folder = folder[:-4]
        folder = output_path + "/" + folder

        if not os.path.exists(folder):
            os.mkdir(folder)

        name = replace_invalid_chars(name)

        begin_page -= 1
        end_page -= 1

        document_1 = fitz.open(input_path)
        document_2 = fitz.open()

        document_2.insertPDF(document_1, from_page = begin_page, to_page = end_page)

        pdf_a = folder + "/" + section + "_" + name + ".pdf"

        pdf = folder + "/" + section + "_" + name + "_not_pdf_a.pdf"

        document_2.save(pdf)

        document_1.close()
        document_2.close()

        gs_path = 'C:/splitter/dependencies/gs9.20/bin/gswin32c'
        pdf_a_def_path = 'C:/splitter/dependencies/PDFA_def.ps'
        gs_args = f'-dPDFA -dNOOUTERSAVE -sProcessColorModel=DeviceRGB -dUseCIEColor -sDEVICE=pdfwrite -o {pdf_a} -dPDFACompatibilityPolicy=1 {pdf_a_def_path}'

        os.system(f"{gs_path} {gs_args} {pdf}")
        return True

    else:
        return False


def replace_invalid_chars(name):
    name = name.replace(" ", "_")
    name = name.replace("ç", "c")
    name = name.replace("ã", "a")
    name = name.replace("õ", "o")
    name = name.replace("á", "a")
    name = name.replace("é", "e")
    name = name.replace("í", "i")
    name = name.replace("ó", "o")
    name = name.replace("ú", "u")
    name = name.upper()

    return name


def are_valid_pages(begin_page, end_page):
    import re

    if begin_page is not None and end_page is not None:
        if begin_page is not str:
            begin_page = str(begin_page)
        if end_page is not str:
            end_page = str(end_page)

        if re.match(r"-?[0-9]+", begin_page) and re.match(r"-?[0-9]+", end_page):
            begin_page = int(begin_page)
            end_page = int(end_page)

            if 0 < begin_page <= end_page:
                return True
            elif begin_page <= 0:
                return False
            elif begin_page > end_page:
                return False
            else:
                return False
        else:
            return False
    else:
        return False


def is_valid_path(path):
    if ' ' in path:
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setWindowTitle("Error")
        error_dialog.setText("Arquivo não pode conter espaço em branco no nome")
        error_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        error_dialog.exec_()
        return False
    else:
        if path is not None and path != "":
            return True
        else:
            return False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Splitter()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("splitter")
    MainWindow.show()
    sys.exit(app.exec_())

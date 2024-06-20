# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(944, 632)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(200, 275))
        self.widget.setMaximumSize(QtCore.QSize(200, 275))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(60, 70))
        self.label.setMaximumSize(QtCore.QSize(60, 70))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/icons/HKU (3).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 50))
        self.label_2.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.username_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.username_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.username_lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.username_lineEdit.setText("")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.horizontalLayout.addWidget(self.username_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, 10, 20, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.login_btn.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_4.addWidget(self.login_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.error_message = QtWidgets.QLabel(self.widget)
        self.error_message.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.error_message.setFont(font)
        self.error_message.setText("")
        self.error_message.setAlignment(QtCore.Qt.AlignCenter)
        self.error_message.setObjectName("error_message")
        self.verticalLayout.addWidget(self.error_message)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(249, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 174, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 174, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Log In"))
        self.username_lineEdit.setPlaceholderText(_translate("Form", "Enter Username.."))
        self.login_btn.setText(_translate("Form", "Face Login"))
import resource_rc
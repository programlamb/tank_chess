# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rules_des.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Rules(object):
    def setupUi(self, Rules):
        Rules.setObjectName("Rules")
        Rules.resize(660, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Rules.sizePolicy().hasHeightForWidth())
        Rules.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Rules)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.last = QtWidgets.QPushButton(self.widget)
        self.last.setObjectName("last")
        self.horizontalLayout.addWidget(self.last)
        self.next = QtWidgets.QPushButton(self.widget)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pb_close = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_close.sizePolicy().hasHeightForWidth())
        self.pb_close.setSizePolicy(sizePolicy)
        self.pb_close.setObjectName("pb_close")
        self.gridLayout_2.addWidget(self.pb_close, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        Rules.setCentralWidget(self.centralwidget)

        self.retranslateUi(Rules)
        QtCore.QMetaObject.connectSlotsByName(Rules)

    def retranslateUi(self, Rules):
        _translate = QtCore.QCoreApplication.translate
        Rules.setWindowTitle(_translate("Rules", "Rules"))
        self.last.setText(_translate("Rules", "<"))
        self.next.setText(_translate("Rules", ">"))
        self.pb_close.setText(_translate("Rules", "Close"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 121)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(291, 121))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pltWidgetframe = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pltWidgetframe.sizePolicy().hasHeightForWidth())
        self.pltWidgetframe.setSizePolicy(sizePolicy)
        self.pltWidgetframe.setMinimumSize(QtCore.QSize(291, 81))
        self.pltWidgetframe.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pltWidgetframe.setObjectName("pltWidgetframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.pltWidgetframe)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pltWidget = QtWidgets.QWidget(self.pltWidgetframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pltWidget.sizePolicy().hasHeightForWidth())
        self.pltWidget.setSizePolicy(sizePolicy)
        self.pltWidget.setMinimumSize(QtCore.QSize(190, 81))
        self.pltWidget.setObjectName("pltWidget")
        self.horizontalLayout.addWidget(self.pltWidget)
        self.widget = QtWidgets.QWidget(self.pltWidgetframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(120, 120))
        self.widget.setObjectName("widget")
        self.lbl_temp = QtWidgets.QLabel(self.widget)
        self.lbl_temp.setGeometry(QtCore.QRect(60, 0, 51, 16))
        self.lbl_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_temp.setObjectName("lbl_temp")
        self.lbl_count = QtWidgets.QLabel(self.widget)
        self.lbl_count.setGeometry(QtCore.QRect(10, 0, 51, 16))
        self.lbl_count.setObjectName("lbl_count")
        self.lbl_count_2 = QtWidgets.QLabel(self.widget)
        self.lbl_count_2.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.lbl_count_2.setObjectName("lbl_count_2")
        self.lbl_RH = QtWidgets.QLabel(self.widget)
        self.lbl_RH.setGeometry(QtCore.QRect(60, 20, 51, 16))
        self.lbl_RH.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_RH.setObjectName("lbl_RH")
        self.lbl_count_3 = QtWidgets.QLabel(self.widget)
        self.lbl_count_3.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.lbl_count_3.setObjectName("lbl_count_3")
        self.lbl_press = QtWidgets.QLabel(self.widget)
        self.lbl_press.setGeometry(QtCore.QRect(60, 40, 51, 16))
        self.lbl_press.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_press.setObjectName("lbl_press")
        self.lbl_count_4 = QtWidgets.QLabel(self.widget)
        self.lbl_count_4.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.lbl_count_4.setObjectName("lbl_count_4")
        self.lbl_alt = QtWidgets.QLabel(self.widget)
        self.lbl_alt.setGeometry(QtCore.QRect(60, 60, 51, 16))
        self.lbl_alt.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_alt.setObjectName("lbl_alt")
        self.lbl_count_5 = QtWidgets.QLabel(self.widget)
        self.lbl_count_5.setGeometry(QtCore.QRect(10, 80, 51, 16))
        self.lbl_count_5.setObjectName("lbl_count_5")
        self.lbl_lat = QtWidgets.QLabel(self.widget)
        self.lbl_lat.setGeometry(QtCore.QRect(60, 80, 51, 16))
        self.lbl_lat.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_lat.setObjectName("lbl_lat")
        self.lbl_count_6 = QtWidgets.QLabel(self.widget)
        self.lbl_count_6.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.lbl_count_6.setObjectName("lbl_count_6")
        self.lbl_long = QtWidgets.QLabel(self.widget)
        self.lbl_long.setGeometry(QtCore.QRect(60, 100, 51, 16))
        self.lbl_long.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_long.setObjectName("lbl_long")
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addWidget(self.pltWidgetframe)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_temp.setText(_translate("Form", "0"))
        self.lbl_count.setText(_translate("Form", "Temp(°C):"))
        self.lbl_count_2.setText(_translate("Form", "RH(%):"))
        self.lbl_RH.setText(_translate("Form", "0"))
        self.lbl_count_3.setText(_translate("Form", "Press(mB):"))
        self.lbl_press.setText(_translate("Form", "0"))
        self.lbl_count_4.setText(_translate("Form", "Alt(m):"))
        self.lbl_alt.setText(_translate("Form", "0"))
        self.lbl_count_5.setText(_translate("Form", "Lat(°):"))
        self.lbl_lat.setText(_translate("Form", "0"))
        self.lbl_count_6.setText(_translate("Form", "Long(°):"))
        self.lbl_long.setText(_translate("Form", "0"))


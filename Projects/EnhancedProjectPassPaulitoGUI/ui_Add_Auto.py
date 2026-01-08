# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_Auto.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(854, 371)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(854, 371))
        MainWindow.setMaximumSize(QSize(854, 371))
        icon = QIcon()
        icon.addFile(u":/IconImage/Icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-image: url(:/BackgroundImage/Background.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: transparent;\n"
"")
        self.label.setPixmap(QPixmap(u":/IconImage/Icon.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.verticalLayout.addWidget(self.label_7)

        self.Pass_Length = QSpinBox(self.centralwidget)
        self.Pass_Length.setObjectName(u"Pass_Length")

        self.verticalLayout.addWidget(self.Pass_Length)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 3, 2)

        self.Web_URL_Box_Add_Auto = QLineEdit(self.centralwidget)
        self.Web_URL_Box_Add_Auto.setObjectName(u"Web_URL_Box_Add_Auto")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.Web_URL_Box_Add_Auto.setFont(font3)
        self.Web_URL_Box_Add_Auto.setStyleSheet(u"color: black;\n"
"background: white;\n"
"caret-color: black;\n"
"selection-color: white;\n"
"selection-background-color: #0078d7;\n"
"")

        self.gridLayout.addWidget(self.Web_URL_Box_Add_Auto, 3, 2, 1, 2)

        self.Username_Box_Add_Auto = QLineEdit(self.centralwidget)
        self.Username_Box_Add_Auto.setObjectName(u"Username_Box_Add_Auto")
        self.Username_Box_Add_Auto.setFont(font3)
        self.Username_Box_Add_Auto.setStyleSheet(u"color: black;\n"
"background: white;\n"
"caret-color: black;\n"
"selection-color: white;\n"
"selection-background-color: #0078d7;\n"
"")

        self.gridLayout.addWidget(self.Username_Box_Add_Auto, 4, 2, 1, 2)

        self.Generated_Pass_Box = QLineEdit(self.centralwidget)
        self.Generated_Pass_Box.setObjectName(u"Generated_Pass_Box")
        self.Generated_Pass_Box.setFont(font3)
        self.Generated_Pass_Box.setStyleSheet(u"color: black;\n"
"background: white;\n"
"caret-color: black;\n"
"selection-color: white;\n"
"selection-background-color: #0078d7;\n"
"")

        self.gridLayout.addWidget(self.Generated_Pass_Box, 5, 2, 1, 2)

        self.Generate_Pass_Button = QPushButton(self.centralwidget)
        self.Generate_Pass_Button.setObjectName(u"Generate_Pass_Button")
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.Generate_Pass_Button.setFont(font4)
        self.Generate_Pass_Button.setStyleSheet(u"background: #16476A;\n"
"color: white;")

        self.gridLayout.addWidget(self.Generate_Pass_Button, 6, 0, 1, 3)

        self.Menu_Button_Add_Auto = QPushButton(self.centralwidget)
        self.Menu_Button_Add_Auto.setObjectName(u"Menu_Button_Add_Auto")
        self.Menu_Button_Add_Auto.setFont(font4)
        self.Menu_Button_Add_Auto.setStyleSheet(u"background: #16476A;\n"
"color: white;")

        self.gridLayout.addWidget(self.Menu_Button_Add_Auto, 6, 3, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 4)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pass Paulito Manager v1.0", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pass Paulito Manager", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"This program is a GSM CORPS property!            -Created by underpaid developer Paul", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Add Password Automatically:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter Website URL:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Enter Username:", None))
        self.Generate_Pass_Button.setText(QCoreApplication.translate("MainWindow", u"GENERATE PASSWORD WITH LENGTH INT", None))
        self.Menu_Button_Add_Auto.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"*GSM CORPS does not guarantee against data breaches! HeeheeHawhaw", None))
    # retranslateUi


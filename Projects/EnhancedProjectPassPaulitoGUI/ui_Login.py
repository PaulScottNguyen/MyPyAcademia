# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(851, 370)
        MainWindow.setMinimumSize(QSize(851, 370))
        MainWindow.setMaximumSize(QSize(851, 370))
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.Login_Button = QPushButton(self.centralwidget)
        self.Login_Button.setObjectName(u"Login_Button")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.Login_Button.setFont(font1)
        self.Login_Button.setStyleSheet(u"background: #16476A;\n"
"color: white;")

        self.gridLayout.addWidget(self.Login_Button, 5, 0, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")
        self.label_3.setScaledContents(False)

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: transparent;\n"
"")
        self.label.setPixmap(QPixmap(u":/IconImage/Icon.png"))
        self.label.setScaledContents(False)

        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)

        self.Master_Password = QLineEdit(self.centralwidget)
        self.Master_Password.setObjectName(u"Master_Password")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.Master_Password.setFont(font3)
        self.Master_Password.setStyleSheet(u"color: black;\n"
"background: white;\n"
"caret-color: black;\n"
"selection-color: white;\n"
"selection-background-color: #0078d7;\n"
"")

        self.gridLayout.addWidget(self.Master_Password, 3, 0, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")
        self.label_5.setWordWrap(True)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setStrikeOut(False)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)


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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pass Paulito Manager", None))
        self.Login_Button.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"This program is a GSM CORPS property!        -Created by underpaid developer Paul", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"*Note: Your master password key is needed to encrypt/decrypt your secured passwords. Do not lose it!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enter your master password key:", None))
    # retranslateUi


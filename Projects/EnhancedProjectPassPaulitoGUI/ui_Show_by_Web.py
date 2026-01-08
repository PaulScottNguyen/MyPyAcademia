# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Show_by_Web.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListView,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(851, 440)
        MainWindow.setMinimumSize(QSize(851, 440))
        MainWindow.setMaximumSize(QSize(851, 440))
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: transparent;\n"
"")
        self.label.setPixmap(QPixmap(u":/IconImage/Icon.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listViewWeb = QListView(self.centralwidget)
        self.listViewWeb.setObjectName(u"listViewWeb")
        self.listViewWeb.setStyleSheet(u"background: white;\n"
"border-color: rgb(0, 0, 0);\n"
"")

        self.verticalLayout.addWidget(self.listViewWeb)

        self.Menu_Web_Button = QPushButton(self.centralwidget)
        self.Menu_Web_Button.setObjectName(u"Menu_Web_Button")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.Menu_Web_Button.setFont(font)
        self.Menu_Web_Button.setStyleSheet(u"background: #16476A;\n"
"color: white;")

        self.verticalLayout.addWidget(self.Menu_Web_Button)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(48)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)


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
        self.Menu_Web_Button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"*GSM CORPS does not guarantee against data breaches! HeeheeHawhaw", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pass Paulito Manager", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Show By Websites:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"This program is a GSM CORPS property!           -Created by underpaid developer Paul", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
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

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

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

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Add_Pass_Manually_Button = QPushButton(self.centralwidget)
        self.Add_Pass_Manually_Button.setObjectName(u"Add_Pass_Manually_Button")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.Add_Pass_Manually_Button.setFont(font3)
        self.Add_Pass_Manually_Button.setStyleSheet(u"background: #16476A;\n"
"color: white;")

        self.verticalLayout.addWidget(self.Add_Pass_Manually_Button)

        self.Add_Pass_Auto_Button = QPushButton(self.centralwidget)
        self.Add_Pass_Auto_Button.setObjectName(u"Add_Pass_Auto_Button")
        self.Add_Pass_Auto_Button.setFont(font3)
        self.Add_Pass_Auto_Button.setStyleSheet(u"background: #16476A;\n"
"color: white;")

        self.verticalLayout.addWidget(self.Add_Pass_Auto_Button)

        self.Show_All_Button = QPushButton(self.centralwidget)
        self.Show_All_Button.setObjectName(u"Show_All_Button")
        self.Show_All_Button.setFont(font3)
        self.Show_All_Button.setStyleSheet(u"background: #16476A;\n"
"color: white;")

        self.verticalLayout.addWidget(self.Show_All_Button)

        self.Delete_Pass_Button = QPushButton(self.centralwidget)
        self.Delete_Pass_Button.setObjectName(u"Delete_Pass_Button")
        self.Delete_Pass_Button.setFont(font3)
        self.Delete_Pass_Button.setStyleSheet(u"background: #16476A;\n"
"color: white;")

        self.verticalLayout.addWidget(self.Delete_Pass_Button)

        self.Update_Pass_Button = QPushButton(self.centralwidget)
        self.Update_Pass_Button.setObjectName(u"Update_Pass_Button")
        self.Update_Pass_Button.setFont(font3)
        self.Update_Pass_Button.setStyleSheet(u"background: #16476A;\n"
"color: white;")

        self.verticalLayout.addWidget(self.Update_Pass_Button)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background: transparent;\n"
"color: #132440;\n"
"")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)


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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"This program is a GSM CORPS property!           -Created by underpaid developer Paul", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"OPTIONS:", None))
        self.Add_Pass_Manually_Button.setText(QCoreApplication.translate("MainWindow", u"Add Password Manually", None))
        self.Add_Pass_Auto_Button.setText(QCoreApplication.translate("MainWindow", u"Add Password Automatically", None))
        self.Show_All_Button.setText(QCoreApplication.translate("MainWindow", u"Show All Passwords", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"*GSM CORPS does not guarantee against data breaches! HeeheeHawhaw", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(598, 612)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_camera = QLabel(self.centralwidget)
        self.lbl_camera.setObjectName(u"lbl_camera")
        self.lbl_camera.setGeometry(QRect(20, 20, 561, 381))
        self.lbl_camera.setFrameShape(QFrame.Box)
        self.lbl_camera.setLineWidth(1)
        self.lbl_status = QLabel(self.centralwidget)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setGeometry(QRect(250, 420, 151, 31))
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(20, 420, 81, 41))
        self.sd_fps = QSlider(self.centralwidget)
        self.sd_fps.setObjectName(u"sd_fps")
        self.sd_fps.setGeometry(QRect(20, 480, 251, 31))
        self.sd_fps.setOrientation(Qt.Horizontal)
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(120, 420, 81, 41))
        self.sb_sensitivity = QSlider(self.centralwidget)
        self.sb_sensitivity.setObjectName(u"sb_sensitivity")
        self.sb_sensitivity.setGeometry(QRect(310, 480, 251, 31))
        self.sb_sensitivity.setOrientation(Qt.Horizontal)
        self.lbl_status_2 = QLabel(self.centralwidget)
        self.lbl_status_2.setObjectName(u"lbl_status_2")
        self.lbl_status_2.setGeometry(QRect(110, 520, 81, 31))
        self.lbl_status_3 = QLabel(self.centralwidget)
        self.lbl_status_3.setObjectName(u"lbl_status_3")
        self.lbl_status_3.setGeometry(QRect(390, 520, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 598, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_camera.setText("")
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"\uac10\ub3c4 500\uc73c\ub85c \uc870\uc815!", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\ucf1c\uae30", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"\ub044\uae30", None))
        self.lbl_status_2.setText(QCoreApplication.translate("MainWindow", u"FPS \uc870\uc808", None))
        self.lbl_status_3.setText(QCoreApplication.translate("MainWindow", u"\uac10\ub3c4 \uc870\uc808", None))
    # retranslateUi


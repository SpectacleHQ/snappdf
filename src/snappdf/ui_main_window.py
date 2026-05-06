# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 700)
        MainWindow.setMinimumSize(QSize(540, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(16)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 20, 24, 24)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setSpacing(12)
        self.headerLayout.setObjectName(u"headerLayout")
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(40, 40))
        self.logoLabel.setMaximumSize(QSize(40, 40))
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.headerLayout.addWidget(self.logoLabel)

        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(2)
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"font-size: 20px; font-weight: 700; color: #F8FAFC;")

        self.titleLayout.addWidget(self.titleLabel)

        self.subtitleLabel = QLabel(self.centralwidget)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        self.subtitleLabel.setStyleSheet(u"font-size: 12px; color: #94A3B8;")

        self.titleLayout.addWidget(self.subtitleLabel)


        self.headerLayout.addLayout(self.titleLayout)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)


        self.mainLayout.addLayout(self.headerLayout)

        self.dropZoneFrame = QFrame(self.centralwidget)
        self.dropZoneFrame.setObjectName(u"dropZoneFrame")
        self.dropZoneFrame.setMinimumSize(QSize(0, 140))
        self.dropZoneFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dropZoneLayout = QVBoxLayout(self.dropZoneFrame)
        self.dropZoneLayout.setSpacing(8)
        self.dropZoneLayout.setObjectName(u"dropZoneLayout")
        self.dropZoneLayout.setContentsMargins(-1, 24, -1, 24)
        self.dropIconLabel = QLabel(self.dropZoneFrame)
        self.dropIconLabel.setObjectName(u"dropIconLabel")
        self.dropIconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dropIconLabel.setStyleSheet(u"font-size: 36px;")

        self.dropZoneLayout.addWidget(self.dropIconLabel)

        self.dropTextLabel = QLabel(self.dropZoneFrame)
        self.dropTextLabel.setObjectName(u"dropTextLabel")
        self.dropTextLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dropTextLabel.setStyleSheet(u"font-size: 14px; color: #94A3B8;")

        self.dropZoneLayout.addWidget(self.dropTextLabel)

        self.fileNameLabel = QLabel(self.dropZoneFrame)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fileNameLabel.setStyleSheet(u"font-size: 13px; color: #EA580C; font-weight: 600;")

        self.dropZoneLayout.addWidget(self.fileNameLabel)


        self.mainLayout.addWidget(self.dropZoneFrame)

        self.settingsFrame = QFrame(self.centralwidget)
        self.settingsFrame.setObjectName(u"settingsFrame")
        self.settingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsLayout = QVBoxLayout(self.settingsFrame)
        self.settingsLayout.setSpacing(16)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.settingsTitleLabel = QLabel(self.settingsFrame)
        self.settingsTitleLabel.setObjectName(u"settingsTitleLabel")
        self.settingsTitleLabel.setStyleSheet(u"font-size: 14px; font-weight: 600; color: #F8FAFC;")

        self.settingsLayout.addWidget(self.settingsTitleLabel)

        self.formatLayout = QHBoxLayout()
        self.formatLayout.setSpacing(12)
        self.formatLayout.setObjectName(u"formatLayout")
        self.formatLabel = QLabel(self.settingsFrame)
        self.formatLabel.setObjectName(u"formatLabel")
        self.formatLabel.setMinimumSize(QSize(70, 0))
        self.formatLabel.setStyleSheet(u"font-size: 13px; color: #94A3B8;")

        self.formatLayout.addWidget(self.formatLabel)

        self.formatComboBox = QComboBox(self.settingsFrame)
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.setObjectName(u"formatComboBox")
        self.formatComboBox.setMinimumSize(QSize(0, 36))

        self.formatLayout.addWidget(self.formatComboBox)


        self.settingsLayout.addLayout(self.formatLayout)

        self.qualityLayout = QHBoxLayout()
        self.qualityLayout.setSpacing(12)
        self.qualityLayout.setObjectName(u"qualityLayout")
        self.qualityLabel = QLabel(self.settingsFrame)
        self.qualityLabel.setObjectName(u"qualityLabel")
        self.qualityLabel.setMinimumSize(QSize(70, 0))
        self.qualityLabel.setStyleSheet(u"font-size: 13px; color: #94A3B8;")

        self.qualityLayout.addWidget(self.qualityLabel)

        self.qualitySlider = QSlider(self.settingsFrame)
        self.qualitySlider.setObjectName(u"qualitySlider")
        self.qualitySlider.setMinimum(1)
        self.qualitySlider.setMaximum(100)
        self.qualitySlider.setValue(90)
        self.qualitySlider.setOrientation(Qt.Orientation.Horizontal)

        self.qualityLayout.addWidget(self.qualitySlider)

        self.qualityValueLabel = QLabel(self.settingsFrame)
        self.qualityValueLabel.setObjectName(u"qualityValueLabel")
        self.qualityValueLabel.setMinimumSize(QSize(36, 0))
        self.qualityValueLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)
        self.qualityValueLabel.setStyleSheet(u"font-size: 13px; color: #F8FAFC; font-weight: 500;")

        self.qualityLayout.addWidget(self.qualityValueLabel)


        self.settingsLayout.addLayout(self.qualityLayout)

        self.dpiLayout = QHBoxLayout()
        self.dpiLayout.setSpacing(12)
        self.dpiLayout.setObjectName(u"dpiLayout")
        self.dpiLabel = QLabel(self.settingsFrame)
        self.dpiLabel.setObjectName(u"dpiLabel")
        self.dpiLabel.setMinimumSize(QSize(70, 0))
        self.dpiLabel.setStyleSheet(u"font-size: 13px; color: #94A3B8;")

        self.dpiLayout.addWidget(self.dpiLabel)

        self.dpiComboBox = QComboBox(self.settingsFrame)
        self.dpiComboBox.addItem("")
        self.dpiComboBox.addItem("")
        self.dpiComboBox.addItem("")
        self.dpiComboBox.addItem("")
        self.dpiComboBox.addItem("")
        self.dpiComboBox.setObjectName(u"dpiComboBox")
        self.dpiComboBox.setMinimumSize(QSize(0, 36))

        self.dpiLayout.addWidget(self.dpiComboBox)


        self.settingsLayout.addLayout(self.dpiLayout)

        self.pageRangeLayout = QHBoxLayout()
        self.pageRangeLayout.setSpacing(12)
        self.pageRangeLayout.setObjectName(u"pageRangeLayout")
        self.pageRangeLabel = QLabel(self.settingsFrame)
        self.pageRangeLabel.setObjectName(u"pageRangeLabel")
        self.pageRangeLabel.setMinimumSize(QSize(70, 0))
        self.pageRangeLabel.setStyleSheet(u"font-size: 13px; color: #94A3B8;")

        self.pageRangeLayout.addWidget(self.pageRangeLabel)

        self.pageRangeEdit = QLineEdit(self.settingsFrame)
        self.pageRangeEdit.setObjectName(u"pageRangeEdit")
        self.pageRangeEdit.setMinimumSize(QSize(0, 36))

        self.pageRangeLayout.addWidget(self.pageRangeEdit)


        self.settingsLayout.addLayout(self.pageRangeLayout)

        self.outputDirLayout = QHBoxLayout()
        self.outputDirLayout.setSpacing(12)
        self.outputDirLayout.setObjectName(u"outputDirLayout")
        self.outputDirLabel = QLabel(self.settingsFrame)
        self.outputDirLabel.setObjectName(u"outputDirLabel")
        self.outputDirLabel.setMinimumSize(QSize(70, 0))
        self.outputDirLabel.setStyleSheet(u"font-size: 13px; color: #94A3B8;")

        self.outputDirLayout.addWidget(self.outputDirLabel)

        self.outputDirEdit = QLineEdit(self.settingsFrame)
        self.outputDirEdit.setObjectName(u"outputDirEdit")
        self.outputDirEdit.setMinimumSize(QSize(0, 36))
        self.outputDirEdit.setReadOnly(True)

        self.outputDirLayout.addWidget(self.outputDirEdit)

        self.browseOutputBtn = QPushButton(self.settingsFrame)
        self.browseOutputBtn.setObjectName(u"browseOutputBtn")
        self.browseOutputBtn.setMinimumSize(QSize(60, 36))

        self.outputDirLayout.addWidget(self.browseOutputBtn)


        self.settingsLayout.addLayout(self.outputDirLayout)


        self.mainLayout.addWidget(self.settingsFrame)

        self.progressFrame = QFrame(self.centralwidget)
        self.progressFrame.setObjectName(u"progressFrame")
        self.progressFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.progressLayout = QVBoxLayout(self.progressFrame)
        self.progressLayout.setSpacing(8)
        self.progressLayout.setObjectName(u"progressLayout")
        self.progressInfoLayout = QHBoxLayout()
        self.progressInfoLayout.setObjectName(u"progressInfoLayout")
        self.progressLabel = QLabel(self.progressFrame)
        self.progressLabel.setObjectName(u"progressLabel")
        self.progressLabel.setStyleSheet(u"font-size: 13px; color: #94A3B8;")

        self.progressInfoLayout.addWidget(self.progressLabel)

        self.progressInfoSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.progressInfoLayout.addItem(self.progressInfoSpacer)

        self.progressPercentLabel = QLabel(self.progressFrame)
        self.progressPercentLabel.setObjectName(u"progressPercentLabel")
        self.progressPercentLabel.setStyleSheet(u"font-size: 13px; color: #F8FAFC; font-weight: 500;")

        self.progressInfoLayout.addWidget(self.progressPercentLabel)


        self.progressLayout.addLayout(self.progressInfoLayout)

        self.progressBar = QProgressBar(self.progressFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 8))
        self.progressBar.setMaximumSize(QSize(16777215, 8))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.progressLayout.addWidget(self.progressBar)


        self.mainLayout.addWidget(self.progressFrame)

        self.convertBtn = QPushButton(self.centralwidget)
        self.convertBtn.setObjectName(u"convertBtn")
        self.convertBtn.setMinimumSize(QSize(0, 48))
        self.convertBtn.setEnabled(False)

        self.mainLayout.addWidget(self.convertBtn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SnapPDF", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c4", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"SnapPDF", None))
        self.subtitleLabel.setText(QCoreApplication.translate("MainWindow", u"PDF \u9875\u9762\u5bfc\u51fa\u4e3a\u56fe\u7247", None))
        self.dropZoneFrame.setObjectName(QCoreApplication.translate("MainWindow", u"dropZoneFrame", None))
        self.dropIconLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c1", None))
        self.dropTextLabel.setText(QCoreApplication.translate("MainWindow", u"\u62d6\u62fd PDF \u6587\u4ef6\u5230\u6b64\u5904\uff0c\u6216\u70b9\u51fb\u6d4f\u89c8", None))
        self.fileNameLabel.setText("")
        self.settingsFrame.setObjectName(QCoreApplication.translate("MainWindow", u"settingsFrame", None))
        self.settingsTitleLabel.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8bbe\u7f6e", None))
        self.formatLabel.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u683c\u5f0f", None))
        self.formatComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"PNG", None))
        self.formatComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"JPG", None))
        self.formatComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"WEBP", None))
        self.formatComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"BMP", None))

        self.qualityLabel.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u8d28\u91cf", None))
        self.qualityValueLabel.setText(QCoreApplication.translate("MainWindow", u"90%", None))
        self.dpiLabel.setText(QCoreApplication.translate("MainWindow", u"DPI", None))
        self.dpiComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"72", None))
        self.dpiComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"150", None))
        self.dpiComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"200", None))
        self.dpiComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"300", None))
        self.dpiComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"600", None))

        self.pageRangeLabel.setText(QCoreApplication.translate("MainWindow", u"\u9875\u9762\u8303\u56f4", None))
        self.pageRangeEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u9875\u9762\uff08\u5982: 1-3, 5, 7-9\uff09", None))
        self.outputDirLabel.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55", None))
        self.outputDirEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4e0e PDF \u6587\u4ef6\u76f8\u540c\u76ee\u5f55", None))
        self.browseOutputBtn.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.progressFrame.setObjectName(QCoreApplication.translate("MainWindow", u"progressFrame", None))
        self.progressLabel.setText(QCoreApplication.translate("MainWindow", u"\u51c6\u5907\u5c31\u7eea", None))
        self.progressPercentLabel.setText("")
        self.convertBtn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
    # retranslateUi


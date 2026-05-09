# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(482, 354)
        self.verticalLayout_6 = QVBoxLayout(Widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.textBrowser)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"        border: 1px solid grey; /* \u6574\u4e2a\u8fdb\u5ea6\u6761\u7684\u5916\u8fb9\u6846 */\n"
"        border-radius: 3px;     /* \u5706\u89d2 */\n"
"        text-align: center;     /* \u6587\u5b57\u5c45\u4e2d */\n"
"        background-color: #333; /* \u80cc\u666f\u989c\u8272\uff08\u672a\u5b8c\u6210\u90e8\u5206\uff09 */\n"
"    }\n"
"\n"
"    QProgressBar::chunk {\n"
"        background-color: #008000; /* \u8fdb\u5ea6\u6761\u989c\u8272\uff08\u5df2\u5b8c\u6210\u90e8\u5206\uff09 */\n"
"        border: none;              /* \u5173\u952e\uff1a\u53bb\u6389\u5185\u90e8\u8fb9\u6846 */\n"
"        /* \u6216\u8005\u4f60\u53ef\u4ee5\u7ed9\u5b83\u52a0\u4e00\u70b9\u5706\u89d2\uff0c\u8ba9\u5b83\u66f4\u597d\u770b */\n"
"        border-radius: 3px;\n"
"    }\n"
"")
        self.progressBar.setValue(30)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_5.addWidget(self.progressBar)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 25))
        self.label_2.setMaximumSize(QSize(80, 25))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.label_2.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_lineEdit = QLineEdit(Widget)
        self.input_lineEdit.setObjectName(u"input_lineEdit")
        self.input_lineEdit.setMinimumSize(QSize(230, 30))
        self.input_lineEdit.setMaximumSize(QSize(230, 30))
        self.input_lineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.input_lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.run_pushButton = QPushButton(Widget)
        self.run_pushButton.setObjectName(u"run_pushButton")
        self.run_pushButton.setMaximumSize(QSize(70, 30))
        self.run_pushButton.setBaseSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.run_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 25))
        self.label_4.setMaximumSize(QSize(100, 25))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.in_file_lineEdit1 = QLineEdit(Widget)
        self.in_file_lineEdit1.setObjectName(u"in_file_lineEdit1")
        self.in_file_lineEdit1.setMinimumSize(QSize(230, 30))
        self.in_file_lineEdit1.setMaximumSize(QSize(230, 30))

        self.horizontalLayout_4.addWidget(self.in_file_lineEdit1)

        self.in_open_toolButton1 = QToolButton(Widget)
        self.in_open_toolButton1.setObjectName(u"in_open_toolButton1")
        self.in_open_toolButton1.setMinimumSize(QSize(30, 30))
        self.in_open_toolButton1.setMaximumSize(QSize(30, 30))
        self.in_open_toolButton1.setBaseSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.in_open_toolButton1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 25))
        self.label_5.setMaximumSize(QSize(100, 25))
        self.label_5.setFont(font)
        self.label_5.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.in_file_lineEdit2 = QLineEdit(Widget)
        self.in_file_lineEdit2.setObjectName(u"in_file_lineEdit2")
        self.in_file_lineEdit2.setMinimumSize(QSize(230, 30))
        self.in_file_lineEdit2.setMaximumSize(QSize(230, 30))

        self.horizontalLayout_9.addWidget(self.in_file_lineEdit2)

        self.in_open_toolButton2 = QToolButton(Widget)
        self.in_open_toolButton2.setObjectName(u"in_open_toolButton2")
        self.in_open_toolButton2.setMinimumSize(QSize(30, 30))
        self.in_open_toolButton2.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.in_open_toolButton2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 25))
        self.label_3.setMaximumSize(QSize(80, 25))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.out_file_lineEdit = QLineEdit(Widget)
        self.out_file_lineEdit.setObjectName(u"out_file_lineEdit")
        self.out_file_lineEdit.setMinimumSize(QSize(230, 30))
        self.out_file_lineEdit.setMaximumSize(QSize(230, 30))

        self.horizontalLayout_3.addWidget(self.out_file_lineEdit)

        self.out_open_toolButton = QToolButton(Widget)
        self.out_open_toolButton.setObjectName(u"out_open_toolButton")
        self.out_open_toolButton.setMinimumSize(QSize(30, 30))
        self.out_open_toolButton.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.out_open_toolButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u81ea\u7136\u8bed\u8a00\u526a\u8f91\u89c6\u9891\u5c0f\u5de5\u5177", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#121314;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#a5d6ff;\">1.\u89c6\u9891\u683c\u5f0f\u8f6c\u6362</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#121314;\"><span style=\" font-family:'Conso"
                        "las','Courier New','monospace'; font-size:14px; color:#a5d6ff;\">2.\u88c1\u526a\u89c6\u9891</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#121314;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#a5d6ff;\">3.\u63d0\u53d6\u97f3\u9891</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#121314;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#a5d6ff;\">4.\u8c03\u6574\u5206\u8fa8\u7387</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#121314;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#a5d6ff;\">5.\u964d\u4f4e\u89c6\u9891\u7801\u7387<"
                        "/span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#121314;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#a5d6ff;\">6.\u5408\u5e76\u4e24\u4e2a\u89c6\u9891</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#121314;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#a5d6ff;\">7.\u63d0\u53d6\u5355\u5e27\u56fe\u50cf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#121314;\"><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:14px; color:#a5d6ff;\">8.\u53bb\u9664\u97f3\u9891</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u9700\u6c42\u8f93\u5165\uff1a", None))
        self.input_lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"\u793a\u4f8b:\u5e2e\u6211\u628a\u89c6\u9891\u7684\u97f3\u9891\u63d0\u53d6\u51fa\u6765", None))
        self.run_pushButton.setText(QCoreApplication.translate("Widget", u"\u8fd0\u884c", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u8f93\u5165\u89c6\u9891\u6587\u4ef61", None))
        self.in_open_toolButton1.setText(QCoreApplication.translate("Widget", u"...", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u8f93\u5165\u89c6\u9891\u6587\u4ef62", None))
        self.in_file_lineEdit2.setText(QCoreApplication.translate("Widget", u"\u9700\u4f7f\u7528\u5408\u5e76\u529f\u80fd\u65f6\u518d\u4fee\u6539", None))
        self.in_open_toolButton2.setText(QCoreApplication.translate("Widget", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u8f93\u51fa\u6587\u4ef6\u5939\u00b7", None))
        self.out_open_toolButton.setText(QCoreApplication.translate("Widget", u"...", None))
    # retranslateUi


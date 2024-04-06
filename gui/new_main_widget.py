from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class MainWidget:
    def setupUi(self, main_window:QtWidgets.QMainWindow):
        main_window.setObjectName("main_window")

        # email example text output
        self.email_example = QtWidgets.QTextBrowser(main_window)
        self.email_example.setEnabled(True)
        self.email_example.setGeometry(QtCore.QRect(12, 32, 301, 371))
        self.email_example.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.email_example.setObjectName("email_example")
        
        # progress bar
        self.progress_bar = QtWidgets.QProgressBar(main_window)
        self.progress_bar.setGeometry(QtCore.QRect(20, 430, 251, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")

        # log text output
        self.log_outputs = QtWidgets.QTextBrowser(main_window)
        self.log_outputs.setGeometry(QtCore.QRect(340, 311, 271, 141))
        self.log_outputs.setObjectName("log_outputs")

        # email site select dropdown
        self.email_site_select = QtWidgets.QComboBox(main_window)
        self.email_site_select.setGeometry(QtCore.QRect(340, 30, 171, 26))
        self.email_site_select.setObjectName("email_site_select")
        self.email_site_select.addItem("")
        self.email_site_select.addItem("")
        self.email_site_select.addItem("")

        # help button
        self.help_button = QtWidgets.QPushButton(main_window)
        self.help_button.setGeometry(QtCore.QRect(550, 20, 41, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_button.sizePolicy().hasHeightForWidth())
        self.help_button.setSizePolicy(sizePolicy)
        self.help_button.setCheckable(False)
        self.help_button.setAutoDefault(False)
        self.help_button.setDefault(False)
        self.help_button.setFlat(False)
        self.help_button.setObjectName("help_button")

        # email input text and label
        self.email_label = QtWidgets.QLabel(main_window)
        self.email_label.setGeometry(QtCore.QRect(350, 90, 41, 16))
        self.email_label.setObjectName("email_label")
        self.email_address_input = QtWidgets.QLineEdit(main_window)
        self.email_address_input.setGeometry(QtCore.QRect(420, 80, 181, 31))
        self.email_address_input.setDragEnabled(True)
        self.email_address_input.setObjectName("email_address_input")

        # password input text and label
        self.password_label = QtWidgets.QLabel(main_window)
        self.password_label.setGeometry(QtCore.QRect(340, 130, 61, 16))
        self.password_label.setObjectName("password_label")
        self.password_input = QtWidgets.QLineEdit(main_window)
        self.password_input.setGeometry(QtCore.QRect(420, 120, 181, 31))
        self.password_input.setInputMask("")
        self.password_input.setText("")
        self.password_input.setDragEnabled(True)
        self.password_input.setObjectName("password_input")

        # load template button
        self.load_template_button = QtWidgets.QPushButton(main_window)
        self.load_template_button.setGeometry(QtCore.QRect(340, 190, 141, 41))
        self.load_template_button.setObjectName("load_template_button")

        # load candidates button
        self.load_candidates_button = QtWidgets.QPushButton(main_window)
        self.load_candidates_button.setGeometry(QtCore.QRect(480, 190, 141, 41))
        self.load_candidates_button.setObjectName("load_candidates_button")

        # send email button
        self.send_email_button = QtWidgets.QPushButton(main_window)
        self.send_email_button.setGeometry(QtCore.QRect(410, 250, 141, 41))
        self.send_email_button.setObjectName("send_email_button")

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Auto Email Sender"))
        self.email_site_select.setItemText(0, _translate("main_window", "Naver (@naver.com)"))
        self.email_site_select.setItemText(1, _translate("main_window", "Google (@google.com)"))
        self.email_site_select.setItemText(2, _translate("main_window", "Daum (@daum.net)"))
        self.help_button.setText(_translate("main_window", "?"))
        self.email_label.setText(_translate("main_window", "EMAIL"))
        self.password_label.setText(_translate("main_window", "Password"))
        self.load_template_button.setText(_translate("main_window", "Load Template"))
        self.load_candidates_button.setText(_translate("main_window", "Load Candidates"))
        self.send_email_button.setText(_translate("main_window", "Send Email"))
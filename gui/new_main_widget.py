from PyQt5 import QtCore, QtWidgets


class MainWidget:
    def setupUi(self, main_window: QtWidgets.QMainWindow) -> None:
        main_window.setObjectName("main_window")

        # email example text output
        self.email_example = QtWidgets.QTextBrowser(main_window)
        self.email_example.setEnabled(True)
        self.email_example.setGeometry(QtCore.QRect(12, 32, 301, 371))
        self.email_example.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored
        )
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
        self.email_site_select.addItem("Naver (@naver.com)")
        self.email_site_select.addItem("Google (@google.com)")
        self.email_site_select.addItem("Daum (@daum.net)")

        # help button
        self.help_button = QtWidgets.QPushButton(main_window)
        self.help_button.setGeometry(QtCore.QRect(550, 20, 41, 32))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_button.sizePolicy().hasHeightForWidth())
        self.help_button.setSizePolicy(sizePolicy)
        self.help_button.setCheckable(False)
        self.help_button.setAutoDefault(False)
        self.help_button.setDefault(False)
        self.help_button.setFlat(False)
        self.help_button.setObjectName("help_button")
        self.help_button.setText("?")
        self.help_button.clicked.connect(self.help_button_clicked)

        # email input text and label
        self.email_label = QtWidgets.QLabel(main_window)
        self.email_label.setGeometry(QtCore.QRect(350, 90, 41, 16))
        self.email_label.setObjectName("email_label")
        self.email_label.setText("EMAIL")
        self.email_address_input = QtWidgets.QLineEdit(main_window)
        self.email_address_input.setGeometry(QtCore.QRect(420, 80, 181, 31))
        self.email_address_input.setDragEnabled(True)
        self.email_address_input.setObjectName("email_address_input")

        # password input text and label
        self.password_label = QtWidgets.QLabel(main_window)
        self.password_label.setGeometry(QtCore.QRect(325, 130, 76, 16))
        self.password_label.setObjectName("password_label")
        self.password_label.setText("PASSWORD")
        self.password_input = QtWidgets.QLineEdit(main_window)
        self.password_input.setGeometry(QtCore.QRect(420, 120, 181, 31))
        self.password_input.setInputMask("")
        self.password_input.setText("")
        self.password_input.setDragEnabled(True)
        self.password_input.setObjectName("password_input")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # load template button
        self.load_template_button = QtWidgets.QPushButton(main_window)
        self.load_template_button.setGeometry(QtCore.QRect(340, 190, 141, 41))
        self.load_template_button.setObjectName("load_template_button")
        self.load_template_button.setText("Load Template")
        self.load_template_button.clicked.connect(self.load_templates_button_clicked)

        # load candidates button
        self.load_candidates_button = QtWidgets.QPushButton(main_window)
        self.load_candidates_button.setGeometry(QtCore.QRect(480, 190, 141, 41))
        self.load_candidates_button.setObjectName("load_candidates_button")
        self.load_candidates_button.setText("Load Candidates")
        self.load_candidates_button.clicked.connect(self.load_candidates_button_clicked)
        
        # send email button
        self.send_email_button = QtWidgets.QPushButton(main_window)
        self.send_email_button.setGeometry(QtCore.QRect(410, 250, 141, 41))
        self.send_email_button.setObjectName("send_email_button")
        self.send_email_button.setText("Send Email")
        self.send_email_button.clicked.connect(self.send_email_button_clicked)

        QtCore.QMetaObject.connectSlotsByName(main_window)

    @staticmethod
    def help_button_clicked() -> None:
        """
        Help Button Click Event
        """
        QtWidgets.QMessageBox.about(
            None,
            "test",
            """<사용법>
1. 보내고자 하는 이메일 사이트를 선택한다. (Naver, Daum, Google)
2. 해당 사이트의 계정(이메일 주소 포함)과 비밀번호를 입력한다.
3. Load Templates로 이메일 템플릿을 불러온다. (대체하고자 하는 값을 ${} 로 감싼다)
4. Load Candidates로 이메일 후보 및 대체 값들을 채운 CSV, EXCEL 파일을 불러온다.
5. 이메일 예시를 확인 한 후 Send Email 클릭한다.
""",
        )

    def load_templates_button_clicked(self) -> None:
        """
        Load Templates Button Clicked
        """
        self.email_example.append("load_templates_button_clicked")

    def load_candidates_button_clicked(self) -> None:
        """
        Load Candidates Button Clicked
        """
        self.email_example.append("load_candidates_button_clicked")

    def send_email_button_clicked(self) -> None:
        """
        Send Email Button Clicked
        """
        self.log_outputs.append("send_email_button_clicked")
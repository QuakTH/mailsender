import os
from typing import Optional
from PyQt5 import QtCore, QtWidgets

from email_process.email_send_process import EmailSendProcess
from file_process.candiate_process import CandidateProcess
from file_process.template_process import TemplateProcess
from utils import run_log_exception


class MainWidget:
    def __init__(self) -> None:
        self.template_process = TemplateProcess(self)
        self.candidate_process = CandidateProcess(self)
        # self.progress_bar_thread = ProgressBarThread()

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
        self.progress_bar.setValue(0)
        self.progress_bar.setObjectName("progress_bar")
        # self.progress_bar_thread.progress.connect(self.progress_bar.setValue)

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
        self.load_template_button.clicked.connect(
            lambda: self.load_templates_button_clicked()
        )

        # load candidates button
        self.load_candidates_button = QtWidgets.QPushButton(main_window)
        self.load_candidates_button.setGeometry(QtCore.QRect(480, 190, 141, 41))
        self.load_candidates_button.setObjectName("load_candidates_button")
        self.load_candidates_button.setText("Load Candidates")
        self.load_candidates_button.clicked.connect(
            lambda: self.load_candidates_button_clicked()
        )

        # send email button
        self.send_email_button = QtWidgets.QPushButton(main_window)
        self.send_email_button.setGeometry(QtCore.QRect(410, 250, 141, 41))
        self.send_email_button.setObjectName("send_email_button")
        self.send_email_button.setText("Send Email")
        self.send_email_button.clicked.connect(lambda: self.send_email_button_clicked())

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
4. Load Candidates로 이메일 후보 및 대체 값들을 채운 CSV, EXCEL 파일을 불러온다.(email 정보는 필수!)
5. 이메일 예시를 확인 한 후 Send Email 클릭한다.
""",
        )

    @run_log_exception("log_outputs")
    def load_templates_button_clicked(self) -> None:
        """
        Load Templates Button Clicked
        """
        file_path = self.get_file_path("이메일 내용 파일 선택", "TEXT(*.txt);;")
        if not file_path:
            return

        self.template_process.set_file_path(file_path)
        self.template_process.extract_place_holders()
        self.template_process.set_email_example()
        self.log_outputs.append(f"Load Template file : {os.path.basename(file_path)}")

    @run_log_exception("log_outputs")
    def load_candidates_button_clicked(self) -> None:
        """
        Load Candidates Button Clicked
        """
        if not self.template_process.file_path_set:
            self.log_outputs.append('Load the template files first.')
            return

        file_path = self.get_file_path(
            "이메일 목록 파일 선택", "EXCEL,CSV(*.xlsx *.csv)"
        )
        if not file_path:
            return

        self.candidate_process.set_file_path(file_path)
        self.candidate_process.load_dataframe()
        self.log_outputs.append(f"Load Candidate file : {os.path.basename(file_path)}")

        self.template_process.set_email_example()

    @run_log_exception("log_outputs")
    def send_email_button_clicked(self) -> None:
        """
        Send Email Button Clicked
        """
        email_type = self.email_site_select.currentText()
        email = self.email_address_input.text()
        password = self.password_input.text()

        EmailSendProcess.send_email(email_type, email, password, self.template_process.template,
                                    self.candidate_process.candidate_df, self.progress_bar)

        self.log_outputs.append("Email send completed.")

    @staticmethod
    def get_file_path(action_name, filter) -> Optional[str | os.PathLike]:
        """
        Open file dialog and get file path from dialog.

        action_name : File dialog title.
        filter : File extension filter.
        :return: File path of the file. if file is selected.
        """
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            caption=action_name, filter=filter
        )

        if fname:
            return fname
        return None

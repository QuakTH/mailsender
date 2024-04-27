from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from gui.layouts.base_layout import BaseLayout


class MailSenderSelectLayout(BaseLayout):
    def set_layout(self) -> None:
        mail_select_label = QLabel('메일 사이트 선택 :')
        mail_select_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        mail_select_label.setFont(QFont('굴림', 13, 90))

        radio_group = QButtonGroup()

        naver_radio_btn = QRadioButton('네이버')
        naver_radio_btn.setFont(QFont('굴림', 13))
        radio_group.addButton(naver_radio_btn)

        google_radio_btn = QRadioButton('구글')
        google_radio_btn.setFont(QFont('굴림', 13))
        radio_group.addButton(google_radio_btn)

        daum_radio_btn = QRadioButton('다음')
        daum_radio_btn.setFont(QFont('굴림', 13))
        radio_group.addButton(daum_radio_btn)

        self.addStretch(1)
        self.addWidget(mail_select_label)
        self.addStretch(1)
        self.addWidget(naver_radio_btn)
        self.addWidget(google_radio_btn)
        self.addWidget(daum_radio_btn)
        self.addStretch(1)
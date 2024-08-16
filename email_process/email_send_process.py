import json
import random
import smtplib
import time
from email.mime.text import MIMEText

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from exceptions import CustomException
from file_process.candiate_process import CandidateProcess


class EmailSendProcess:
    @staticmethod
    def get_smtp(email_type: str, email: str, password: str) -> smtplib.SMTP:
        """Create an SMTP object.

        :param email_type: Which email type to use.
        :param email: ID.
        :param password: Password.
        :return: SMTP object.
        """
        if email_type.startswith('Naver'):
            mail_type = 'smtp.naver.com'
            port = 587
        elif email_type.startswith('Google'):
            mail_type = 'smtp.gmail.com'
            port = 587
        else:
            raise CustomException(f'Email type `{email_type}` is not supported')

        smtp = smtplib.SMTP(mail_type, port)

        smtp.ehlo()
        smtp.starttls()
        try:
            smtp.login(email, password)
        except smtplib.SMTPAuthenticationError:
            smtp.quit()
            raise CustomException('Check ID or Password.')

        return smtp

    @staticmethod
    def send_email(email_type: str, email: str, password: str, template: str, candidate_df: pd.DataFrame,
                   progress_bar: QtWidgets.QProgressBar):
        """Sends an email to the candidate listed in the candidate_df one by one.
        Using the template. And update the progress bar respectively to the candidate that has been sent.

        :param email_type: Which email type to use.
        :param email: ID.
        :param password: Password.
        :param template: Email body template.
        :param candidate_df: Candidate dataframe.
        :param progress_bar: Progress bar.
        """
        smtp = None
        sender = email + email_type.split()[1].replace('(', '').replace(')', '')
        try:
            smtp = EmailSendProcess.get_smtp(email_type, email, password)

            total_candidates = len(candidate_df)
            count = 1
            for _, candidate in candidate_df.iterrows():
                text = template
                candidate_info = json.loads(candidate.to_json(force_ascii=False))
                for key, value in candidate_info.items():
                    if key not in CandidateProcess.MANDATORY_KEYS:
                        text = text.replace(f'${{{{{key}}}}}', value)

                msg = MIMEText(text)
                msg['Subject'] = candidate_info['title']
                msg['From'] = sender
                msg['To'] = candidate_info['email']

                smtp.sendmail(sender, candidate_info['email'], msg.as_string())

                progress_bar.setProperty('value', count / total_candidates * 100)
                QApplication.processEvents()

                count += 1
                time.sleep(0.5)
        finally:
            if smtp:
                smtp.quit()

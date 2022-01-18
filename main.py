# from gui import GUI
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication
import sys


def main():
    '''
    main 함수
    '''
    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

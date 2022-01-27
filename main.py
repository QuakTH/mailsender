# from gui import GUI
from main_window import MainWidget, MainWindow
from PyQt5.QtWidgets import QApplication
import sys


def main():
    '''
    main 함수
    '''
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

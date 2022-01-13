from gui import GUI


def main():
    '''
    main 함수
    '''
    gui = GUI('메일 자동 처리 프로그램')
    gui.set_size('600x450')
    gui.fill_assets()
    gui.show()


if __name__ == '__main__':
    main()

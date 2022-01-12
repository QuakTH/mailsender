from tkinter import Tk, filedialog, Menu


def main():
    '''
    main 함수
    '''
    main_window = Tk()

    main_window.title('메일 자동화 프로그램')
    main_window.geometry('500x400')

    menubar = Menu(main_window)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label='열기')
    menubar.add_cascade(label='파일', menu=menu1)

    main_window.config(menu=menubar)
    main_window.mainloop()


if __name__ == '__main__':
    main()

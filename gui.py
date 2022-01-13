from tkinter import Label, Tk, filedialog, Menu, Button
from tkinter.font import Font


class GUI():
    '''
    기본 UI 담당
    '''

    def __init__(self, title):
        '''
        생성자 윈도우 생성

        title : 애플리케이션 상단에 보이는 제목
        '''
        self.main_window = Tk()
        self.main_window.title(title)

    def set_size(self, size_str):
        '''
        window의 크기 및 위치 설정

        size_str : 사이즈 및 위치를 정하는 string
        '''
        self.main_window.geometry(size_str)

    def show(self):
        '''
        window 보여주기
        '''
        self.main_window.mainloop()

    def fill_assets(self):
        '''
        에셋들로 채우기
        '''
        font1 = Font(family='굴림', size=15)
        self.label1 = Label(
            self.main_window, text='메일 자동 처리 프로그램 입니다.', pady=8, font=font1)
        self.label1.pack()

        self.button1 = Button(self.main_window, text='파일 열기',
                              font=font1, width=20, height=2)
        self.button1.pack()

    def open_filedialog(self):
        '''
        버튼을 눌렀을 때, filedialog를 띄우고
        file_path return
        '''

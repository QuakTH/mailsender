from tkinter import Label, OptionMenu, Tk, filedialog, Button, Frame,StringVar
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
        self.frame1=Frame(self.main_window,height=3)
        self.frame1.pack()

        font1 = Font(family='굴림', size=15)
        self.label1 = Label(
            self.frame1, text='메일 자동 처리 프로그램 입니다.', font=font1)
        self.label1.pack(side='left')

        email_site_list=('네이버','구글','다음')
        self.var1=StringVar(self.frame1)
        self.var1.set('사이트 선택')

        self.dropdown1=OptionMenu(self.frame1,self.var1,*email_site_list)
        self.dropdown1.config(font=font1)
        self.dropdown1.pack(side='left')

        self.frame2 = Frame(self.main_window,height=3)
        self.frame2.pack()

        self.button1 = Button(self.frame2, text='이메일 목록 파일',
                              font=font1, width=20, height=2, command=lambda :self.open_filedialog([('Excel 파일', '*.xlsx')]))
        self.button1.pack(side='left')
        self.button2 = Button(self.frame2, text='보낼 email 내용',
                              font=font1, width=15, height=2, command=lambda :self.open_filedialog([('텍트스 파일', '*.txt')]))
        self.button2.pack(side='left')

        self.frame3=Frame(self.main_window,height=3)
        self.frame3.pack()
        self.label3 = Label(
            self.frame3, text='이메일 목록 파일명 :', pady=8, font=font1)
        self.label3.pack()

        self.label4 = Label(
            self.frame3, text='<보내지는 내용 예시>', pady=8, font=font1)
        self.label4.pack()
    def open_filedialog(self, file_types):
        '''
        버튼을 눌렀을 때, filedialog를 띄우고
        file_path return
        '''
        filename = filedialog.askopenfilename(
            initialdir='/', title='파일을 선택하세요', filetypes=file_types)
        print(filename)

from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from hanja import hangul

def change_kor2yale(a):
    import hgtk

    dic_const = {u'ㄱ': 'k', u'ㄲ': 'kk', u'ㄴ': 'n', u'ㄷ': 't', u'ㄸ': 'tt', u'ㄹ': 'l', u'ㅇ': 'ng',
                 u'ㅁ': 'm', u'ㅂ': 'p', u'ㅃ': 'pp', u'ㅅ': 's', u'ㅆ': 'ss',
                 u'ㅈ': 'c', u'ㅉ': 'cc', u'ㅊ': 'ch', u'ㅋ': 'kh', u'ㅌ': 'th', u'ㅍ': 'ph', u'ㅎ': 'h',
                 u"ㄳ": [u'ㄱ', u'ㅅ'], u'ㄵ': [u'ㄴ', u'ㅈ'], u'ㄶ': [u'ㄴ', u'ㅎ'],
                 u'ㄺ': [u'ㄹ', u'ㄱ'], u'ㄻ': [u'ㄹ', u'ㅁ'], u'ㄼ': [u'ㄹ', u'ㅂ'],
                 u'ㄽ': [u'ㄹ', u'ㅅ'], u'ㄾ': [u'ㄹ', u'ㅌ'], u'ㄿ': [u'ㄹ', u'ㅍ'],
                 u'ㅀ': [u'ㄹ', u'ㅎ'], u'ㅄ': [u'ㅂ', u'ㅅ']}
    dic_vow = {u'ㅏ': 'a', u'ㅓ': 'e', u'ㅗ': 'o', u'ㅡ': 'u', u'ㅣ': 'i',
               u'ㅐ': 'ay', u'ㅔ': 'ey', u'ㅚ': 'oy', u'ㅟ': 'wi', u'ㅑ': 'ya', u'ㅕ': 'ye',
               u'ㅛ': 'yo', u'ㅠ': 'yu', u'ㅒ': 'yay', u'ㅖ': 'yey', u'ㅘ': 'wa', u'ㅙ': 'way',
               u'ㅝ': 'we', u'ㅞ': 'wey', u'ㅢ': 'uy'}

    dic_wu = {'m': 'wu', 'ph': 'wu', 'p': 'wu'}

    Kor1 = list(hgtk.text.decompose(a))

    for spc in Kor1:
        if spc == " ":
            Kor1[Kor1.index(spc)] = '~'
    for sp in Kor1:
        if sp == 'ᴥ':
            Kor1[Kor1.index(sp)] = '/'
    n = 0
    Yale = []

    while True :
            cho = dic_const[Kor1[n]]
            Yale.append(cho)
            n += 1
            if cho == 'ng':
                Yale.pop()
            if Kor1[n] != u'ㅜ':
                joong = dic_vow[Kor1[n]]
                Yale.append(joong)
                n += 1
            elif Kor1[n] == u'ㅜ':
                    if cho in dic_wu.keys():
                        joong = 'wu'
                        Yale.append(joong)
                        n += 1
                    else:
                        joong = 'u'
                        Yale.append(joong)
                        n += 1

            if Kor1[n] != '/' :
                if type(dic_const[Kor1[n]]) == list:
                    jong = list(dic_const[Kor1[n]])
                    jong1 = jong[0]
                    jong2 = jong[1]
                    Yale.append(jong1)
                    Yale.append(jong2)
                    n += 1
                    if Kor1[n] == '/':
                        Yale.append("-")
                        n += 1
                        if Kor1[n] == '~':
                            Yale.pop(-1)
                            Yale.append("  ")
                            n += 1
                else:
                    jong = dic_const[Kor1[n]]
                    Yale.append(jong)
                    n += 1
                    if Kor1[n] == '/':
                        Yale.append("-")
                        n += 1
                        if n < len(Kor1):
                            if Kor1[n] == '~':
                                Yale.pop(-1)
                                Yale.append("  ")
                                n += 1
            else:
                if Kor1[n] == '/':
                    Yale.append("-")
                    n += 1
                    if n < len(Kor1):
                        if Kor1[n] == '~':
                            Yale.pop(-1)
                            Yale.append("  ")
                            n += 1

            if n == len(Kor1):
                Yale.pop(-1)
                break

    return ''.join(Yale)


class Transducer(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title(" Kor2Yale ")
        self.pack(fill=BOTH, expand=True)

        # 안내
        anounce = Frame(self)
        anounce.pack(fill = BOTH, expand = TRUE)
        lblanounce = Label(anounce, text = u''' ◈ 예일식 표기법은 국어의 로마자 표기법과는 달리 \n     단어의 형태음운론적 구조를 표현하는 데 초점을 맞추고 있습니다. ''', width = 200)
        lblanounce.pack(side = TOP, pady = 10, padx = 10 )

        # 한국어
        kor = Frame(self)
        kor.pack(fill=X)

        lblkor = Label(kor, text=u" 변환할 단어나 문장을 입력하세요", width=30)
        lblkor.pack(side=TOP, padx=10, pady=10)

        self.entrykor = StringVar()
        self.entrykor = Entry(kor)
        self.entrykor.pack(fill=X, padx=10, expand=True)

        # 변환
        change = Frame(self)
        change.pack(fill=X)
        btnchange = Button(change, text=u" 변환 ", command = self.changing)
        btnchange.pack(side=LEFT, padx=10, pady=10)

        # 예일어
        yale = Frame(self)
        yale.pack(fill=X)

        lblyale = Label(yale, text= u" 예일어 표기 ", width=10)
        lblyale.pack(side= TOP, padx=10, pady=10)

        self.entryyale = StringVar()
        entryyale = Entry(yale, textvariable = self.entryyale)
        entryyale.pack(fill=X, padx=10, expand=True)

        # 리셋
        reset =Frame(self)
        reset.pack(fill = X)
        btnreset = Button(reset, text = u" 리셋 ", command = self.reset_)
        btnreset.pack(side =LEFT, padx = 10, pady = 10)

        # 안내사항
        anounc = Frame(self)
        anounc.pack(fill=X)

        lblanounc = Label(anounc, text=u""" ※ 텍스트 파일로 저장할 경우 최초로 1번을 클릭하고 
        계속 추가하려면 2번을 눌러주세요 ※ """, width=50)
        lblanounc.pack(side=LEFT, padx=10, pady=10)

        # 저장
        save = Frame(self)
        save.pack(fill = X)
        btnsave = Button(save, text = u" 1. 텍스트 파일로 내보내기 ", command = self.save1)
        btnsave.pack(side = LEFT, padx = 10, pady = 10)

        # 추가
        add = Frame(self)
        add.pack(fill = X)
        btnadd = Button(add, text = u" 2. 텍스트 파일에 추가하기 ", command = self.add_)
        btnadd.pack(side = LEFT, padx = 10, pady = 10)

        # 종료
        esc = Frame(self)
        esc.pack(fill = X)
        btnesc = Button(esc, text = u" 종료 ",command = self.close )
        btnesc.pack(side = RIGHT, padx =10, pady = 10)


    def changing(self):
        try:
            count = 0
            kor = self.entrykor.get()

            for i in kor:
                if hangul.is_hangul(i) == FALSE:
                    if i == " ":
                        count = 0
                    else:
                        count += 1
                else:
                    pass

            if count >= 1:
                messagebox.showerror(u" ※ 경 고 ", u" 한글만 입력하세요 ")

            elif count == 0:
                toyale = change_kor2yale(kor)
                self.entryyale.set(toyale)

        except KeyError:
            pass


    def reset_(self):
        self.entrykor.delete(0,END)
        self.entryyale.__del__()

    def save1(self):
        from datetime import datetime
        f = open("C:/Users/juha/Desktop/k2y_%d-%d.txt" % (datetime.today().month, datetime.today().day), 'w')

        kor_dt = u" ⊙ 변환한 한국어 : "
        yale_dt = u" ▷▶▷ 예일식 표기  : "
        f.write(kor_dt)
        f.write(self.entrykor.get())
        f.write("\n")
        f.write(yale_dt)
        f.write(self.entryyale.get())
        f.write("\n")
        f.close()

    def add_(self):
        from datetime import datetime
        f = open("C:/Users/juha/Desktop/k2y_%d-%d.txt" % (datetime.today().month, datetime.today().day), 'a')
        kor_dt = u" ⊙  변환한 한국어 : "
        yale_dt = u" ▷▶▷ 예일식 표기  : "
        f.write(kor_dt)
        f.write(self.entrykor.get())
        f.write("\n")
        f.write(yale_dt)
        f.write(self.entryyale.get())
        f.write("\n")
        f.close()

    def close(self):
        self.destroy()
        self.quit()


def main():
    root = Tk()
    root.geometry("600x450+120+120")
    app = Transducer(root)
    root.mainloop()


if __name__ == '__main__':
    main()
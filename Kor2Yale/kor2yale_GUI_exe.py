from tkinter import *
from Kor2Yale import k2y

class App:
    def __init__(self,change):
        Label(change, text = " 변환할 단어나 문장을 입력하세요 ").grid(row = 0, column = 0)
        self.kor = StringVar()
        kor_input = Entry(change, textvariable = self.kor)
        kor_input.grid(row = 1, column = 0)
        Label(change, text = " 예일어 표기 ").grid(row = 2, column = 0 )
        self.yale = StringVar()
        Entry(change,textvariable = self.yale).grid(row = 3, column = 0)
        b1 = Button(change, text = " click to change ", command = self.changing)
        b1.grid(row =1 , column = 1)
    def changing(self):
        kor = self.kor.get()
        toyale = k2y.change_kor2yale(kor)
        print(toyale)
        self.yale.set(toyale)



win = Tk()
win.wm_title(" 예일어 변환기 ")
app = App(win)
win.mainloop()

"""
Project with HanJaeho
 : Korean -> Yale Romanization
"""
# 1) seperating graphemes by using 'hgtk toolkit'
 # ㅁ ㅍ ㅂ = ㅜ : wu  그 외 는 u
import hgtk
# 자소분리 딕셔너리. dic_doub과 dic_wu는 특수한 경우 모음
dic_const = {'ㄱ':'k','ㄲ':'kk','ㄴ':'n','ㄷ':'t','ㄸ':'tt','ㄹ':'l','ㅇ':'ng',
             'ㅁ':'m','ㅂ':'p','ㅃ':'pp','ㅅ':'s','ㅆ':'ss',
             'ㅈ':'c','ㅉ':'cc','ㅊ':'ch','ㅋ':'kh','ㅌ':'th','ㅍ':'ph','ㅎ':'h',
             "ㄳ": ['ㄱ', 'ㅅ'], 'ㄵ': ['ㄴ', 'ㅈ'], 'ㄶ': ['ㄴ', 'ㅎ'],
             'ㄺ': ['ㄹ', 'ㄱ'], 'ㄻ': ['ㄹ', 'ㅁ'], 'ㄼ': ['ㄹ', 'ㅂ'],
             'ㄽ': ['ㄹ', 'ㅅ'], 'ㄾ': ['ㄹ', 'ㅌ'], 'ㄿ': ['ㄹ', 'ㅍ'],
             'ㅀ': ['ㄹ', 'ㅎ'], 'ㅄ': ['ㅂ', 'ㅅ']}
dic_vow = {'ㅏ':'a','ㅓ':'e','ㅗ':'o','ㅡ':'u','ㅣ':'i',
           'ㅐ':'ay','ㅔ':'ey','ㅚ':'oy','ㅟ':'wi','ㅑ':'ya','ㅕ':'ye',
           'ㅛ':'yo','ㅠ':'yu','ㅒ':'yay','ㅖ':'yey','ㅘ':'wa','ㅙ':'way',
           'ㅝ':'we','ㅞ':'wey','ㅢ':'uy'}
dic_doub = {"ㄳ":['ㄱ','ㅅ'],'ㄵ':['ㄴ','ㅈ'],'ㄶ':['ㄴ','ㅎ'],
            'ㄺ':['ㄹ','ㄱ'],'ㄻ':['ㄹ','ㅁ'],'ㄼ':['ㄹ','ㅂ'],
            'ㄽ':['ㄹ','ㅅ'],'ㄾ':['ㄹ','ㅌ'],'ㄿ':['ㄹ','ㅍ'],
            'ㅀ':['ㄹ','ㅎ'],'ㅄ':['ㅂ','ㅅ']}
dic_wu = {'m':'wu','ph':'wu','p':'wu'}
Yale = []

Kor = input("예일식 표기법으로 바꿀 단어 혹은 문장을 입력해주세요>>>>")

Kor1 = list(hgtk.text.decompose(Kor))

for spc in Kor1:
    if spc == " ":
        Kor1[Kor1.index(spc)] = '~'
for sp in Kor1:
    if sp == 'ᴥ':
        Kor1[Kor1.index(sp)] = '/'

print(Kor1)
n = 0

while True :
        cho = dic_const[Kor1[n]]
        Yale.append(cho)
        n += 1
        if cho == 'ng':
            Yale.pop()
        if Kor1[n] != 'ㅜ':
            joong = dic_vow[Kor1[n]]
            Yale.append(joong)
            n += 1
        elif Kor1[n] == 'ㅜ':
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
            print(Yale)
            print(''.join(Yale))
            break

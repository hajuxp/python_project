"""
Project with HanJaeho
 : Korean -> Yale Romanization
"""
# 1) seperating graphemes by using 'hgtk toolkit'
 # ㅁ ㅍ ㅂ = ㅜ : wu  그 외 는 u
import hgtk
# 자소분리 딕셔너리. dic_doub과 dic_wu는 특수한 경우 모음
dic_const = {'ㄱ':'k','ㄲ':'kk','ㄴ':'n','ㄷ':'t','ㄸ':'tt','ㄹ':'l',
             'ㅁ':'m','ㅂ':'p','ㅃ':'pp','ㅅ':'s','ㅆ':'ss','ㅇ':'ng',
             'ㅈ':'c','ㅉ':'cc','ㅊ':'ch','ㅋ':'kh','ㅌ':'th','ㅍ':'ph','ㅎ':'h',
             "ㄳ": ['ㄱ', 'ㅅ'], 'ㄵ': ['ㄴ', 'ㅈ'], 'ㄶ': ['ㄴ', 'ㅎ'],
             'ㄺ': ['ㄹ', 'ㄱ'], 'ㄻ': ['ㄹ', 'ㅁ'], 'ㄼ': ['ㄹ', 'ㅂ'],
             'ㄽ': ['ㄹ', 'ㅅ'], 'ㄾ': ['ㄹ', 'ㅌ'], 'ㄿ': ['ㄹ', 'ㅍ'],
             'ㅀ': ['ㄹ', 'ㅎ'], 'ㅄ': ['ㅂ', 'ㅅ']}
dic_vow = {'ㅏ':'a','ㅓ':'e','ㅗ':'o','ㅜ':['u','wu'],'ㅡ':'u','ㅣ':'i',
           'ㅐ':'ay','ㅔ':'ey','ㅚ':'oy','ㅟ':'wi','ㅑ':'ya','ㅕ':'ye',
           'ㅛ':'yo','ㅠ':'yu','ㅒ':'yay','ㅖ':'yey','ㅘ':'wa','ㅙ':'way',
           'ㅝ':'we','ㅞ':'wey','ㅢ':'uy'}
dic_doub = {"ㄳ":['ㄱ','ㅅ'],'ㄵ':['ㄴ','ㅈ'],'ㄶ':['ㄴ','ㅎ'],
            'ㄺ':['ㄹ','ㄱ'],'ㄻ':['ㄹ','ㅁ'],'ㄼ':['ㄹ','ㅂ'],
            'ㄽ':['ㄹ','ㅅ'],'ㄾ':['ㄹ','ㅌ'],'ㄿ':['ㄹ','ㅍ'],
            'ㅀ':['ㄹ','ㅎ'],'ㅄ':['ㅂ','ㅅ']}
dic_wu = {'ㅁ':'wu','ㅍ':'wu','ㅂ':'wu'}

dic_sp = {'/':" "}

Kor = input("예일식 표기법으로 바꿀 단어 혹은 문장을 입력해주세요>>>>")

Kor1 = list(hgtk.text.decompose(Kor))

for sp in Kor1:
    if sp == 'ᴥ':
        Kor1[Kor1.index(sp)] = '/'

Yale = []
n = 0


for cho in dic_const.keys():
    if cho == Kor1[n]:
        Yale.append(dic_const[cho])
        n += 1
        for joong in dic_vow.keys():
            if joong == Kor1[n]:
                Yale.append(dic_vow[joong])
                n += 1
                for jong in dic_const.keys():
                    if type(jong) == list:




# while n > len(Kor1) :
#     if Kor1[n] in dic_const.keys():
#         cho = dic_const[Kor1[n]]
#         Yale.append(cho)
#         n += 1
#         if Kor1[n] in dic_const.keys():
#             joong = dic_vow[Kor1[n]]
#             Yale.append(joong)
#             n += 1
#             if Kor1[n] == '/':
#                 Yale.append(" ")
#                 n += 1
#             elif Kor1[n] in dic_doub :
#                 jong1 = dic_const[Kor1[n][0]]
#                 jong2 = dic_const[Kor1[n][1]]
#                 Yale.append(jong1)
#                 Yale.append(jong2)
#                 n += 1
#                 if Kor1[n] == '/':
#                     Yale.append(" ")
#                     n += 1
#                 else:
#                     jong = dic_const[Kor1[n]]
#                     Yale.append(jong)
#                     n += 1
#                     if Kor1[n] == '/':
#                         Yale.append(" ")
#                         n += 1
#
# print(Yale)
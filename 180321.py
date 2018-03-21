"""
 REINDEX (재색인)
  - 새로운 색인에 맞도록 객체를 새로 생성하는 기능이다.
"""
from pandas import Series, DataFrame
import pandas as pd
import numpy  as np

# ex1)
obj = Series([4.5,7.2,-5.3,3.6], index=['d','b','a','c'])
print(obj)
'''
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64
'''
 # 이 series객체에 대해 reindex를 호출하면 데이터를 새로운 색인에 맞게 재배열하고,
 # 없는 색인 값이 있다면 비어있는 값을 새로 추가한다.
obj2 = obj.reindex(['a','b','c','d','e'])
print(obj2)
obj2 = obj.reindex(['a','b','c','d','e'],fill_value=0)
print(obj2)
'''
a   -5.3
b    7.2
c    3.6
d    4.5
e    NaN    / e    0.0
dtype: float64
'''
 # 시계열같은 순차적인 데이터를 재색인할 때 값을 보간하거나 채워넣어야 하는 경우가 있다.
 # 이런 경우 method옵션을 이용해서 해결할 수 있다.
 # ffill or pad 앞의 값으로 채워넣기 / bfrill or backfill 뒤의 값으로 채워넣기
 # method = 'ffill' 과 같은 방식으로 옵션을 준다
obj3 = Series(['blue','purple','yellow'],index=[0,2,4])
print(obj3)
'''
0      blue
2    purple
4    yellow
dtype: object
'''
print(obj3.reindex(range(6),method='ffill'))
'''
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
'''

# DataFrame에 대한 재색인은 로우색인,칼럼색인 또는 둘 다 변경이 가능하다.
# 순서만 전달하면 로우가 재색인된다(기본값은 로우)

frame = DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],
                  columns=['Ohio','Texas','California'])
print(frame)
'''
   Ohio  Texas  California
a     0      1           2
c     3      4           5
d     6      7           8
'''

frame2 = frame.reindex(['a','b','c','d'])
print(frame2)
'''
   Ohio  Texas  California
a   0.0    1.0         2.0
b   NaN    NaN         NaN
c   3.0    4.0         5.0
d   6.0    7.0         8.0
'''
 # 열은 columns 예악어를 사용해서 재색인할 수 있다.
states = ['Texas','Utah','California']
frame3 = frame.reindex(columns = states)
print(frame3)
'''
   Texas  Utah  California
a      1   NaN           2
c      4   NaN           5
d      7   NaN           8
'''

 # 로우와 칼럽은 모두 한번에 재색인할 수 있지만, 보간은 로우에 대해서만 이루어진다.
 # frame4 = frame.reindex(index = ['a','b','c','d'],method = 'ffill', columns = states)
 # 책 내용대로 위와같이 실행했을 경우 ValueError: index must be monotonic increasing or decreasing가 뜬다
 # 검색결과 pandas의 old bug라고 뜨는데.. 이유는 모르겠으나. 아래와 같이 실행하면 실행됨
frame4 = frame.reindex(index = ['a','b','c','d'],columns = states).ffill()
print(frame4)
'''
   Texas  Utah  California
a    1.0   NaN         2.0
b    1.0   NaN         2.0
c    4.0   NaN         5.0
d    7.0   NaN         8.0
'''

 # 재색인은 ix를 이용해 라벨로 색인하면 좀 더 간결하게 할 수 있다.
print(frame.ix[['a','b','c','d','e'],states])
'''
   Texas  Utah  California
a    1.0   NaN         2.0
b    NaN   NaN         NaN
c    4.0   NaN         5.0
d    7.0   NaN         8.0
e    NaN   NaN         NaN
'''


"""
 하나의 로우 또는 칼럼 삭제하기
  - 색인 배열 또는 삭제하려는 로우나 칼럼이 제외된 리스트를 이미 가지고 있다면 쉽게 삭제 가능
    drop 메서드를 사용하면 선택된 값이 삭제된 새로운 객체 얻을 수 있다
"""

obj = Series(np.arange(5.), index=['a','b','c','d','e'])
new_obj = obj.drop('c')
print(new_obj)
'''
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
'''
print(obj.drop(['d','c']))
'''
a    0.0
b    1.0
e    4.0
dtype: float64
'''
# DataFrame 에서는 로우와 칼럼 모두에서 값 삭제가능
data = DataFrame(np.arange(16).reshape((4,4)),
                 index=['Ohio','Colorado','Utah','New York'],
                 columns=['one','two','three','four'])
print(data.drop(['Colorado','Ohio']))
'''
          one  two  three  four
Utah        8    9     10    11
New York   12   13     14    15
'''
print(data.drop('two',axis=1))
'''
          one  three  four
Ohio        0      2     3
Colorado    4      6     7
Utah        8     10    11
New York   12     14    15
'''
print(data.drop(['two','four'],axis=1))
'''
          one  three
Ohio        0      2
Colorado    4      6
Utah        8     10
New York   12     14
'''
 # 디폴트값은 로우이므로, 로우을 삭제할때에는 삭제할 로우명만 입력
 # 칼럼을 삭제할 때에는, 칼럼명과 뒤에 axis = 1 로 지정해줘야함.

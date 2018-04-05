from pandas import Series, DataFrame
import numpy as np
# Series의 색인은 Numpy배열과 유사하게 동작하는데, 다른 점은 Series의 색인은 *정수가 아니어도 된다는 점이다.
obj = Series(np.arange(4.),index=['a','b','c','d'])
print(obj['b'], "/", obj[1])
'''
>>> 1.0 / 1.0
'''
print(obj[2:4])
'''
>>> c    2.0
    d    3.0
    dtype: float64
'''
print(obj[['a','b','c']])
'''
>>> a    0.0
    b    1.0
    c    2.0
    dtype: float64
'''
print(obj[[1,3]])
'''
>>> b    1.0
    d    3.0
    dtype: float64
'''
print(obj[obj < 2])
'''
>>> a    0.0
    b    1.0
    dtype: float64
'''

# 라벨 이름으로 슬라이싱하는 것은 시작점과 끝점을 포함한다는 점이 일반 파이썬에서의 슬라이싱과 다르다.
print(obj['b':'d'])
'''
>>> b    1.0
    c    2.0
    d    3.0
    dtype: float64
'''     # 일반슬라이싱의 경우 'b' : 'd' 의 의미는 b =<  < d 의 의미.
obj['b':'c'] = 5
print(obj)
'''
>>> a    0.0
    b    5.0
    c    5.0
    d    3.0
    dtype: float64
'''

# DateFrame에서 칼럼의 값을 하나 이상 가져올 수 있다.
data = DataFrame(np.arange(16).reshape((4,4)),
                 index=['Ohio','Texas','Utah',"New York"],
                 columns=['one','two','three','four'])
print(data)
print(data['two'])
'''
>>> Ohio         1
    Texas        5
    Utah         9
    New Yokr    13
    Name: two, dtype: int32
'''
print(data[['three','one']])   # 두 개이상을 가져올때는 [ ]로 묶기
'''
>>>           three  one
    Ohio          2    0
    Texas         6    4
    Utah         10    8
    New Yokr     14   12
'''
# 슬라이싱으로 로우를 선택하거나 불리언 배열로 칼럼을 선택할 수도 있다.
print(data[:2])
'''
>>>        one  two  three  four
    Ohio     0    1      2     3
    Texas    4    5      6     7'''
print(data[data['three']>5])   # 불리언배열을 통한
'''
>>>           one  two  three  four
    Texas       4    5      6     7
    Utah        8    9     10    11
    New Yokr   12   13     14    15
'''
print(data<5)   # 스칼라 비교를 통해 생성된 불리언 dataframe을 사용해 값 선택
'''
>>>             one    two  three   four
    Ohio       True   True   True   True
    Texas      True  False  False  False
    Utah      False  False  False  False
    New Yokr  False  False  False  False

'''
# data[data<5]=0
print(data)
'''
>>>           one  two  three  four
    Ohio        0    0      0     0
    Texas       0    5      6     7
    Utah        8    9     10    11
    New Yokr   12   13     14    15
'''

# ix
# Numpy와 비슷한 방식에 추가적으로 축의 라벨을 통해 DataFrame의 로우와 칼럼을 선택할 수 있도록 한다.
# 재색인을 좀 더 간단하게 할 수 있는 방법

print(data.ix['New York',['two','three']])
'''
>>> two      13
    three    14
    Name: New York, dtype: int32
'''
print(data.ix[['Utah','Ohio'],[3,0,1]])  # 로우는 Utah와 Ohio선택 / 컬럼은 3번째, 0번째, 1번째 순서로 선택
'''
>>>       four  one  two
    Utah    11    8    9
    Ohio     3    0    1
'''

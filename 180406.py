"""
산술연산과 데이터정렬
pandas에서 중요한 기능은 색인이 다른 객체간의 연술이다.
객체를 더할 때 짝이 맞지 않는 색인이 있다면 두 색인이 통합된다"""
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a','c','d','e'])
s2 = Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
print(s1, s2)
print(s1+s2)    # 결과값으로 중복되는 a,c,e에 대한 값은 더해지고, 나머지 d,f,g는 NaN값으로 출력

df1 = DataFrame(np.arange(9.).reshape((3,3)), columns=list('bcd'),
                index= ['Ohio','Texas','Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),
                index=['Utah','Ohio','Texas','Oregon'])

print(df1+df2)  # 결과값으로 Texas와 Ohio의 b,d 값만 연산되고 나머지는 NaN
                # 출력값은 로우 기준으로 알파벳순서대로 정렬되어 출력
'''
서로 다른 색인을 가지는 객체 간의 산술연산에서 존재하지 않는 축의 값을 특수한 값(0 같은)으로 지정하고 싶을 때는
다음과 같이 할 수 있다. '''

df1 = DataFrame(np.arange(12.).reshape((3,4)),columns= list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))
print(df1+df2)

# df1의 add 메서드로 df2와 fill_value 값을 인자로 전달한다.
print(df1.add(df2, fill_value=0))   # df1에 df2를 더하는데, 없는값은 fill_value로 0을 넣어준다

# Series나 DataFrame을 재색인할 때 역시 fill_value를 지정할 수 있다.
print(df1.reindex(columns=df2.columns, fill_value=0))
# reindex를 쓸 경우, 전체 NAN이 나온 곳(중복되지않는 로우)은 출력값에 나오지 않음
# columns를 reindex 했기 때문에, e는 0으로 채워짐

'''
산술연산 메서드
add  :  덧셈을 위한 메서드
sub  :  뺄샘을 위한 메서드
div  :  나눗셈을 위한 메서드
mul  :  곱셈을 위한 메서드   '''

# ex
da = DataFrame(np.arange(10.).reshape((2,5)),columns=list('abcde'))
da2 = DataFrame(np.arange(20.).reshape((5,4)),columns=list('abnd'))

print(da.mul(da2, fill_value = 0 ))

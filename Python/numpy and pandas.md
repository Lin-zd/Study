# Numpy and Pandas 入门

## 01-numpy基本属性

```python
import numpy as np

array = np.array([[1,2,3],
                  [2,3,4]])
print(array)
print('number of dim:', array.ndim)
print('shape:', array.shape)
print('size:', array.size)

"""
[[1 2 3]
 [2 3 4]]
number of dim: 2
shape: (2, 3)
size: 6
"""
```

## 02-numpy创建array

```python
import numpy as np

a = np.array([2,23,4], dtype=int)
# a = np.array([2,23,4], dtype=float)
print(a.dtype)

"""
int32
# float64
"""
```

```python
import numpy as np

a = np.array([ [2,23,4],
               [2,32,4] ])
print(a)
"""
[[ 2 23  4]
 [ 2 32  4]]
"""
b = np.zeros((3,4))
print(b)
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""
c = np.ones((3,4), dtype=int)
print(c)
"""
[[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
"""
d = np.empty((3,4))
print(d)
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""
e = np.arange(10,20,2)
print(e)
"""
[10 12 14 16 18]
"""
f = np.arange(12).reshape((3,4))
print(f)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""
g = np.linspace(1,10,6).reshape((2,3))
print(g)
"""
[[ 1.   2.8  4.6]
 [ 6.4  8.2 10. ]]
"""
```

## 03-numpy的基础运算

```python
import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4)
print(a)
print(b)
print(b<3)
print(b==3)
"""
[10 20 30 40]
[0 1 2 3]
[ True  True  True False]
[False False False  True]
"""

c = a - b
print(c)

d = a + b
print(d)

e = b ** 2
print(e)

f = 10*np.sin(a)
print(f)

"""
[10 19 28 37]
[10 21 32 43]
[0 1 4 9]
[-5.44021111  9.12945251 -9.88031624  7.4511316 ]
"""
```

```python
import numpy as np

a = np.array([[1,1],
              [0,1]])
b = np.arange(4).reshape((2,2))

print(a)
print(b)

c = a*b
c_dot = np.dot(a,b) # 矩阵乘法
c_dot_2 = a.dot(b)
print(c)
print(c_dot)
print(c_dot_2)

"""
[[1 1]
 [0 1]]
[[0 1]
 [2 3]]
[[0 1]
 [0 3]]
[[2 4]
 [2 3]]
[[2 4]
 [2 3]]
"""

x = np.random.random((2,4))
print(x)

print(np.sum(x))
print(np.min(x))
print(np.max(x))
print(np.sum(x,axis=1))    # 列求和
print(np.min(x,axis=0))    # 行求最小值
print(np.max(x,axis=1))    # 列求最大值

"""
[[0.76484817 0.19350868 0.06904974 0.02365789]
 [0.43020867 0.5095642  0.12217376 0.30596241]]
2.418973531454805
0.023657891631676975
0.7648481731598034
[1.05106449 1.36790904]
[0.43020867 0.19350868 0.06904974 0.02365789]
[0.76484817 0.5095642 ]
"""
```

```python
import numpy as np

A = np.arange(2,14).reshape(3,4)

print(np.argmin(A)) # 索引最小值的位置
print(np.argmax(A))  # 索引最大值位置
print(np.mean(A))   # 平均值
print(np.mean(A, axis=0))  # 按某一轴进行计算
print(np.median(A))  # 中位数
print(A)
print(np.cumsum(A))  # 逐项累加
print(np.diff(A))  # 逐项累差
print(np.nonzero(A))  #找出非0数的位置

B = np.arange(14,2,-1).reshape(3,4)

print(np.sort(B))  # 逐行排序
print(np.transpose(B))
print(B.T)
print(np.clip(B,5,9))  #小于5的数等于5 大于9的数等于9 中间数不变

"""
0
11
7.5
[6. 7. 8. 9.]
7.5
[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]]
[ 2  5  9 14 20 27 35 44 54 65 77 90]
[[1 1 1]
 [1 1 1]
 [1 1 1]]
(array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], dtype=int64), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], dtype=int64))
[[11 12 13 14]
 [ 7  8  9 10]
 [ 3  4  5  6]]
[[14 10  6]
 [13  9  5]
 [12  8  4]
 [11  7  3]]
[[14 10  6]
 [13  9  5]
 [12  8  4]
 [11  7  3]]
[[9 9 9 9]
 [9 9 8 7]
 [6 5 5 5]]
"""
```

## 04-numpy索引

```python
import numpy as np

A = np.arange(3,15)
B = np.arange(3,15).reshape(3,4)

print(A)
print(A[3])
print(B)
print(B[2][1])
print(B[2,1])
print(B[2,:])
print(B[:,1])
# 迭代每一行
for row in B:
    print(row)

print(B.T)
# 迭代每一列
for column in B.T:
    print(column)

print(A.flatten())
# 迭代每一个数
for item in B.flat:
    print(item)
    
"""
[ 3  4  5  6  7  8  9 10 11 12 13 14]
6
[[ 3  4  5  6]
 [ 7  8  9 10]
 [11 12 13 14]]
12
12
[11 12 13 14]
[ 4  8 12]
[3 4 5 6]
[ 7  8  9 10]
[11 12 13 14]
[[ 3  7 11]
 [ 4  8 12]
 [ 5  9 13]
 [ 6 10 14]]
[ 3  7 11]
[ 4  8 12]
[ 5  9 13]
[ 6 10 14]
[ 3  4  5  6  7  8  9 10 11 12 13 14]
3
4
5
6
7
8
9
10
11
12
13
14
"""
```

## 05-numpy array合并

```python
import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

C = np.vstack((A, B)) # 上下合并AB
D = np.hstack((A,B)) # 左右合并
print(C)
print(D)
print(A.shape,C.shape)
print(A.shape,D.shape)

print(A[np.newaxis,:].shape)  # 增加维度
print(A[np.newaxis,:])  # 增加维度

print(A[:,np.newaxis].shape)  # 增加维度
print(A[:,np.newaxis])  # 增加维度
"""
[[1 1 1]
 [2 2 2]]
[1 1 1 2 2 2]
(3,) (2, 3)
(3,) (6,)
(1, 3)
[[1 1 1]]
(3, 1)
[[1]
 [1]
 [1]]
"""
```

```python
import numpy as np

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]

C = np.vstack((A, B)) # 上下合并AB
D = np.hstack((A,B)) # 左右合并
print(C)
print(D)
print(A.shape,C.shape)
print(A.shape,D.shape)

E = np.concatenate((A,B,B,A),axis=0)
print(E)

"""
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]]
[[1 2]
 [1 2]
 [1 2]]
(3, 1) (6, 1)
(3, 1) (3, 2)
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]
 [2]
 [2]
 [2]
 [1]
 [1]
 [1]]
"""
```

## 06-numpy array分割

```python
import numpy as np

A = np.arange(12).reshape(3,4)
print(A)

print(np.split(A,2,axis=1)) # 按列分成两块
print(np.split(A,3,axis=0)) # 按行分成两块

print(np.array_split(A,3,axis=1)) # 不均匀分割

print(np.vsplit(A,3))  # 按行分割
print(np.hsplit(A,2))  # 按列分割

"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2],
       [ 6],
       [10]]), array([[ 3],
       [ 7],
       [11]])]
[array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11]])]
"""
```

## 07-numpy cope & deep copy

```python
import numpy as np

a = np.arange(4)
b = a
c = a
d = b
a[0] = 11
print(b is a)
print(b)
print(c)
print(d)
d[1:3] = [22,33]
print(a)

"""
True
[11  1  2  3]
[11  1  2  3]
[11  1  2  3]
[11 22 33  3]
"""
```

```python
import numpy as np

a = np.arange(4)
b = a.copy()  # deep copy

a[3] = 44
print(b is a)
print(a)
print(b)

"""
False
[ 0  1  2 44]
[0 1 2 3]
"""
```

## 01-pandas基本介绍

```python
import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
print(s)

dates = pd.date_range('20160101',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
"""
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
               '2016-01-05', '2016-01-06'],
              dtype='datetime64[ns]', freq='D')
                   a         b         c         d
2016-01-01 -0.478008 -0.586170 -0.324736 -1.752621
2016-01-02 -0.280455 -1.236538 -0.134364  0.190156
2016-01-03 -0.809115  0.790370  0.292850 -1.806293
2016-01-04  0.458943  0.227262  0.172643  1.448147
2016-01-05 -0.655451  0.281851 -0.365744 -0.177848
2016-01-06  0.730406  1.424807  2.292938  0.029142
"""
```

```python
df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)

df2 = pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20130102'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),
    'F':'foo'
})
print(df2)
print(df2.dtypes)
print(df2.index)  # 输出所有列
print(df2.columns) # 输出所有行
print(df2.values)  # 输出所有值
print(df2.describe()) # 数值处理
print(df2.T)
print(df2.sort_index(axis=1, ascending=False)) # 按列排序 倒序
print(df2.sort_index(axis=0, ascending=False)) # 按行排序 倒序
print(df2.sort_values(by='E'))  # 指定值排序

"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
Index([0, 1, 2, 3], dtype='int64')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
[[1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']]
         A                    B    C    D
count  4.0                    4  4.0  4.0
mean   1.0  2013-01-02 00:00:00  1.0  3.0
min    1.0  2013-01-02 00:00:00  1.0  3.0
25%    1.0  2013-01-02 00:00:00  1.0  3.0
50%    1.0  2013-01-02 00:00:00  1.0  3.0
75%    1.0  2013-01-02 00:00:00  1.0  3.0
max    1.0  2013-01-02 00:00:00  1.0  3.0
std    0.0                  NaN  0.0  0.0
                     0  ...                    3
A                  1.0  ...                  1.0
B  2013-01-02 00:00:00  ...  2013-01-02 00:00:00
C                  1.0  ...                  1.0
D                    3  ...                    3
E                 test  ...                train
F                  foo  ...                  foo

[6 rows x 4 columns]
     F      E  D    C          B    A
0  foo   test  3  1.0 2013-01-02  1.0
1  foo  train  3  1.0 2013-01-02  1.0
2  foo   test  3  1.0 2013-01-02  1.0
3  foo  train  3  1.0 2013-01-02  1.0
     A          B    C  D      E    F
3  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
0  1.0 2013-01-02  1.0  3   test  foo
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
2  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""
```

## 02-pandas选择数据

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df['A'])
print(df.A)
print(df[0:3])
print(df['20130102':'20130104'])
"""
2013-01-01     0
2013-01-02     4
2013-01-03     8
2013-01-04    12
2013-01-05    16
2013-01-06    20
Freq: D, Name: A, dtype: int32
2013-01-01     0
2013-01-02     4
2013-01-03     8
2013-01-04    12
2013-01-05    16
2013-01-06    20
Freq: D, Name: A, dtype: int32
            A  B   C   D
2013-01-01  0  1   2   3
2013-01-02  4  5   6   7
2013-01-03  8  9  10  11
             A   B   C   D
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
"""
```

```python
# select by lable:loc  根据标签选择
print(df.loc['20130102'])
print(df.loc[:,['A','B']])
print(df.loc['20130102',['A','B']])  # 打印某一行的某些列
"""
A    4
B    5
C    6
D    7
Name: 2013-01-02 00:00:00, dtype: int32
             A   B
2013-01-01   0   1
2013-01-02   4   5
2013-01-03   8   9
2013-01-04  12  13
2013-01-05  16  17
2013-01-06  20  21
A    4
B    5
Name: 2013-01-02 00:00:00, dtype: int32
"""
```

```python
# select by position:iloc  根据位置选择
print(df.iloc[3])
print(df.iloc[3,1])
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])
"""
A    12
B    13
C    14
D    15
Name: 2013-01-04 00:00:00, dtype: int32
13
             B   C
2013-01-04  13  14
2013-01-05  17  18
             B   C
2013-01-02   5   6
2013-01-04  13  14
2013-01-06  21  22
"""
```

```python
# Boolean indexing
print(df)
print(df[df.A>8])
"""
             A   B   C   D
2013-01-01   0   1   2   3
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
             A   B   C   D
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
"""
```

## 03-pandas设置值

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])

print(df)
df.iloc[1,2] = 11
df.loc['20130101','B'] = 22
df[df.A>8] = 0    # A列大于8的行变为0
df.B[df.A>4] = 0  # A列大于4的行中的 B列变为0
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
df['F'] = np.nan
print(df)
"""
             A   B   C   D
2013-01-01   0   1   2   3
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
             A   B   C   D  E   F
2013-01-01   0  22   2   3  1 NaN
2013-01-02   4   5  11   7  2 NaN
2013-01-03   8   0  10  11  3 NaN
2013-01-04  12   0  14  15  4 NaN
2013-01-05  16   0  18  19  5 NaN
2013-01-06  20   0  22  23  6 NaN
"""
```

## 04-pandas处理丢失数据

```python
import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])


df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)
print(df.dropna(axis=0,how='any')) # 按行丢弃缺失值 how={'any','all'}
print(df.dropna(axis=1,how='any')) # all 只有某一行全缺失才会丢掉
# 填充缺失值
print(df.fillna(value=0))
# 检查数值
print(df.isnull()) # 缺失数值位置返回True
print(np.any(df.isnull())==True)  # 至少存在丢失值
"""
             A     B     C   D
2013-01-01   0   NaN   2.0   3
2013-01-02   4   5.0   NaN   7
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
             A     B     C   D
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
             A   D
2013-01-01   0   3
2013-01-02   4   7
2013-01-03   8  11
2013-01-04  12  15
2013-01-05  16  19
2013-01-06  20  23
             A     B     C   D
2013-01-01   0   0.0   2.0   3
2013-01-02   4   5.0   0.0   7
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
                A      B      C      D
2013-01-01  False   True  False  False
2013-01-02  False  False   True  False
2013-01-03  False  False  False  False
2013-01-04  False  False  False  False
2013-01-05  False  False  False  False
2013-01-06  False  False  False  False
True
"""
```

## 05-pandas导入导出

```python
import pandas as pd

# 导入
data = pd.read_csv('student.csv')
print(data)
# 导出
data.to_pickle('student.pickle')
```

## 06-pandas合并 concat

```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
# concatenating  优先选用
res1 = pd.concat([df1,df2,df3],axis=0) # 按行合并
res1_1 = pd.concat([df1,df2,df3],axis=0,ignore_index=True) # 按行合并
res2 = pd.concat([df1,df2,df3],axis=1) # 按列合并
print(res1)
print(res1_1)
print(res2)
"""
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
     a    b    c    d    a    b    c    d    a    b    c    d
0  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0  2.0  2.0  2.0  2.0
1  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0  2.0  2.0  2.0  2.0
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0  2.0  2.0  2.0  2.0
"""
```

```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])

res1 = pd.concat([df1,df2],join='outer') # 默认为outer
# join ['inner','outer']
res2 = pd.concat([df1,df2],join='inner',ignore_index=True) # 裁剪 取共有部分
print(res1)
print(res2)
"""
     a    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN
2  0.0  0.0  0.0  0.0  NaN
3  0.0  0.0  0.0  0.0  NaN
2  NaN  1.0  1.0  1.0  1.0
3  NaN  1.0  1.0  1.0  1.0
4  NaN  1.0  1.0  1.0  1.0
     b    c    d
0  0.0  0.0  0.0
1  0.0  0.0  0.0
2  0.0  0.0  0.0
3  1.0  1.0  1.0
4  1.0  1.0  1.0
5  1.0  1.0  1.0
"""
```

```python
import pandas as pd
import numpy as np

# append
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df1._append([df2,df3],ignore_index=True)
res1 = df1._append(s1,ignore_index=True)
print(res)
print(res1)
"""
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  1.0  1.0  1.0  1.0
7  1.0  1.0  1.0  1.0
8  1.0  1.0  1.0  1.0
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  2.0  3.0  4.0
"""
```

## 07-pandas合并 merge

```python
import pandas as pd

left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})
right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})
res = pd.merge(left,right,on='key')
print(res)
"""
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
"""
```

```python
import pandas as pd

left = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})
right = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})
# how = ['left','right','outer','inner']
res = pd.merge(left,right,on=['key1','key2'],how='inner') #默认
res1 = pd.merge(left,right,on=['key1','key2'],how='outer') #默认
res2 = pd.merge(left,right,on=['key1','key2'],how='left') #默认
res3 = pd.merge(left,right,on=['key1','key2'],how='right') #默认

print(res)
print(res1)
print(res2)
print(res3)

"""
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K0   K0  A0  B0  C1  D1
2   K1   K0  A2  B2  C2  D2
  key1 key2    A    B    C    D
0   K0   K0   A0   B0   C0   D0
1   K0   K0   A0   B0   C1   D1
2   K0   K1   A1   B1  NaN  NaN
3   K1   K0   A2   B2   C2   D2
4   K2   K1   A3   B3  NaN  NaN
5   K2   K0  NaN  NaN   C3   D3
  key1 key2   A   B    C    D
0   K0   K0  A0  B0   C0   D0
1   K0   K0  A0  B0   C1   D1
2   K0   K1  A1  B1  NaN  NaN
3   K1   K0  A2  B2   C2   D2
4   K2   K1  A3  B3  NaN  NaN
  key1 key2    A    B   C   D
0   K0   K0   A0   B0  C0  D0
1   K0   K0   A0   B0  C1  D1
2   K1   K0   A2   B2  C2  D2
3   K2   K0  NaN  NaN  C3  D3
"""
```

```python
import pandas as pd

df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_left':[2,2,2]})

# how = ['left','right','outer','inner']
res = pd.merge(df1,df2,on='col1',how='outer',indicator=True)

print(res)
"""
   col1 col_left_x  col_left_y      _merge
0     0          a         NaN   left_only
1     1          b         2.0        both
2     2        NaN         2.0  right_only
3     2        NaN         2.0  right_only
"""
```

```python
import pandas as pd

left = pd.DataFrame({
    'A':['A0','A1','A2'],
    'B':['B0','B1','B2']
},index=['K0','K1','K2'])
right = pd.DataFrame({
    'C':['C1','C2','C3'],
    'D':['D1','D2','D3']
},index=['K0','K2','K3'])

print(left)
print(right)

res = pd.merge(left,right,left_index=True,right_index=True,how='outer')

print(res)
"""
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
     C   D
K0  C1  D1
K2  C2  D2
K3  C3  D3
      A    B    C    D
K0   A0   B0   C1   D1
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3  NaN  NaN   C3   D3
"""
```

```python
import pandas as pd

boys = pd.DataFrame({
    'k':['K0','k1','k2'],
    'age':[1,2,3]
})
girls = pd.DataFrame({
    'k':['K0','K0','K3'],
    'age':[4,5,6]
})

res = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')

print(res)
"""
    k  age_boy  age_girl
0  K0      1.0       4.0
1  K0      1.0       5.0
2  k1      2.0       NaN
3  k2      3.0       NaN
4  K3      NaN       6.0
"""
```

## 08-pandas plot画图

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()
```

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list("ABCD")
                    )
data = data.cumsum()
print(data.head(5))
data.plot()
plt.show()
```

plot methods:

'bar'    'hist'   'box'    'scatter'    'kde'    'area'    'hexbin'    'pie'

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list("ABCD")
                    )
data = data.cumsum()

ax =data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)
plt.show()
```


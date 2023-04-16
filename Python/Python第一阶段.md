# Python-第一阶段

## 第六章 数据容器

### 01-列表

```python
list = []
list.append(元素)       #向列表中追加元素
list.extend(容器)       #将数据容器的内容依次取出，追加到列表尾部
list.insert(下标，元素)  #在指定下标出，插入指定的元素
del list[下标]          #删除列表指定下标元素
list.pop(下标)          #删除列表指定下标元素
list.remove(元素)       #从前向后，删除此元素第一个匹配项
list.clear()           #清空列表
list.count(元素)        #统计此元素在列表中出现的次数
list.index(元素)        #查找指定元素在列表的下标，找不到报错ValueError
len(列表)               #统计容器内有多少元素
```

**列表的特点：**

+ 可以容纳多个元素
+ 可以容纳不同类型的元素
+ 数据是有序存储的(有下标序号)
+ 允许重复数据存在
+ 可以修改(增加或删除元素等)

### 02-元组

```python
index()  #查找某个数据，如果数据存在返回对应下表，否则报错
count()  #统计某个数据在当前元组出现的次数
len(元组)  #统计元组内的元素个数
```

```python
# 根据下标（索引）取出数据
t1 = (1, 2, 'hello')
print(t1[2])  # 结果 'hello'
# 根据index()，查找特定元素的第一个匹配项
t1 = (1, 2, 'hello', 3, 4, 'hello')
print(t1.index('hello'))  # 结果 2
# 统计某个数据在元组内出现的次数
t1 = (1, 2 'hello', 3, 4, 'hello')
print(t1.count('hello'))  # 结果 2
# 统计元组内的元素个数
t1 = (1, 2, 3)  
print(len(t1))  # 结果 3
```

**元组的特点：**

+ 可以容纳多个数据
+ 可以容纳不同类型的数据
+ 数据是有序存储的（下标索引）
+ 允许重复数据存在
+ 不可以修改（增加或删除元素等）
+ 支持for循环

### 03-字符串

```python
str = ""
str[下标]  #根据下标索引取出特定位置字符
str.index(字符串)  #查找给定字符的第一个匹配项的下标
str.replace(字符串1, 字符串2)  #将字符串内的全部字符串1替换为字符串2 不会修改原字符串 而是得到新字符串
str.split(字符串)  #根据给定字符串对字符串进行分隔，不会修改原字符串，而是得到一个新的列表
str.strip()  #移除首尾的空格和换行符
str.strip(字符串)  #移除指定字符串
str.count(字符串)  #统计字符串内某字符串的出现次数
len(str)  #统计字符串的字符个数
```

**字符串的特点：**

+ 只能存储字符串
+ 长度任意（取决于内存大小）
+ 支持下标索引
+ 允许重复字符串存在
+ 不可以修改（增加或删除元素等）
+ 支持for循环

### 04-序列

**序列的常用操作-切片**

序列支持切片，即列表、元组、字符串均支持进行切片操作

切片：从一个序列中取出一个子序列

```python
序列[起始下标:结束下标:步长]  #表示从指定位置开始依次取出元素到指定位置结束，得到一个新的序列
```

起始下标：从何处开始去，可以留空，留空即为从头开始

结束下标：何处结束（不含此处），可以留空，留空即取到结尾

步长：依次取出元素的间隔

步长1表示一个个去元素，2表示每次跳过1个元素取，N表示每次跳过N-1个元素取，步长为负数表示反向取（注意，起始下标和结束下标也要反向标记）



## 集合

无序，无重复元素

![image-20230314095035501](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230314095035501.png)

![image-20230314095247890](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230314095247890.png)

![image-20230314095417493](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230314095417493.png)

![image-20230314100045950](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230314100045950.png)



## 字典

![image-20230315141455310](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230315141455310.png)

![image-20230315143834167](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230315143834167.png)

![image-20230315143958108](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230315143958108.png)

## 数据容器总结

![image-20230315151027663](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230315151027663.png)

![image-20230315151048672](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230315151048672.png)

![image-20230315152449825](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230315152449825.png)

### 函数传参形式

![image-20230318094438260](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230318094438260.png)

![image-20230318100653166](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230318100653166.png)

## 文件

![image-20230321202422811](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230321202422811.png)

![image-20230323191601353](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230323191601353.png)

![image-20230323192024272](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230323192024272.png)

## 数据转换

![image-20230327095534292](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20230327095534292.png)


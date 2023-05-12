# Python-第二阶段

## 第一章

### 01-初识对象

现实中的例子：设计表格——打印表格——填写表格

程序中的实现：设计类(class)——创建对象——对象属性赋值 

### 02-类的成员方法

1. 类的两个组成部分

+ 类的属性，称之为：成员变量

+ 类的行为， 称之为：成员**方法**

  函数是写在类外的，方法定义在类内部

2. 类和成员的定义语法

   ```python
   calss 类名称:
       成员变量
       
       def 成员方法(self, 参数列表)
           成员方法体
   
   对象 = 类名称()
   ```

3. self的作用

- 表示类对象本身的意思
- 只有通过self，成员方法才能访问类的成员变量
- self出现在形参列表中，但是不占用参数位置，无需理会

```python
class Student:
    name = None

    def say_hi(self):
        print(f"大家好，我是{self.name}，欢迎大家多多关照")

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name},{msg}")

stu = Student()
stu.name = "小林"
stu.say_hi()

stu1 = Student()
stu1.name = "小刘"
stu1.say_hi()

stu2 = Student()
stu2.name = "小明"
stu2.say_hi2("我现在有点想家")
```

###  03-类和对象

1. 类和对象的关系：类是程序中的“设计图纸”，对象是基于图纸生产的具体实体

2. 面向对象编程：适用对象进行编程，即设计类，基于类创建对象，并**使用对象完成具体工作**

   ```python
   class Clock:
       id = None
       price = None
   
       def ring(self):
           import  winsound
           winsound.Beep(2000, 3000)
   
   clock1 = Clock()
   clock1.id = "003032"
   clock1.price = 19.99
   print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
   clock1.ring()
   
   clock2 = Clock()
   clock2.id = "003033"
   clock2.price = 21.99
   print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
   clock2.ring()
   ```


### 04-构造方法

构造方法的作用：

- 构建类对象的时候会**自动运行**
- 构建类对象的传参会传递给构造方法，借此特性可以给**成员变量赋值**

构造方法不要忘记self关键字，在方法内使用成员变量需要使用self

```python
class Student:
    # 构造方法 __init__
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创造了一个类对象")

stu = Student("小明", 23, "12345678910")
print(stu.name)
print(stu.age)
print(stu.tel)
```

**题目**：记录学生的姓名年龄地址3类信息

- 通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入
- 输入完成后，使用print语句完成信息的输出

例如：

当前录入第1位学生信息，总共需录入10位学生信息
请输入学生姓名：小明
请输入学生年龄：23
请输入学生地址：北京
学生1信息录入成功，信息为：【学生姓名：小明, 年龄：23, 地址：北京】
当前录入第2位学生信息，总共需录入10位学生信息

```python
class Student:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add

str_dict = {}

for i in range(10):
    print(f"当前录入第{i+1}位学生信息，总共需录入10位学生信息")
    stu = Student(input("请输入学生姓名："), input("请输入学生年龄："), input("请输入学生地址："))
    str_dict[f"学生{i+1}"] = {}
    str_dict[f"学生{i + 1}"]["姓名"] = stu.name
    str_dict[f"学生{i + 1}"]["年龄"] = stu.age
    str_dict[f"学生{i + 1}"]["地址"] = stu.add
    print(f"学生{i+1}信息录入成功，信息为：【学生姓名：{stu.name}, 年龄：{stu.age}, 地址：{stu.add}】")
```

### 05-魔术方法

```python
__init__ # 构造方法可用于创建类对象的时候设置初始化行为
__str__  # 用于实现类对象转字符串的行为
__lt__   # 用于两个类对象进行小于或大于比较
__le__   # 用于两个类对象进行小于等于或大于等于比较
__eq__   # 用于两个类对象进行相等比较
```

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象，name:{self.name}，age:{self.age}"

    # __lt__魔术方法  小于 大于
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法 小于等于 大于等于
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法 相等
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("小明", 22)
stu2 = Student("小林", 23)
print(stu1)
print(str(stu1))
print(stu1 < stu2)
print(stu1 >= stu2)
print(stu1 == stu2)
```

### 06-封装

**封装**：将现实世界事物在类中描述为属性和方法

**私有成员**：现实事物有部分属性和行为是不公开对使用者开放的，同样在类中描述属性和方法的时候也需要达到这个要求，在类中提供仅供内部使用的属性和方法，而不对外开放

**定义私有成员**：成员变量和成员方法的命名均以__作为开头

+ 类对象无法访问私有成员
+ 类中的其他成员可以访问私有成员

```python
class Phone:

    __current_voltage = 0.5  # 私有成员变量 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电。")

phone = Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)
phone.call_by_5g()
```

**题目**：设计一个手机类，内部包含：

+ 私有成员变量：__is_5g_enable，类型为bool，True表示开启5g，False表示关闭5g
+ 私有成员方法：__check_5g()，会判断私有成员的值
  + 若为True，打印输出：5g开启
  + 若为False，打印输出：5g关闭，使用4g网络
+ 公开成员方法：call_by_5g()，判断5g网络状态

运行结果：5g关闭，使用4g网络

​                    正在通话中

```python
class Phone:

    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()
```

### 07-继承

```python
# 单继承
class 类名(父类名)
    类内容体
```

```python
class Phone:
    IMEI = None    # 序列号
    producer = "HM"    # 厂商

    def call_by_4g(self):
        print("4g通话")
class Phone2022(Phone):
    face_id = "10001"    # 面部识别ID

    def call_by_5g(self):
        print("2022年新功能：5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()
```

```python
# 多继承
class 类名(父类1,父类2，……，父类N)
    类内容体
```

```python
class Phone:
    IMEI = None    # 序列号
    producer = "HM"    # 厂商

    def call_by_4g(self):
        print("4g通话")
class Phone2022(Phone):
    face_id = "10001"    # 面部识别ID

    def call_by_5g(self):
        print("2022年新功能：5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone, NFCReader, RemoteControl):
    pass    # 空的意思 补充语法的完整性

myphone = MyPhone()
myphone.call_by_4g()
myphone.read_card()
myphone.write_card()
myphone.control()
```

多继承注意事项：

+ 同名成员继承 左边优先级最高即先继承的优先级最高

```python
class Phone:
    IMEI = None    # 序列号
    producer = "ITCAST"  # 厂商

    def call_by_5g(self):
        print("父类的5g通话")

class MyPhone(Phone):
    proucer = "ITHEIMA"  # 复写父类属性
    
    def call_by_5g(self):
        print("子类的5g通话")  # 复写父类方法
```

```python
class Phone:
    IMEI = None    # 序列号
    producer = "ITCAST"  # 厂商

    def call_by_5g(self):
        print("父类的5g通话")

class MyPhone(Phone):
    producer = "ITHEIMA"  # 复写父类属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        print("子类的5g通话")  # 复写父类方法
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)
```

调用父类同名成员

+ 直接调用父类成员    父类名.成员变量    父类名.成员方法(self)
+ 使用super()调用父类成员   super().成员变量    super().成员方法()

```python
class Phone:
    IMEI = None    # 序列号
    producer = "ITCAST"  # 厂商

    def call_by_5g(self):
        print("使用5g网络进行通话")

class MyPhone(Phone):
    producer = "ITHEIMA"  # 复写父类属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        #print("使用5g网络进行通话")  # 复写父类方法
        # 方式1
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式2
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)
```

### 08-类型注解

**类型注解**：在代码中设计数据交互之时，对数据类型进行显式的说明：可以帮助

+ PyCharm等开发工具对代码做类型推断协助做代码提示
+ 开发者自身做类型的备注

变量的类型注解语法：

+ 变量: 类型
+ 在注释中，#type: 类型

```python
import json
import random

# 基础数据类型注解
# var_1: int = 10
# var_2: str = "itheima"
# var_3: bool = True
# 类对象类型注解
class Student:
    pass
stu: Student = Student()
# 基础容器类注解
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_dict: dict = {"itheima": 666}
# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "itheima", True)
my_dict: dict[str, int] = {"itheima": 666}
# 在注释中进行注解
var_1 = random.randint(1, 10)  # type:int
var_2 = json.loads('{"name":"zhangsen"}')  # type:dict[str, str]
def func():
    return 10
var_3 = func()  # type:int
# 类型注解的限制
var_4: int = "itheima"  #仅仅为备注 写错不影响程序的运行
```

```python
# 函数（方法）的类型注解
def 函数方法名(形参名: 类型,形参名: 类型,……)
    pass
```

```python
# 对形参进行类型注解
def add(x: int, y: int):
    return x + y
# 对返回值进行类型注解
def func(data: list) -> list:
    return data
```

**Union类型**：定义联合类型注解

使用方式：

+ from typing import Union
+ Union[类型, ……, 类型]

```python
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "itheima", "itcast"]

def func(data: Union[int,str]) -> Union[int, str]:
    pass
```

### 09-多态

多态：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态

抽象类：含有抽象方法的类

抽象方法：方法体是空实现的(pass)称之为抽象方法

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)
```

```python
class AC:
    # 制冷
    def cool_wind(self):
        pass
    # 制热
    def hot_wind(self):
        pass
    # 左右摆风
    def swing_l_r(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

media_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(media_ac)
make_cool(gree_ac)
```

### 10-数据分析案例

1. 设计一个类，可以完成数据的封装
2. 设计一个抽象类，定义文件读取的相关内容，并使用子类实现具体功能
3. 读取文件，产生数据对象
4. 进行数据需求的逻辑计算(计算每一天的销售额)
5. 通过PyEcharts进行图形绘制

```python
# data_define.py
"""
定义数据的类
"""
class Record:

    def __init__(self, date, order_id, money, province):
        self.date = date          # 日期
        self.order_id = order_id  # ID
        self.money = money        # 金额
        self.province = province  # 省份

    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"
    
    
```

```python
# file_define.py
"""
与文件相关的类定义
"""
import json
from data_define import Record

class FileReader:

    def read_data(self) -> list[Record]:
        """读取数据 转化为Record对象 并封装为列表"""
        pass

class TxtFileReader(FileReader):

    def __init__(self, path):
        self.path = path   # 记录文件路径

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path   # 记录文件路径

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    txt_file_reader = TxtFileReader("D:/pycharm_program/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("D:/pycharm_program/2011年2月销售数据JSON.txt")
    list1 = txt_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)
```

```python
# main.py
"""
1. 设计一个类，可以完成数据的封装
2. 设计一个抽象类，定义文件读取的相关内容，并使用子类实现具体功能
3. 读取文件，产生数据对象
4. 进行数据需求的逻辑计算(计算每一天的销售额)
5. 通过PyEcharts进行图形绘制
"""

from data_define import Record
from file_define import FileReader,TxtFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

txt_file_reader = TxtFileReader("D:/pycharm_program/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/pycharm_program/2011年2月销售数据JSON.txt")

data1: list[Record] = txt_file_reader.read_data()
data2: list[Record] = json_file_reader.read_data()

data: list[Record] = data1 + data2

data_dict = {}
for record in data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 可视化
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")
```

### 11-SQL基础语法

```sql
# DDL数据定义 库的创建删除 表的创建删除等
# 查看数据库
SHOW DATABASES;
# 使用数据库
USE 数据库名称
# 创建数据库
CREATE DATABASE 数据库名词 [CHARSET UTF8];
# 删除数据库
DROP DATABASE 数据库名称;
# 查看当前使用的数据库
SELECT DATABASE();
# 查看有哪些表
SHOW TABLES; # 需要先选择数据库
# 创建表
CREATE TABLE 表名称(
	列名称 列类型，
    列名称 列类型，
    …………
);
-- 列类型有
int
float
varchar(长度)   -- 文本，长度为数字 最大限制
date
timestamp
# 删除表
DROP TABLE 表名称;
DROP TABLE IF EXISTS 表名称;
```

```sql
# DML数据操作 数据插入、删除、更新
# 数据插入
INSERT INTO 表[(列1，列2，……，列N)] VALUES(值1，值2，……，值N)[，(值1，值2，……，值N)，……，(值1，值2，……，值N)];
# 数据删除
DELETE FROM 表名称 [WHERE 条件判断];
# 数据更新
UPDATE 表名 SET 列=值 [WHERE 条件判断];
```

```sql
use world;
create table student(
	id int,
	name varchar(10),
	age int
);

insert into student(id) values(1), (2), (3);

insert into student(id, name, age) values(4, '林小栋', 23),(5, '刘小明', 23);

delete from student where id < 4;

update student set name = '林大栋' where id = 4;
```

```sql
# DQL数据查询
SELECT 字段列表|* FROM 表
select id, name, age from student;
select * from student;
SELECT 字段列表|* FROM 表 WHERE 条件判断
select * from student where age > 20;
select * from student where gender = '男';

# DQL分组聚合
SELECT 字段|聚合函数 FROM 表 [WHERE 条件] GROUP BY 列
聚合函数有：
- SUM(列)  求和
- AVG(列)  求平均值
- MIN(列)  求最小值
- MAX(列)  求最大值
- COUNT(列|*)  求数量
select gender, avg(age), sum(age), min(age), max(age), count(*) from student group by gender;

# DQL排序分页
SELECT 列|聚合函数|* FROM 表
WHERE ...
GROUP BY ...
ORDER BY ... [ASC | DESC]
LIMIT n[, m]
select * from student where age > 20 order by age asc; # 升序
select * from student where age > 20 order by age desc; # 降序
select * from student limit 5; # 限制 只出现5条信息
select * from student limit 10, 5; # 从第10条之后开始往后数5条
select age, count(*) from student where age > 20 group by age
order by age limit 3;
```

```python
# 获取MySQL数据库的链接对象
from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="280015",
)

# print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()  # 获取游标对象
# 选择数据库
conn.select_db("world")
# 执行sql
# cursor.execute("create table test_pymysql(id int)")
cursor.execute("select * from student")

results = cursor.fetchall()
for i in results:
    print(i)
# 关闭数据库链接
conn.close()
```

```python
# pymysql库在执行对数据库有修改操作的行为时，需要通过链接对象的commmit成员方法来确认
from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="280015",
    autocommit=True
)

cursor = conn.cursor()  # 获取游标对象
# 选择数据库
conn.select_db("world")
# 执行sql
cursor.execute("insert into student values(10001, '周杰伦', 31)")
# 关闭数据库链接
conn.close()
```

```python
# 练习从数据库读取列表并转化为json文件保存
import json
from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="280015",
    autocommit=True
)

cursor = conn.cursor()
conn.select_db("py_sql")
cursor.execute("select * from orders")
r = cursor.fetchall()

f = open("D:/pycharm_program/第2章-12.txt", 'w', encoding='UTF-8')
data_dict = {}
for i in r:
    data_dict["date"] = str(i[0])
    data_dict["id"] = i[1]
    data_dict["money"] = int(i[2])
    data_dict["province"] = i[3]
    f.write(json.dumps(data_dict, ensure_ascii=False)) # 将python对象转化为json对象
    f.write("\n")

f.close()
conn.close()
```


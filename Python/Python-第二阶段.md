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


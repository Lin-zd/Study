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

for i in range(10):
    print(f"当前录入第{i+1}位学生信息，总共需录入10位学生信息")
    stu = Student(input("请输入学生姓名："), input("请输入学生年龄："), input("请输入学生地址："))
    print(f"学生{i+1}信息录入成功，信息为：【学生姓名：{stu.name}, 年龄：{stu.age}, 地址：{stu.add}】")
```


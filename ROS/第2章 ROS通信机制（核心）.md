# 第2章 ROS通信机制（核心）

**ROS是进程（也称为Nodes）的分布式框架。** 

不同主机之间协同工作，但是不同主机如何通信和不同进程如何实现数据交换？——通信机制

#### ROS基本通信的三种实现策略：

- 话题通信(发布订阅模式)
- 服务通信(请求响应模式)
- 参数服务器(参数共享模式)

#### 章节目标：

- 能够熟练介绍ROS中常用的通信机制
- 能够理解ROS中每种通信机制的理论模型
- 能够以代码的方式实现各种通信机制对应的案例
- 能够熟练使用ROS中的一些操作命令
- 能够独立完成相关实操案例

## 2.1 话题通信

### 2.1.1 话题通信的理论模型

![image-20221015184235300](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20221015184235300.png)

### 2.2.2 话题通信基本操作（C++）

发布方 接收方 数据

编写流程：1.编写发布方实现；2.编写订阅方实现；3.编辑配置文件；4.编译并执行。

#### 1.发布方实现流程（C++/Python）

```c++
#include "ros/ros.h"
#include "std_msgs/String.h"
/*
    发布方实现:
        1.包含头文件;
          ROS中文文本类型——>std_msgs/String.h
        2.初始化 ROS 节点;
        3.创建节点句柄;
        4.创建发布者对象;
        5.编写发布逻辑并发布数据。
*/

int main(int argc, char *argv[])
{
    //2.初始化ROS节点;
    ros::init(argc,argv,"erGouZi");
    //3.创建节点句柄；
    ros::NodeHandle nh;
    //4.创建发布者对象
    ros::Publisher pub = nh.advertise<std_msgs::String>("fang",10);
    //5.编写发布逻辑并发布数据
    //先创建被发布的消息
    std_msgs::String msg;
    //编写循环 循环中发布数据
    while (ros::ok())
    {
        msg.data = "hello";
        pub.publish(msg);
    }

return 0;

}
```



```python
#! /usr/bin/env python

import rospy
from std_msgs.msg import String #发布的消息类型

""" 
   使用 Python 实现消息发布：
       1.导包;
       2.初始化ROS节点;
       3.创建发布者对象;
       4.编写发布逻辑并发布消息;

"""

if __name__ == "__main__":
# 2.初始化ROS节点;
rospy.init_node("sanDai") #传入节点名称
# 3.创建发布者对象;
pub = rospy.Publisher("che",String,queue_size=10)
# 4.编写发布逻辑并发布消息;
# 创建数据
msg = String()
#指定发布者对象
rate = rospy.Rate(1)
#设置计数器
count = 0
#使用循环发布数据
rospy.sleep(3)
while not rospy.is_shutdown():
    count += 1
    msg.data = "hello" + str(count)
    #发布数据
    pub.publish(msg)
    rospy.loginfo("发布的数据：%s",msg.data)
    rate.sleep()
```

Python文件需要先赋予执行权限 chmod +x *.py

编译CMakeLists文件

roscore启动ros核心 

cd demo03_ws 

C++ 需要 catkin_make

source ./devel/setup.bash

rosrun plumbing_pub_sub demo01_pub/demo01_pub_p.py

验证 rostopic echo fang

#### 2.订阅方实现流程（C++/Python）

```c++
#include "ros/ros.h"
#include "std_msgs/String.h"

/* 
    订阅方实现:
        1.包含头文件;
          ROS中文本类型 --> String
        2.初始化 ROS 节点;
        3.创建节点句柄;
        4.创建订阅者对象;
        5.处理订阅的信息（回调函数);
        6.设置循环调用回调函数。
 */

void doMsg(const std_msgs::String::ConstPtr &msg){
    //通过msg获取并操作订阅到的数据
    ROS_INFO("翠花订阅到的数据：%s",msg->data.c_str());
}
int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    // 2.初始化 ROS 节点
    ros::init(argc,argv,"cuiHua");
    // 3.创建节点句柄
    ros::NodeHandle nh;
    // 4.创建订阅者对象
    ros::Subscriber sub = nh.subscribe<>("fang",10,doMsg);
    // 5.处理订阅的信息

    // 6. 设置循环调用回调函数
    ros::spin();
    
    
    return 0;
}
    
```



```python
#! /usr/bin/env python
import rospy
from std_msgs.msg import String

""" 
    订阅实现流程：
        1.导包
        2.初始化ROS节点
        3.创建订阅者对象
        4.回调函数处理数据
        5.spin()

"""

def doMsg(msg):
    rospy.loginfo("订阅的数据：%s",msg.data)

if __name__ == "__main__":

# 2.初始化ROS节点
rospy.init_node("huaHua")
# 3.创建订阅者对象
sub = rospy.Subscriber("che",String,doMsg,queue_size=10)
# 4.回调函数处理数据
# 5.spin()
rospy.spin()
```



#### 3. 话题通讯自定义消息

流程：按照固定格式创建msg文件；编辑配置文件；编译生成可以被C++/Python调用的中间文件

3.1 定义msg文件

在功能包下新建msg文件夹，添加msg文件

```c++
string name
int32 age
float32 height
```

3.2 编辑配置文件

在package.xml中添加编译依赖与执行依赖

```c++
  <build_depend>message_generation</build_depend>
  <exec_depend>message_runtime</exec_depend>
  <!-- 
  exce_depend 以前对应的是 run_depend 现在非法
  -->
```

在CMakeLists.txt编辑msg相关配置

```c++
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

# 需要加入 message_generation,必须有 std_msgs
    
## 配置 msg 源文件
add_message_files(
  FILES
  Person.msg
)
    
# 生成消息时依赖于 std_msgs
generate_messages(
  DEPENDENCIES
  std_msgs
)

#执行时依赖
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES demo02_talker_listener
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
#  DEPENDS system_lib
)
```

3.3 编译CMakeLists文件

编译 查看C++和Python所需要的调用的中间文件

3.4 发布方实现

```c++
#include "ros/ros.h"
#include "plumbing_pub_sub/Person.h"

/* 
    发布方实现：
        1.包含头文件
          #include "plumbing_pub_sub/Person.h"
        2.初始化ROS节点
        3.创建ROS句柄
        4.创建发布者对象
        5.编写发布逻辑并发布数据

*/

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ROS_INFO("这是消息的发布方");
    /* code */
    // 2.初始化ROS节点
    ros::init(argc,argv,"banZhuRen");
    // 3.创建ROS句柄
    ros::NodeHandle nh;
    // 4.创建发布者对象
    ros::Publisher pub = nh.advertise<plumbing_pub_sub::Person>("liaotian",10);
    // 5.编写发布逻辑并发布数据
    //5-1 创建被发布的数据
    plumbing_pub_sub::Person person;
    person.name = "张三";
    person.age = 0;
    person.height = 1.73;
    //5-2 设置发布频率
    ros::Rate rate(1);
    //5-3 循环发布数据
    while (ros::ok())
    {
      //修改被发布的数据
      person.age += 1;
      //核心：数据发布
      pub.publish(person);
      ROS_INFO("发布的消息：%s,%d,%.2f",person.name.c_str(),person.age,person.height);
      // 休眠
      rate.sleep();
      // 建议
      ros::spinOnce();
    }
    return 0;
}

```



```python
#! /usr/bin/env python
import rospy
from plumbing_pub_sub.msg import Person
"""  
    发布方：发布人的消息
        1.导包
        2.初始化ROS节点
        3.创建发布者对象
        4.组织发布逻辑并发布数据 

"""
if __name__ == "___main__":

    # 2.初始化ROS节点
    rospy.init_node("daMa")
    # 3.创建发布者对象
    pub = rospy.Publisher("jiaoSheTou",Person,queue_size=10)
    # 4.组织发布逻辑并发布数据
    # 4.1 创建Person数据
    p = Person()
    p.name = "奥特曼"
    p.age = 8
    p.height = 1.85
    # 4.2 创建Rate对象
    rate = rospy.Rate(1)
    # 4.3 循环发布数据
    while not rospy.is_shutdown():
        pub.publish(p)
        rospy.loginfo("发布的消息，%s,%d,%.2f",p.name,p.age,p.height)
        rate.sleep()
```

3.5 订阅方实现

```C++
#include "ros/ros.h"
#include "plumbing_pub_sub/Person.h"
/* 
    订阅方实现：
        1.包含头文件
          #include "plumbing_pub_sub/Person.h"
        2.初始化ROS节点
        3.创建ROS句柄
        4.创建订阅者对象
        5.编写回调函数处理订阅的数据
        6.调用spin()函数

*/

void doPerson(const plumbing_pub_sub::Person::ConstPtr& person){
    ROS_INFO("订阅的人的信息：%s,%d,%.2f",person->name.c_str(),person->age,person->height);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ROS_INFO("订阅方接受的消息");
    //2.初始化ROS节点
    ros::init(argc,argv,"jiaZhang");
    // 3.创建ROS句柄
    ros::NodeHandle nh;
    // 4.创建订阅者对象
    ros::Subscriber sub = nh.subscribe("liaotian",10,doPerson);
    // 5.编写回调函数处理订阅的数据

    // 6.调用spin()函数
    ros::spin();
    return 0;
}

```



```python
#! /usr/bin/env python
import rospy
from plumbing_pub_sub.msg import Person

"""  
    订阅方：订阅人的消息
        1.导包
        2.初始化ROS节点
        3.创建订阅者对象
        4.回调函数处理订阅数据
        5.spin()函数
"""

def doPerson(p):
    rospy.loginfo("小伙子的数据:%s,%d,%.2f",p.name,p.age,p.height)

if __name__ == "__main__":
    
    # 2.初始化ROS节点
    rospy.init_node("daYe")
    # 3.创建订阅者对象
    sub = rospy.Subscriber("jiaoSheTou",Person,doPerson,queue_size=10)
    # 4.回调函数处理订阅数据
    # 5.spin()函数
    rospy.spin()
```

**问题遗留**：话题通讯自定义msg Python 未实现

2023.01.29 问题已解决 先赋予python文件执行权限 再编辑CMakeLists文件

## 2.2 服务通信

### 服务通讯

#### 服务通讯理论模型

角色--->流程--->注意

角色：

1. master 管理者（114平台）

2. Server 服务端（服务公司）

3. Client 客户端（我）

流程：

master会根据话题实现Sever和Client的连接

注意：

1.保证顺序，客户端发起请求时，保证服务端已经启动了；（话题通信则无要求）

2.客户端和服务端均可以存在多个。

关注点：

0. 流程已经封装直接调用即可
1. 话题
2. 服务端
3. 客户端
4. 数据载体

![image-20230129193844488](C:\Users\Lin\AppData\Roaming\Typora\typora-user-images\image-20230129193844488.png)

### 服务通信自定义srv

srv = 请求 + 响应

流程：

srv文件内的可用数据类型与msg文件一致，实现流程类似

1. 按照固定格式创建srv文件
2. 编辑配置文件
3. 编译生成中间文件

#### 定义srv文件

服务通信中，数据分成两部分，请求与响应，在 srv 文件中请求和响应使用`---`分割，具体实现如下:

功能包下新建 srv 目录，添加 xxx.srv 文件

```c++
# 客户端请求时发送的两个数字
int32 num1
int32 num2
---
# 服务器响应发送的数据
int32 sum

```

#### 编辑配置文件

**package.xml**中添加编译依赖与执行依赖

```c++
  <build_depend>message_generation</build_depend>
  <exec_depend>message_runtime</exec_depend>
  <!-- 
  exce_depend 以前对应的是 run_depend 现在非法
  -->

```

**CMakeLists.txt**编辑 srv 相关配置

```c++
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)
# 需要加入 message_generation,必须有 std_msgs

add_service_files(
  FILES
  AddInts.srv
)
    
generate_messages(
  DEPENDENCIES
  std_msgs
)

```

注意: 官网没有在 catkin_package 中配置 message_runtime,经测试配置也可以

#### 编译

编译生成中间文件

C++ 需要调用的中间文件(.../工作空间/devel/include/包名/xxx.h)

Python 需要调用的中间文件(.../工作空间/devel/lib/python3/dist-packages/包名/srv)

### 服务通信自定义srv调用（C++/Python）

vscode配置 与 话题通信配置相同

#### 服务端

服务端实现：解析客户端提交的数据，并运算在产生相应

C++实现流程：

1. 包含头文件
2. 初始化ROS节点
3. 创建节点句柄
4. 创建一个服务对象
5. 处理请求并产生响应
6. spin()

```c++
#include "ros/ros.h"
```



```python
import rospy
```



#### 客户端

C++实现流程：

1. 包含头文件
2. 初始化ROS节点
3. 创建节点句柄
4. 创建一个客户端对象
5. 提交请求并处理响应



## 2.3 参数服务器



## 2.4 常用命令



## 2.5 通信机制实操



## 2.6 通信机制比较



## 2.7 本章小结
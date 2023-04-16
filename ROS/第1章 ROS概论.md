# 第1章 ROS概论

章节目标：

- 了解 ROS 概念、设计目标以及发展历程
- 能够独立安装并运行 ROS
- 能够使用 C++ 或 Python 实现 ROS 版本的 HelloWorld
- 能够搭建 ROS 的集成开发环境
- 了解 ROS 架构设计

## 1.1 ROS简介

### 1.1.1 ROS概念

**ROS，Robot Operating System(机器人操作系统)**

ROS为适用于机器人的**开源元操作系统**；集成了大量的工具、库、协议等，简化了对机器人的控制；还提供了用于多台计算机上获取、构建、编写和运行代码的工具和库，类似与一种“机器人框架”。

ROS = Plumbing + Tools + Capabilities + Ecosystem

即 **通讯机制**、工具软件包、机器人高层技能以及机器人生态系统的集合体

另附：[ROS: Home](https://www.ros.org/)

### 1.1.2 ROS设计目标

1、代码复用

2、分布式 

3、松耦合

4、精简

5、语言独立性：C++   Python

6、易于测试

7、大型应用

8、丰富的组件化工具

9、免费且开源

### 1.1.3 ROS发展历程

2007年，由柳树车库（Willow Garage）提出，再大家共同的努力下，逐渐得以完善

2010——2022 目前最新的ROS版本为noetic，python3（之前的版本支持仅支持python2）

tips：ROS各版本软件首字母命名为从B、C、D……N

## 1.2 ROS安装

安装虚拟机（VMware16，公众号：软件管家）

安装ubuntu系统（版本为20.04.5）

安装ROS

测试ROS

具体安装教程可参考bilibili或者CSDN

## 1.3 ROS HelloWrold实现

ROS编程例程：

创建工作空间——创建功能包——编辑源文件——编辑配置文件——编译执行

1、创建工作空间

```c++
mkdir -p 自定义空间名称/src    //（例：mkdirt -p demo01_ws/src）
cd 自定义空间名称
catkin_make
```

2、进入SRC创建ROS包并添加依赖

```c++
cd src
catkin_create_pkg 自定义ROS包名 roscpp rospy std_msgs
//例：carkin_create_pkg helloworld roscpp rospy std_msgs
```

### 1.3.1 C++

3、编辑C++源文件

1）首先进入上一步所创建的helloworld文件夹中的src目录，编写相应的C++源文件（创建txt文件将后缀修改为.cpp文件即可），具体代码如下：

```c++
 //1、包含ros头文件
#include “ros/ros.h”
//2、编写main函数
int main(int argc, char *argv[]){
         //3.初始化ros节点
         ros::init(argc, argv, "hello_node");
         //4.输出日志
         ROS_INFO("hello world!");
         return 0;
}
```

2）然后编辑helloworld文件夹下的Cmakelist.txt文件，去掉第136行及第149-151行注释

```c++
add_executable(步骤3的源文件名src/步骤3的源文件名.cpp)

target_link_libraries(步骤3的源文件名
  ${catkin_LIBRARIES}
)

//例如：
add_executable(haha src/helloworld_c.cpp)

target_link_libraries(haha
  ${catkin_LIBRARIES}
)
```

3）进入工作空间目标并编译

```c++
cd 自定义空间名称   //（例如：cd demo01_ws）

catkin_make
```

生成bulid devel等文件夹

4）执行

```c++
启动命令行1（Ctrl+Alt+T）:

roscore

启动命令行2：

cd 工作空间    //（例如：cd demo01_ws）

source ./devel/setup.bash

rosrun 功能包名  C++节点    //（例如：rosrun helloworld haha）
```

### 1.3.2 Python

1）在ros功能包下添加scripts文件夹，新建python源文件

```python
cd ros功能包名     #例如：cd helloworld

mkdir scripts
```

新建python源文件

```python
#！ /usr/bin/env python
##指定解释器

#1.导包
import rospy

#2.编写主入口
if __name__ == "__main__":
       #3.初始化 ROS 节点
       rospy.init_node("hello_p")
       #4.输出日志
       rospy.loginfo("hello world! by python");
```

2）添加python文件的可执行权限

chmod +x 自定义文件名.py    #例如：chmod +x helloworld_p.py

3）编辑ros功能包下的Cmakelist.txt文件

去掉其第162—165行的注释

```python
catkin_install_python(PROGRAMS scripts/自定义文件名.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

剩下的步骤同C++实现过程中的3、4两步相同

## 1.4 ROS集成开发环境搭建

### 1.4.1 安装终端 Terminator

```
sudo apt install terminator
```

另附 常用快捷键

```
Alt+Up                          //移动到上面的终端
Alt+Down                        //移动到下面的终端
Alt+Left                        //移动到左边的终端
Alt+Right                       //移动到右边的终端
Ctrl+Shift+O                    //水平分割终端
Ctrl+Shift+E                    //垂直分割终端
Ctrl+Shift+Right                //在垂直分割的终端中将分割条向右移动
Ctrl+Shift+Left                 //在垂直分割的终端中将分割条向左移动
Ctrl+Shift+Up                   //在水平分割的终端中将分割条向上移动
Ctrl+Shift+Down                 //在水平分割的终端中将分割条向下移动
Ctrl+Shift+S                    //隐藏/显示滚动条
Ctrl+Shift+F                    //搜索
Ctrl+Shift+C                    //复制选中的内容到剪贴板
Ctrl+Shift+V                    //粘贴剪贴板的内容到此处
Ctrl+Shift+W                    //关闭当前终端
Ctrl+Shift+Q                    //退出当前窗口，当前窗口的所有终端都将被关闭
Ctrl+Shift+X                    //最大化显示当前终端
Ctrl+Shift+Z                    //最大化显示当前终端并使字体放大
Ctrl+Shift+N or Ctrl+Tab        //移动到下一个终端
Ctrl+Shift+P or Ctrl+Shift+Tab  //Crtl+Shift+Tab 移动到之前的一个终端
```

```
F11                             //全屏开关
Ctrl+Shift+T                    //打开一个新的标签
Ctrl+PageDown                   //移动到下一个标签
Ctrl+PageUp                     //移动到上一个标签
Ctrl+Shift+PageDown             //将当前标签与其后一个标签交换位置
Ctrl+Shift+PageUp               //将当前标签与其前一个标签交换位置
Ctrl+Plus (+)                   //增大字体
Ctrl+Minus (-)                  //减小字体
Ctrl+Zero (0)                   //恢复字体到原始大小
Ctrl+Shift+R                    //重置终端状态
Ctrl+Shift+G                    //重置终端状态并clear屏幕
Super+g                         //绑定所有的终端，以便向一个输入能够输入到所有的终端
Super+Shift+G                   //解除绑定
Super+t                         //绑定当前标签的所有终端，向一个终端输入的内容会自动输入到其他终端
Super+Shift+T                   //解除绑定
Ctrl+Shift+I                    //打开一个窗口，新窗口与原来的窗口使用同一个进程
Super+i                         //打开一个新窗口，新窗口与原来的窗口使用不同的进程
```

### 1.4.2 安装VScode

具体安装过程可参考bilibili或CSDN

如何使用VScode软件实现ros下的hellowrold输出 可 参考bilibli ros教程相关视频（赵虚左老师）

### 1.4.3 launch文件

为实现一次性启动多个节点

1. 选定功能包右击 ---> 添加 launch 文件夹

2. 选定 launch 文件夹右击 ---> 添加 launch 文件

3. 编辑 launch 文件内容

   ```
   <launch>
       <node pkg="helloworld" type="demo_hello" name="hello" output="screen" />
       <node pkg="turtlesim" type="turtlesim_node" name="t1"/>
       <node pkg="turtlesim" type="turtle_teleop_key" name="key1" />
   </launch>
   ```

   node ---> 包含的某个节点

   pkg -----> 功能包

   type ----> 被运行的节点文件

   name --> 为节点命名

   output-> 设置日志的输出目标

4. 运行 launch 文件

   `roslaunch 包名 launch文件名`

5. 运行结果: 一次性启动了多个节点

## 1.5 ROS架构

1.5.1 ROS文件系统

![image-20221013134018361](C:\Users\Y7000P\AppData\Roaming\Typora\typora-user-images\image-20221013134018361.png)

WorkSpace --- 自定义的工作空间

    |--- build:编译空间，用于存放CMake和catkin的缓存信息、配置信息和其他中间文件。
    
    |--- devel:开发空间，用于存放编译后生成的目标文件，包括头文件、动态&静态链接库、可执行文件等。
    
    |--- src: 源码
    
        |-- package：功能包(ROS基本单元)包含多个节点、库与配置文件，包名所有字母小写，只能由字母、数字与下划线组成
    
            |-- CMakeLists.txt 配置编译规则，比如源文件、依赖项、目标文件
    
            |-- package.xml 包信息，比如:包名、版本、作者、依赖项...(以前版本是 manifest.xml)
    
            |-- scripts 存储python文件
    
            |-- src 存储C++源文件
    
            |-- include 头文件
    
            |-- msg 消息通信格式文件
    
            |-- srv 服务通信格式文件
    
            |-- action 动作格式文件
    
            |-- launch 可一次性运行多个节点 
    
            |-- config 配置信息
    
        |-- CMakeLists.txt: 编译的基本配置

1.package.xml

该文件定义有关软件包的属性，例如软件包名称，版本号，作者，维护者以及对其他catkin软件包的依赖性。请注意，该概念类似于旧版 rosbuild 构建系统中使用的*manifest.xml*文件

2.CMakelists.txt

文件**CMakeLists.txt**是CMake构建系统的输入，用于构建软件包。任何兼容CMake的软件包都包含一个或多个CMakeLists.txt文件，这些文件描述了如何构建代码以及将代码安装到何处。

### 1.5.2 ROS文件系统相关命令

1.增

catkin_create_pkg 自定义包名 依赖包 === 创建新的ROS功能包

sudo apt install xxx === 安装 ROS功能包

2.删

sudo apt purge xxx ==== 删除某个功能包

3.查

rospack list === 列出所有功能包

rospack find 包名 === 查找某个功能包是否存在，如果存在返回安装路径

roscd 包名 === 进入某个功能包

rosls 包名 === 列出某个包下的文件

apt search xxx === 搜索某个功能包

4.改

rosed 包名 文件名 === 修改功能包文件

需要安装 vim

**例如:**rosed turtlesim Color.msg

### 1.5.3 ROS计算图

rqt_graph能够创建一个显示当前系统运行情况的动态图形。ROS 分布式系统中不同进程需要进行数据交互，计算图可以以点对点的网络形式表现数据交互过程。rqt_graph是rqt程序包中的一部分。

如果前期把所有的功能包（package）都已经安装完成，则直接在终端窗口中输入

```
rosrun rqt_graph rqt_graph
```

如果未安装则在终端（terminal）中输入

```
$ sudo apt install ros-<distro>-rqt
$ sudo apt install ros-<distro>-rqt-common-plugins
```

请使用你的ROS版本名称（比如:kinetic、melodic、Noetic等）来替换掉<distro>。

例如当前版本是 Noetic,就在终端窗口中输入

```
$ sudo apt install ros-noetic-rqt
$ sudo apt install ros-noetic-rqt-common-plugins
```

### 1.6 本章小结

**2022.10.13** ROS第1章学习完成，了解了ROS的相关概念及功能、发展历史等基础知识，实现了虚拟机、ROS、VScode等软件的安装，搭建了相关环境并动手实现了ROS下的C++和Python两种编程语言的helloworld输出，对ROS实现架构有了初步地了解。
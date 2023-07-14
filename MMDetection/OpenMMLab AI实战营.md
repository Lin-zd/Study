# OpenMMLab AI实战营

## 2023.05.31

### 二十分钟入门计算机视觉开源神器OpenMMLab笔记

MMDetection：目标检测  实例分割  全景分割

MMYOLO：YOLOV1--YOLOV8

MMOCR：文本检测  文本识别  关键信息提取

MMDetection3D：无人驾驶  3D目标检测

MMRotate：旋转目标检测  小众研究领域

MMsegmentation：语义分割

MMPretrain：图像分类+预训练+多模态算法库

MMPose：姿态估计  关键点检测

MMHuman3D：三维人体姿态估计算法库

MMAction2：视频动作识别算法库

MMagic：生成模型+底层视觉+AIGC算法库

MMDeploy：模型部署工具箱

Playground：趣味应用游乐场

## 2023.06.01

### 人体关键点检测与MMPose笔记

**个人研究方向与其关联较小 仅作为知识面扩充 了解即可**

**2D姿态估计**：在图像上定位人体关键点(臀部、颈部、手、腿等)的坐标

基于回归：回归关键点坐标-->深度模型回归困难 精度非最优

基于热力图：预测关键点位置-->模型精度更高

热力图训练流程：

1. 关键点标注 得到真之热力图
2. 输入图像 预测模型 预测热力图
3. 将1 2 步骤的记过进行逐点对比计算损失

如何从热力图中还原关键点位置：

1. 朴素方法：求热力图最大值位置
2. 归一化热力图形成点位于不同位置的概论，再计算位置的期望 优点：连续可微

**多人姿态估计**：

自顶向下：

1. 使用目标检测算法检测出每个人体
2. 基于单人图像估计每个人的姿态
3. 精度受限 速度与计算量正比于人数

自底向上：

1. 使用关键点模型检测出所有人体关键点
2. 基于位置关系或其他辅助信息将关键点组合成不同的人
3. 推理速度与人数无关

自顶向下方法：DeepPose RLE Hourglass Simple Baseline HRNet

自底向上方法：Part Affinity Fields&OpenPose

单阶段方法：SPM SPR

基于Transformer的方法:：PRTR TokenPose

**3D姿态估计**：预测空间点坐标

直接预测 利用视频信息 利用多视角图像

Coarse-to-fine prediction

Simple Baseline 3D

VideoPose3D

VideoPose3D

**评价指标**：PDP PDJ PCK OKS

**人体参数化模型**：SMPL SMPLify HMR

## 2023.06.02

### MMPose代码实战笔记 

了解

安装MMPose torch 1.10.1+cu113 torchvision 0.11.2+cu113 torchvision 0.10.1+cu113 

用MIM安装MMCV mmcv 2.0.0rc3 mmdet ≥3.0.0rc6 

安装其他工具包 opencv-python pillow matplotlib seaborn tqdm pycocotools 

下载并安装MMPose MMDetection 

下载预训练模型权重文件和视频素材 

检查安装成功 

MMPose预训练模型预测 命令行 本地安装调用摄像头检测 

三角板目标检测 

加载数据集 下载权重 训练测试 预测 

关键点检测 

下载配置文件 训练 预测

## 2023.06.06

### 深度学习预训练与MMPreTrain笔记

MMPretrain 一个全新升级得预训练开源算法框架 提供各种预训练主干网络 支持不同的预训练策略

+ 主干模型：VGG  ResNet  DenseNet  EfficientNet ConvNeXt  Vit   SwinTransformer等
+ 自监督学习：MoCo v1/v2/v3  SimCLR等
+ 多模态学习：CLIP  BLIP/BLIP-2
+ 数据集支持：MNIST/CIFAR  ImageNet  COCO等
+ 训练技巧与策略：优化器与学习率策略  数据增强策略
+ 易用性

Python推理API：图像分类 图像描述 视觉问答 视觉定位  检索

环境搭建步骤：

```shell
# 基础安装
conda create -n open-mmlab python=3.8
pytorch==1.10.1  torchvision==0.11.2  cudatoolkit=11.3 -c -y
conda activate open-mmlab
pip install openmim
git clone http://github.com/open-mmlab/mmpretrain.git
cd mmpretrain
mim install -e.
# 多模态依赖
mim install -e".[multimodal]"
```

深度学习模型的训练设计的几个方面：

- 模型结构：模型多少层 每层通道数等
- 数据：数据集划分 数据文件路径 批大小 数据增强策略等
- 训练优化：梯度下降算法 学习率参数 训练总轮次 学习率变化策略等
- 运行：GPU、分布式环境配置等
- 辅助功能：打印日志 定时保存checkpoint等

数据-->数据读取，数据增强等操作-->模型输入-->计算损失-->优化 梯度反向传播-->模型输出预测结果

ResNet 

Vision Transformer

注意力机制

自监督学习 SimCLR  MAE

多模态算法 CLIP  BLIP  BLIP-2等

## 2023.06.07

### MMPretrain代码实战笔记

```shell
conda activate mmpre
python 8.13.2 torch 2.0.1
```

```shell
git clone git clone http://github.com/open-mmlab/mmpretrain.git
pip install openmim
mim --help
mim install -e".[multimodal]"
```

图像推理  mmpre 1.0.0rc8

预训练模型  模型推理 inferencxe_model  需要加载预训练权重

微调训练

数据集获取：猫狗图像数据集

```python
# 配置文件解读
_base_ = [  ] # 继承 
type    backbone    neck    head
```

 pipeline

规划配置

运行参数配置  一般不需要修改   logger 日志打印  checkpoint  权重保存（max_keep_ckpts = 5  save_best='auto'）  随机种子 randomness（seed = True）

mim train mmpretrain 配置文件.py  --work-dir=保存结果路径

mim test mmpretrain 权重文件.py  --checkpoint    --out result.pkl

## 2023.06.08

### 目标检测与MMDetection笔记

目标检测的基本范式

+ 滑窗：设置一个固定大小的窗口，遍历图像所有位置，所到之处用分类模型识别窗口中的内容    计算成本较高
  + 改进思路：分析滑窗中的重复计算-->用卷积一次性计算所有特征，再取出对应位置的特征完成分类

感受野：神经网路中，一个神经元能够“看到”的原图的区域

对于3*3卷积 pad=1的卷积所堆叠的模型  感受野中心=神经元特征图上的坐标×感受野的步长(特征图尺寸的缩减倍数，即多所有stride的累积)

有效感受野：中心敏感 边缘不敏感

+ 使用卷积实现密集预测：借助卷积高效实现滑窗

边界框回归    基于锚框    无锚框

非极大值抑制：仅保存置信度最高的检测框    贪心算法 

置信度：模型认可自身预测结果的程度

+ 锚框：在原图上设置不同尺寸的基准框

图像金字塔：算法不经过改动即可适应不同尺度的物体，但是计算成本成倍增加

基于层次化特征：计算成本低 低层特征抽象级别不够 预测困难

+ 多尺度检测与FPN

特征金字塔：高层次特征包括足够抽象语义信息，将高层特征融入低层特征，补充低层语义特征  融合方法：特征求和

单阶段&无锚框检测器选讲

+ RPN
+ YOLO、SSD
+ Focal Loss与RetinaNet
+ FCOS
+ YOLO系列选讲

## 2023.06.09

### MMDetectiin代码实战笔记

流程: 

1.数据集准备和可视化 

2.自定义配置文件 

3.训练前可视化验证 

4.模型训练 

5.模型测试和推理 

6.可视化分析 

环境检测和安装 nvcc -V    gcc -version    python 3.10 

安装mmengine和mmcv依赖   限制版本 环境信息

收集和打印 数据集下载得到猫的数据集 

可视化数据集  coco可视化 自定义配置文件 

训练前可视化验证 数据流没问题开始训练 模型测试和推理 可视化分析

## 2023.06.13

### 语义分割与MMSegmentation笔记

语义分割：：仅考虑像素的类别 不分割同一类的不同实体

实例分割：分割不同的实体 仅考虑前景物体

全景分割：背景仅考虑类别 前景需要区分实体

基本思路：按颜色分割-->逐像素分类

复用卷积计算  全连接层的卷积化

2015 全卷积网络 FCN    基于多层级特征的上采样

2015 UNet  逐级融合高低层次特征

上下文信息  根据图像周围内容进行判断

2016 PSPNet 多尺度池化得到不同尺度的上下文特征

DeepLab系列  空洞卷积  解决下采样问题

条件随机场  后处理手段  

空间金字塔池化

语义分割前沿算法

SegFormer

K-Net：统一分割任务

MaskFormer

Mask2Former

SAM

语义分割模型评估：基于交并集的评估指标

## 2023.06.14

### MMSegmentation代码课笔记

环境配置 torch 1.10.1+cu113

安装 openmim  mmengine  mmcv==2.0.0rc4

安装 opencv-python pillow matplotlib seaborn tqdm pytorch-lightning

安装 MMSegementation

创建checkpoint文件夹存放预训练模型权重

创建outputs文件夹用于存放预测结果

创建data文件夹用于存放图片和视频素材

1. 下载权重文件至checkpoint
2. 下载data
3. 设置plot中文字体

预训练语义分割模型预测-单张图像-命令行/Python API

 预训练语义分割模型预测-视频

## 2023.06.15

### 底层视觉与MMEditing笔记

图像超分辨率Super Resolution：

根据从低分辨率图像重构高分辨率图像

目标：提高图像分辨率；高分辨率符合低分图像的内容；恢复图像的细节、产生真实的内容

经典方法：稀疏编码 Sparse Coding

+ 基于卷积网络的模型SRCNN与FSRCNN
  + SRCNN首个基于深度学习的超分辨率算法 证明了深度学习在底层视觉的可行性
  + 模型由三层卷基层构成，可以端到端学习，不需要额外的前后处理步骤
  + 第一层 提取图像块的低层次局部特征
  + 第二层 对低层次局部特征进行非线性变换，得到高层次特征
  + 组合邻域内的高层次特征，恢复高清图像
  + FSRCNN在SRCNN上的基础上对速度进行了提升

+ 损失函数：感知损失和均方误差
+ 对抗生成网络GAN：基于神经网络的无监督学习模型
+ 基于GAN的模型SRGAN与ESRGAN
+ 视频超分辨率

可变形卷积 Deformable Convolution

在可变形卷积中具有增加的偏移量使此案样位置能够灵活变化 获得更丰富的信息

### MMagic代码课笔记

环境配置 pytorch 1.10.1+cu113 mmcv mmengine mmagic  pip3 install -e .

安装其他工具包 opencv-python pillow matplotlib seaborn tqdm

黑白老照片上色

文生图  Stable Diffusion 扩散模型    DreamBooth

图生图

训练自己的ControlNet

进入MMagic主目录    下载数据集   训练

```shell
！bash tools/dist_train.sh configs/controlnet/controlnet-1xb1-demo_dataset 1
```

ControlNet/docs/train.md

数据集    咒语  通过扩散模型  生成图

监督学习

突然收敛现象    涌现    量变到质变

OpenXLab应用中心AIGC在线Demo

beta.openxlab.org.cn

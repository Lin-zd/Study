import torch
import torchvision
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

train_set = torchvision.datasets.MNIST(root='./dataset/mnist', train=True, download=True)
test_set = torchvision.datasets.MNIST(root='./dataset/mnist', train=False, download=True)
# train_set = torchvision.datasets.CIFAR10(root='./dataset/cifar10', train=True, download=True)
# test_set = torchvision.datasets.CIFAR10(root='./dataset/cifar10', train=False, download=True)

x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[0], [0], [1]])

class LogisticRegressionModel(torch.nn.Module):
    # 构造函数 初始化对象
    def __init__(self):
        super(LogisticRegressionModel, self).__init__() # 调用父类 必须要有
        self.linear = torch.nn.Linear(1, 1) # 构造对象

    # 前向反馈
    def forward(self, x):
        y_pred = F.sigmoid(self.linear(x))
        return y_pred
    
model = LogisticRegressionModel()

# 构造损失函数和优化器
criterion = torch.nn.BCELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    y_prep = model(x_data)
    loss = criterion(y_prep, y_data)
    print(epoch, loss)

    optimizer.zero_grad()
    loss.backward()  # 反向传播
    optimizer.step() # 更新权重

x = np.linspace(0, 10, 200)
x_t = torch.Tensor(x).view((200, 1))
y_t = model(x_t)
y = y_t.data.numpy()
plt.plot(x, y)
plt.plot([0, 10], [0.5, 0.5], c='r')
plt.xlabel('Hours')
plt.ylabel('Probability of Pass')
plt.grid()
plt.show()
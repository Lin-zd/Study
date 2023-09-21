import torch
import numpy as np
from torch.utils.data import Dataset  # 抽象类 只能被继承
from torch.utils.data import DataLoader  # 加载数据
from torchvision import transforms
from torchvision import datasets

'''
train_dataset = datasets.MNIST(root='./dataset/mnist', train=True,
                               transform=transforms.ToTensor(),
                               download=True)
test_dataset = datasets.MNIST(root='./dataset/mnist', train=False,
                               transform=transforms.ToTensor(),
                               download=True)
train_lodar = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)
test_lodar = DataLoader(dataset=test_dataset, batch_size=32, shuffle=False)

for batch_idx, (inputs, target) in enumerate(train_loader):

'''

class DiabetesDataset(Dataset): 
    def __init__(self, filepath):
        xy = np.loadtxt(filepath, delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]
        self.x_data = torch.from_numpy(xy[:,:-1])
        self.y_data = torch.from_numpy(xy[:,[-1]])
    # 魔法方法 实例化后支持下标操作
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    # 魔法函数 实例化后支持长度返回 
    def __len__(self):
        return self.len

dataset = DiabetesDataset('./diabetes.csv.gz')
train_loader = DataLoader(dataset=dataset, batch_size=32, 
                          shuffle=True, num_workers=2)


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)  # 多维输入
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.activate = torch.nn.Sigmoid()
        # self.activate = torch.nn.ReLU()

    def forward(self, x):
        x = self.activate(self.linear1(x))
        x = self.activate(self.linear2(x))
        x = self.activate(self.linear3(x))
        return x
    
model = Model()

criterion = torch.nn.BCELoss(size_average=True)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

if __name__ == '__main__':
    for epoch in range(100):
        for i, data in enumerate(train_loader, 0):
            # 数据准备
            inputs, labels = data
            # 前向传播
            y_pred = model(inputs)
            loss = criterion(y_pred, labels)
            print(epoch, i, loss.item())
            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            # 更新
            optimizer.step()
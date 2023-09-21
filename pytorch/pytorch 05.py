import torch

x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[2.0], [4.0], [6.0]])

class LinearModel(torch.nn.Module):
    # 构造函数 初始化对象
    def __init__(self):
        super(LinearModel, self).__init__() # 调用父类 必须要有
        self.linear = torch.nn.Linear(1, 1) # 构造对象

    # 前向反馈
    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred
    
model = LinearModel()

# 构造损失函数和优化器
criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    y_prep = model(x_data)
    loss = criterion(y_prep, y_data)
    print(epoch, loss)

    optimizer.zero_grad()
    loss.backward()  # 反向传播
    optimizer.step() # 更新权重

print('w=', model.linear.weight.item())
print('b=', model.linear.bias.item())

x_test = torch.Tensor([[4.0]])
y_test = model(x_test)
print('y_perd=', y_test.data)
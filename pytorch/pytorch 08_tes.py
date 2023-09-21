import torch
import numpy as np
import pandas as pd
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

class DiabetesDataset(Dataset):
    def __init__(self, filepath):
        xy = pd.read_csv(filepath)
        self.len = xy.shape[0]
        # 选取相关的数据特征
        features = ["Pclass", "Sex", "SibSp", "Parch"]
        self.x_data = torch.from_numpy(np.array(pd.get_dummies(xy[features])))
        self.y_data = torch.from_numpy(np.array(xy["Survived"]))

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len

dataset = DiabetesDataset('./dataset/titanic_train.csv')
train_loader = DataLoader(dataset=dataset, batch_size=32,shuffle=True,num_workers=2)

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(5, 3)
        self.linear2 = torch.nn.Linear(3, 1)
        self.activate = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.activate(self.linear1(x))
        x = self.activate(self.linear2(x))
        return x
    
    def test(self, x):
        with torch.no_grad():
            x = self.activate(self.linear1(x))
            x = self.activate(self.linear2(x))
            y = []
            for i in x :
                if i > 0.5 :
                    y.append(1)
                else:
                    y.append(0)
            return y
    
model = Model()

criterion = torch.nn.BCELoss(reduction='mean')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

if __name__ == '__main__':
    for epoch in range(100):
        for i, data in enumerate(train_loader, 0):
            # 数据准备
            inputs, labels = data
            inputs = inputs.float()
            labels = labels.float()
            # 前向传播
            y_pred = model(inputs)
            y_pred = y_pred.squeeze(-1)
            loss = criterion(y_pred, labels)
            print(epoch, i, loss.item())
            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            # 更新
            optimizer.step()

# 测试
test_data = pd.read_csv('./dataset/titanic_test.csv')

features = ["Pclass", "Sex", "SibSp", "Parch"]
test=torch.from_numpy(np.array(pd.get_dummies(test_data[features])))
y=model.test(test.float())
 
# 输出预测结果
output=pd.DataFrame({'PassengerId':test_data.PassengerId,'Survived':y})
output.to_csv('my_predict.csv', index=False)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]
 
def forward(x):
    return x*w + b
 
def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y)**2
 
# 穷举法
w_list = []
b_list = []
mse_list = []
for w in np.arange(0.0, 4.1, 0.1):
    for b in np.arange(-2.0, 2.1, 0.1):
        l_sum=0
        for x_val, y_val in zip(x_data, y_data):
            y_pred_val = forward(x_val)
            loss_val = loss(x_val, y_val)
            l_sum += loss_val
            print('\t', x_val, y_val, y_pred_val, loss_val)
        w_list.append(w)
        b_list.append(b)
        mse_list.append(l_sum/3)
    
mse_list = np.array(mse_list)
mse_list = mse_list.reshape(41, 41)
mse_list = mse_list.transpose()

# w和b由于嵌套的for循环，每个值都出现了41次，故要去重，接下来使用meshgrid将w和b转化成41*41的矩阵
w, b = np.meshgrid(np.unique(w_list), np.unique(b_list))

# Plot the surface.
surf = ax.plot_surface(w, b, mse_list, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0, 35)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.00f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)


ax.set_xlabel('w')
ax.set_ylabel('b')
ax.text2D(0.4, 0.92, "Cost Values", transform=ax.transAxes)
plt.show()
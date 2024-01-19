import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据集
x = np.arange(1, 11)
y = np.array([2, 4, 1, 7, 5, 10, 8, 3, 6, 9])

# 设置Seaborn样式
sns.set(style="whitegrid")

# 绘制折线图
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
sns.lineplot(x=x, y=y)
plt.title('折线图')

# 绘制散点图
plt.subplot(1, 3, 2)
sns.scatterplot(x=x, y=y, color='red')
plt.title('散点图')

# 绘制柱状图
plt.subplot(1, 3, 3)
sns.barplot(x=x, y=y, color='green')
plt.title('柱状图')

# 显示图形
plt.tight_layout()
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 相关系数矩阵数据
correlation_data = {
    'server': [1, -0.017804238, 0.405710795],
    'serve_no': [-0.017804238, 1, -0.017482919],
    'point_victor': [0.405710795, -0.017482919, 1]
}

# 创建DataFrame
correlation_df = pd.DataFrame(correlation_data, index=['server', 'serve_no', 'point_victor'])

# 绘制相关系数矩阵的热图，使用不同的配色方案
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_df, annot=True, cmap='PRGn', fmt=".3f", vmin=-1, vmax=1, linewidths=.5)


# 保存图像到文件
plt.savefig('相关系数/发球因素相关系数.png', dpi=600)

# 显示图像
plt.show()

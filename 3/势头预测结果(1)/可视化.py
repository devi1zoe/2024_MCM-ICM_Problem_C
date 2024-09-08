# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # 读取Excel文件
# df = pd.read_csv('势头波动预测2503.csv')
#
# # 设置时间作为索引
# df.set_index('point_no', inplace=True)
#
# # 创建子图
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(11, 9))
#
# # 1. 折线图 - Model 1
# df[['p1_momentum', 'p1_momentum_predict_lightGBM']].plot(ax=axes[0])
# axes[0].set_xlabel('point_no')
# axes[0].set_ylabel('Momentum')
# axes[0].legend(loc='upper right')
#
# # 2. 折线图 - Model 2
# df[['p2_momentum', 'p2_momentum_predict_lightGBM']].plot(ax=axes[1])
# axes[1].set_xlabel('point_no')
# axes[1].set_ylabel('Momentum')
# axes[1].legend(loc='upper right')
#
# # 调整布局
# plt.tight_layout()
#
# # 保存图形
# plt.savefig('2503折线图.png', transparent=True, dpi=600)
# plt.show()




# # 5. 子图
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
# df[['p1_momentum', 'p1_momentum_predict_svm']].plot(ax=axes[0, 0])
# axes[0, 0].set_title('SVM Prediction')
# axes[0, 0].legend(loc='upper right')
# df[['p1_momentum', 'p1_momentum_predict_XGboost']].plot(ax=axes[0, 1])
# axes[0, 1].set_title('Xgboost Prediction')
# axes[0, 1].legend(loc='upper right')
# df[['p1_momentum', 'p1_momentum_predict_arima_rolling']].plot(ax=axes[1, 0])
# axes[1, 0].set_title('ARIMA Rolling Predictions')
# axes[1, 0].legend(loc='upper right')
# df[['p1_momentum', 'p1_momentum_predict_lightGBM']].plot(ax=axes[1, 1])
# axes[1, 1].set_title('lightGBM Predictions')
# axes[1, 1].legend(loc='upper right')
# plt.tight_layout()
#
# plt.savefig('子图1.png', transparent=True, dpi=600)
# plt.show()

# # 5. 子图
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
# df[['p2_momentum', 'p2_momentum_predict_svm']].plot(ax=axes[0, 0])
# axes[0, 0].set_title('SVM Prediction')
# axes[0, 0].legend(loc='upper right')
# df[['p2_momentum', 'p2_momentum_predict_XGboost']].plot(ax=axes[0, 1])
# axes[0, 1].set_title('Xgboost Prediction')
# axes[0, 1].legend(loc='upper right')
# df[['p2_momentum', 'p2_momentum_predict_arima_rolling']].plot(ax=axes[1, 0])
# axes[1, 0].set_title('ARIMA Rolling Predictions')
# axes[1, 0].legend(loc='upper right')
# df[['p2_momentum', 'p2_momentum_predict_lightGBM']].plot(ax=axes[1, 1])
# axes[1, 1].set_title('lightGBM Predictions')
# axes[1, 1].legend(loc='upper right')
# plt.tight_layout()
#
# plt.savefig('子图2.png', transparent=True, dpi=600)
# plt.show()
#
#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
# df = pd.read_csv('势头波动预测2503.csv')
df = pd.read_excel('势头波动预测.xlsx')

# 设置时间作为索引
df.set_index('point_no', inplace=True)

# 创建势头变化图
plt.figure(figsize=(10, 6))
plt.plot(df['p1_p2_momentum_predict_lightGBM_cha'], label='Momentum Difference Change', color='#6ABAA4')

# 初始化新的DataFrame来保存每八个点的统计信息
stats_df = pd.DataFrame()

# 计算分组的数量
num_groups = len(df) // 8

# 对每个八点分组进行操作
for i in range(num_groups):
    # 选择当前分组的数据
    group_data = df['p1_p2_momentum_predict_lightGBM_cha'].iloc[i * 8: (i + 1) * 8]

    # 计算当前分组的统计信息
    group_stats = {
        'point_no': group_data.index[3],  # 选择中间点作为x值
        'avg_momentum': group_data.mean()  # 计算平均势能
    }

    # 将当前分组的统计信息添加到新的DataFrame
    stats_df = pd.concat([stats_df, pd.DataFrame([group_stats])], ignore_index=True)

# 画出每八个点的平均势能
plt.scatter(stats_df['point_no'],
            stats_df['avg_momentum'],
            color=np.where(stats_df['avg_momentum'] > 0, '#938BB7', '#FF8A6C'),  # 势能大于0使用绿色，否则使用红色
            label='Average Momentum Difference every 8 points',
            zorder=10)  # Set a higher zorder to make points appear above the line

# 连接点之间的虚曲线
plt.plot(stats_df['point_no'], stats_df['avg_momentum'], linestyle='dashed', color='gray', zorder=5)


plt.xlabel('point_no')
plt.ylabel('Momentum Difference')
plt.legend(loc='upper right')
plt.grid(False)  # 添加网格线

# plt.savefig('2503预测的势头波动图.png', transparent=True, dpi=600)
plt.savefig('预测的势头波动图.png', transparent=True, dpi=600)
plt.show()
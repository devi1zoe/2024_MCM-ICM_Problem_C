# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 读取Excel文件
# file_path = '灵敏度分析.xlsx'
# df = pd.read_excel(file_path, sheet_name='Sheet2')
#
# # 调整心理因素权重
# psychological_weight = 0.01
#
# # 重新计算p1_momentum
# df['new_p1_momentum'] = df['p1_Psychological_Factor'] * psychological_weight + \
#                         df['p1_Physical_Factor'] * 0.2 + \
#                         df['p1_skill_factors'] * 0.3 + \
#                         df['p1_server_factors'] * 0.4
#
# # 将DataFrame保存到新的Excel文件
# output_excel_path = '123.xlsx'
# df.to_excel(output_excel_path, index=False)
#
# print(f"New data with 'new_p1_momentum' column saved to {output_excel_path}")

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取CSV文件
file_path = '灵敏度分析.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet2')

# 获取所有不同的 match_id
unique_match_ids = df['match_id'].unique()

# 遍历每个 match_id
for match_id in unique_match_ids:
    plt.figure(figsize=(12, 5))

    # 选择当前 match_id 的数据
    match_data = df[df['match_id'] == match_id]

    # 为 p1_momentum 和 p2_momentum 设置基础颜色
    base_color_p1 = 'seagreen'
    base_color_p2 = 'royalblue'

    # 使用累计值绘制 p1_momentum 的折线图
    sns.lineplot(data=match_data, x=match_data.index, y='p1_momentum_sum', color=base_color_p1, label='old')

    # 使用累计值绘制 p2_momentum 的折线图
    sns.lineplot(data=match_data, x=match_data.index, y='new_p1_momentum_sum', color=base_color_p2, label='new')

    # 设置图例和标签
    plt.xlabel('point_no')
    plt.ylabel('Cumulative Momentum')
    plt.grid(False)
    # 设置图例位置和标题
    plt.legend(title=f'Match {match_id}', loc='upper right', bbox_to_anchor=(1.2, 1))
    # 调整坐标轴位置
    plt.subplots_adjust(right=0.8)
    # 保存图形，注意设置透明背景

    # 创建保存图形的文件夹
    output_folder = '灵敏度'
    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(os.path.join(output_folder, f'比赛{match_id}_sum.png'), transparent=True, dpi=600)
    plt.close()

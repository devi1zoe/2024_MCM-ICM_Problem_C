# import os
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 读取CSV文件
# file_path = 'perfect2_1701_no.xlsx'
# df = pd.read_excel(file_path)
#
# # 获取所有不同的 match_id
# unique_match_ids = df['match_id'].unique()
#
# # 遍历每个 match_id
# for match_id in unique_match_ids:
#     # 选择当前 match_id 的数据
#     match_data = df[df['match_id'] == match_id]
#
#     # 获取当前 match_id 的 set_no 列的唯一值
#     unique_set_nos = match_data['set_no'].unique()
#
#     # 遍历每个 set_no，生成对应的折线图
#     for set_no in unique_set_nos:
#         plt.figure(figsize=(12, 5))
#
#         set_data = match_data[match_data['set_no'] == set_no]
#
#         # 为 p1_momentum 和 p2_momentum 设置基础颜色
#         base_color_p1 = 'seagreen'
#         base_color_p2 = 'royalblue'
#
#         # 使用单一颜色绘制 p1_momentum 的折线图
#         sns.lineplot(data=set_data, x=set_data.index, y='p1_momentum', color=base_color_p1, label='Player 1')
#
#         # 使用单一颜色绘制 p2_momentum 的折线图
#         sns.lineplot(data=set_data, x=set_data.index, y='p2_momentum', color=base_color_p2, label='Player 2')
#
#         # 设置图例和标签
#         plt.xlabel('point_no')
#         plt.ylabel('Momentum')
#         plt.grid(False)
#         # 设置图例位置和标题
#         plt.legend(title=f'Set {set_no}', loc='upper right', bbox_to_anchor=(1.2, 1))
#         # 调整坐标轴位置
#         plt.subplots_adjust(right=0.8)
#         # 保存图形，注意设置透明背景
#
#         # 创建保存图形的文件夹
#         output_folder = '每场比赛的全程势能'
#         os.makedirs(output_folder, exist_ok=True)
#         plt.savefig(os.path.join(output_folder, f'比赛{match_id}_set{set_no}.png'), transparent=True, dpi=600)
#         plt.close()

#







import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取CSV文件
file_path = 'perfect2_1701_no.xlsx'
df = pd.read_excel(file_path)

# 获取所有不同的 match_id
unique_match_ids = df['match_id'].unique()

# 遍历每个 match_id
for match_id in unique_match_ids:
    # 选择当前 match_id 的数据
    match_data = df[df['match_id'] == match_id]

    # 获取当前 match_id 的 set_no 列的唯一值
    unique_set_nos = match_data['set_no'].unique()

    # 遍历每个 set_no，生成对应的折线图
    for set_no in unique_set_nos:
        plt.figure(figsize=(12, 5))

        set_data = match_data[match_data['set_no'] == set_no]

        # 为 p1_momentum 和 p2_momentum 设置基础颜色
        base_color_p1 = 'seagreen'
        base_color_p2 = 'royalblue'

        # 计算 p1_momentum 和 p2_momentum 的累计值
        set_data['p1_momentum_cumulative'] = set_data['p1_momentum'].cumsum()
        set_data['p2_momentum_cumulative'] = set_data['p2_momentum'].cumsum()

        # 使用累计值绘制 p1_momentum 的折线图
        sns.lineplot(data=set_data, x=set_data.index, y='p1_momentum_cumulative', color=base_color_p1, label='Player 1')

        # 使用累计值绘制 p2_momentum 的折线图
        sns.lineplot(data=set_data, x=set_data.index, y='p2_momentum_cumulative', color=base_color_p2, label='Player 2')

        # 设置图例和标签
        plt.xlabel('point_no')
        plt.ylabel('Cumulative Momentum')
        plt.grid(False)
        # 设置图例位置和标题
        plt.legend(title=f'Set {set_no}', loc='upper right', bbox_to_anchor=(1.2, 1))
        # 调整坐标轴位置
        plt.subplots_adjust(right=0.8)
        # 保存图形，注意设置透明背景

        # 创建保存图形的文件夹
        output_folder = '每场比赛的全程势能'
        os.makedirs(output_folder, exist_ok=True)
        plt.savefig(os.path.join(output_folder, f'比赛{match_id}_set{set_no}_cumulative.png'), transparent=True, dpi=600)
        plt.close()


# import os
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 读取CSV文件
# file_path = 'perfect2_1701_no.xlsx'
# df = pd.read_excel(file_path)
#
# # 获取所有不同的 match_id
# unique_match_ids = df['match_id'].unique()
#
# # 遍历每个 match_id
# for match_id in unique_match_ids:
#     # 选择当前 match_id 的数据
#     match_data = df[df['match_id'] == match_id]
#
#     # 获取当前 match_id 的 set_no 列的唯一值
#     unique_set_nos = match_data['set_no'].unique()
#
#     # 遍历每个 set_no，生成对应的折线图
#     for set_no in unique_set_nos:
#         plt.figure(figsize=(12, 5))
#
#         set_data = match_data[match_data['set_no'] == set_no]
#
#         # 为 p1_momentum 和 p2_momentum 设置基础颜色
#         base_color_p1 = 'seagreen'
#         base_color_p2 = 'royalblue'
#
#         # 使用累计值绘制 p1_momentum 的折线图
#         sns.lineplot(data=set_data, x=set_data.index, y='A', color=base_color_p1, label='Player 1')
#
#         # 使用累计值绘制 p2_momentum 的折线图
#         sns.lineplot(data=set_data, x=set_data.index, y='B', color=base_color_p2, label='Player 2')
#
#         # 设置图例和标签
#         plt.xlabel('point_no')
#         plt.ylabel('Cumulative Momentum')
#         plt.grid(False)
#         # 设置图例位置和标题
#         plt.legend(title=f'Set {set_no}', loc='upper right', bbox_to_anchor=(1.2, 1))
#         # 调整坐标轴位置
#         plt.subplots_adjust(right=0.8)
#         # 保存图形，注意设置透明背景
#
#         # 创建保存图形的文件夹
#         output_folder = '每场比赛的全程势能'
#         os.makedirs(output_folder, exist_ok=True)
#         plt.savefig(os.path.join(output_folder, f'比赛{match_id}_set{set_no}_cumulative_cumulative.png'), transparent=True, dpi=600)
#         plt.close()



#
# import os
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 读取CSV文件
# file_path = 'perfect2_1701_no.xlsx'
# df = pd.read_excel(file_path)
#
# # 获取所有不同的 match_id
# unique_match_ids = df['match_id'].unique()
#
# # 遍历每个 match_id
# for match_id in unique_match_ids:
#     # 选择当前 match_id 的数据
#     match_data = df[df['match_id'] == match_id]
#
#     # 获取当前 match_id 的 set_no 列的唯一值
#     unique_set_nos = match_data['set_no'].unique()
#
#     # 创建一个子图，每个子图包含一行，五列，但不共享y轴刻度
#     fig, axes = plt.subplots(1, 5, figsize=(20, 5), sharey=False)
#
#     # 初始化y轴刻度的最大最小值
#     min_y = float('inf')
#     max_y = float('-inf')
#
#     # 遍历每个 set_no，生成对应的折线图
#     for idx, set_no in enumerate(unique_set_nos):
#         set_data = match_data[match_data['set_no'] == set_no]
#
#         # 为 p1_momentum 和 p2_momentum 设置基础颜色
#         base_color_p1 = 'seagreen'
#         base_color_p2 = 'royalblue'
#
#         # 计算 p1_momentum 和 p2_momentum 的累计值
#         set_data.loc[:, 'p1_momentum_cumulative'] = set_data['p1_momentum'].cumsum()
#         set_data.loc[:, 'p2_momentum_cumulative'] = set_data['p2_momentum'].cumsum()
#
#         # 使用累计值绘制 p1_momentum 的折线图
#         sns.lineplot(data=set_data, x=set_data.index, y='p1_momentum_cumulative', color=base_color_p1, label='Player 1', ax=axes[idx])
#
#         # 使用累计值绘制 p2_momentum 的折线图
#         sns.lineplot(data=set_data, x=set_data.index, y='p2_momentum_cumulative', color=base_color_p2, label='Player 2', ax=axes[idx])
#
#         # 更新y轴刻度的最大最小值
#         min_y = min(min_y, set_data['p1_momentum_cumulative'].min(), set_data['p2_momentum_cumulative'].min())
#         max_y = max(max_y, set_data['p1_momentum_cumulative'].max(), set_data['p2_momentum_cumulative'].max())
#
#         # 设置图例和标签
#         axes[idx].set_xlabel('point_no')
#         if idx == 0:
#             axes[idx].set_ylabel('Cumulative Momentum')
#         else:
#             axes[idx].set_ylabel('       ')
#         axes[idx].grid(False)
#         # 设置图例位置和标题
#         axes[idx].legend(title=f'Set {set_no}', loc='upper left')
#         # 调整坐标轴位置
#         fig.subplots_adjust(right=0.8)
#
#     # 在所有子图上统一设置y轴刻度的范围
#     for ax in axes:
#         ax.set_ylim(min_y, max_y)
#
#     # 创建保存图形的文件夹
#     output_folder = '每场比赛的全程势能'
#     os.makedirs(output_folder, exist_ok=True)
#     plt.savefig(os.path.join(output_folder, f'比赛{match_id}_all_sets_cumulative.png'), transparent=True, dpi=600)
#     plt.close()

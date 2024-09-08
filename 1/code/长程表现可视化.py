# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 读取CSV文件
# file_path = 'perfect.csv'
# df = pd.read_csv(file_path)
#
# # 提取需要的列数据
# user_data = df[['p1_momentum', 'p2_momentum']]
#
# # 将User列设置为索引，方便绘制折线图
# # user_data.set_index('User', inplace=True)
#
# # 使用seaborn绘制多幅折线图
# plt.figure(figsize=(12, 8))
#
# # 根据 match_id 分组并绘制折线图
# sns.lineplot(data=df, x=df.index, y='p1_momentum', hue='match_id', marker='o')
#
# plt.title('p1_momentum Over Time for Different match_id')
# plt.xlabel('Data Point')
# plt.ylabel('p1_momentum')
# plt.grid(True)
# plt.show()
#









# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 读取CSV文件
# file_path = 'perfect2.csv'
# df = pd.read_csv(file_path)
#
# # 获取所有不同的 match_id
# unique_match_ids = df['match_id'].unique()
#
# # 遍历每个 match_id，生成对应的折线图
# for match_id in unique_match_ids:
#     plt.figure(figsize=(12, 5))
#
#     # 选择当前 match_id 的数据
#     match_data = df[df['match_id'] == match_id]
#
#     # 绘制 p1_momentum 的折线图
#     sns.lineplot(data=match_data, x=match_data.index, y='p1_momentum', label='p1_momentum')
#
#     # 绘制 p2_momentum 的折线图
#     sns.lineplot(data=match_data, x=match_data.index, y='p2_momentum', label='p2_momentum')
#
#     plt.title(f'Momentum Over Time for match_id {match_id}')
#     plt.xlabel('Data Point')
#     plt.ylabel('Momentum')
#     plt.grid(True)
#     plt.show()










import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 读取CSV文件
file_path = 'perfect2.csv'
df = pd.read_csv(file_path)

# 创建保存图形的文件夹
output_folder = '每场比赛的全程势能'
os.makedirs(output_folder, exist_ok=True)

# 获取所有不同的 match_id
unique_match_ids = df['match_id'].unique()

# 遍历每个 match_id，生成对应的折线图
for match_id in unique_match_ids:
    plt.figure(figsize=(12, 5))

    # 选择当前 match_id 的数据
    match_data = df[df['match_id'] == match_id]

    # 绘制 p1_momentum 的折线图
    sns.lineplot(data=match_data, x=match_data.index, y='p1_momentum', label='p1_momentum')

    # 绘制 p2_momentum 的折线图
    sns.lineplot(data=match_data, x=match_data.index, y='p2_momentum', label='p2_momentum')

    plt.title(f'Momentum Over Time for match_id {match_id}')
    plt.xlabel('Data Point')
    plt.ylabel('Momentum')
    plt.grid(True)

    # 保存图形，注意设置透明背景
    plt.savefig(os.path.join(output_folder, f'比赛{match_id}.png'), transparent=True)

    # 关闭当前图形，以便下一个图形可以在新的窗口中显示
    plt.close()






import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取CSV文件
file_path = 'perfect2_1701_no.xlsx'
df = pd.read_excel(file_path)

# 获取所有不同的 match_id
unique_match_ids = df['match_id'].unique()

# 计算 set_no 的唯一值数量
num_unique_sets = df['set_no'].nunique()

# 为 p1_momentum 和 p2_momentum 设置基础颜色
base_color_p1 = 'seagreen'
base_color_p2 = 'royalblue'

# 根据 set_no 的数量生成颜色渐变
palette_p1 = sns.color_palette("Blues")
# 只取后 num_unique_sets 个颜色
palette_p1 = palette_p1[-num_unique_sets:]
palette_p2 = sns.cubehelix_palette()
# 只取后 num_unique_sets 个颜色
palette_p2 = palette_p2[-num_unique_sets:]

# 遍历每个 match_id，生成对应的折线图
for i, match_id in enumerate(unique_match_ids):
    # 判断是否为最后一个 match_id，只在最后一个循环中显示图形
    if i == len(unique_match_ids) - 1:
        plt.figure(figsize=(15, 5))

        # 选择当前 match_id 的数据
        match_data = df[df['match_id'] == match_id]

        # 绘制 p1_momentum 的折线图，根据 set_no 列用不同颜色展示
        sns.lineplot(data=match_data, x=match_data.index, y='p1_momentum', hue='set_no', palette=palette_p1)

        # 绘制 p2_momentum 的折线图，根据 set_no 列用不同颜色展示
        sns.lineplot(data=match_data, x=match_data.index, y='p2_momentum', hue='set_no', palette=palette_p2)

        # 设置图例和标签
        plt.xlabel('point_no')
        plt.ylabel('Momentum')
        plt.grid(False)
        # 设置图例位置和标题
        plt.legend(title='Player1 vs Player2', loc='upper right', bbox_to_anchor=(1.2, 1), ncol=2)
        # 调整坐标轴位置
        plt.subplots_adjust(right=0.8)
        # 保存图形，注意设置透明背景

        # 创建保存图形的文件夹
        output_folder = '每场比赛的全程势能'
        os.makedirs(output_folder, exist_ok=True)
        plt.savefig(os.path.join(output_folder, f'比赛{match_id}的拉宽图.png'), transparent=True, dpi=600)

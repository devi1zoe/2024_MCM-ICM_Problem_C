# import pandas as pd
import os
#
# # 获取当前工作目录
# current_directory = os.getcwd()
# data_directory = os.path.join(current_directory, '中间数据')
#
# # 用于存储每个文件的最后一行数据和平均速度值
# last_rows_data = []
#
# # 循环处理每个match_id对应的文件
# for filename in os.listdir(data_directory):
#     if filename.startswith("match_") and filename.endswith(".csv"):
#         # 读取每个文件
#         file_path = os.path.join(data_directory, filename)
#         data = pd.read_csv(file_path)
#
#         # 计算 "speed_mph" 列的平均值
#         average_speed = data['speed_mph'].mean()
#
#         # 提取每个文件的最后一行数据
#         last_row = data.iloc[-1]
#
#         # 将每个文件的最后一行数据和平均速度值保存到列表中
#         last_row['average_speed_mph'] = average_speed
#         last_rows_data.append(last_row)
#
# # 创建包含所有最后一行数据和平均速度值的DataFrame
# last_rows_dataframe = pd.DataFrame(last_rows_data)
#
# # 将包含所有最后一行数据和平均速度值的DataFrame保存为单独的CSV文件
# output_file_path = 'last_rows_and_average_speed.csv'
# last_rows_dataframe.to_csv(output_file_path, index=False)
#
# print("每个文件的最后一行数据和平均速度值已保存为CSV文件，文件名为last_rows_and_average_speed.csv，保存在当前工作目录中。")


import pandas as pd

# 获取当前工作目录
current_directory = os.getcwd()
data_directory = os.path.join(current_directory, '中间数据')

# 用于存储每个文件的最后一行数据和平均速度值
last_rows_data = []

# 循环处理每个match_id对应的文件
for filename in os.listdir(data_directory):
    if filename.startswith("match_") and filename.endswith(".csv"):
        # 读取每个文件
        file_path = os.path.join(data_directory, filename)
        df = pd.read_csv(file_path)

        # 设定滑动窗口大小为10
        window_size = 10

        # 选择需要进行滑动窗口操作的列
        selected_columns = ['p1_ace', 'p2_ace', 'p1_winner', 'p2_winner', 'p1_double_fault', 'p2_double_fault',
                            'p1_unf_err', 'p2_unf_err', 'p1_net_pt', 'p2_net_pt', 'p1_net_pt_won', 'p2_net_pt_won',
                            'p1_break_pt', 'p2_break_pt', 'p1_break_pt_won', 'p2_break_pt_won', 'p1_break_pt_missed',
                            'p2_break_pt_missed']

        # 计算每个变量的滑动窗口前缀和
        for column in df[selected_columns].columns:
            if column.startswith('p1_') or column.startswith('p2_'):
                # 利用rolling函数计算滑动窗口前缀和
                df[column + '_rolling_sum'] = df[column].rolling(window=window_size, min_periods=1).sum()

        # 打印结果
        print(df[selected_columns])

        df[selected_columns].to_csv(f'1111.csv', index=False)

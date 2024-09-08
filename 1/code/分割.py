import pandas as pd

# 读取原始CSV文件
file_path = 'Wimbledon_featured_matches.csv'
data = pd.read_csv(file_path)

# 按match_id分组
grouped_data = data.groupby('match_id')

# 将每个分组保存为单独的CSV文件
for group_name, group_df in grouped_data:
    output_file_path = f'match_{group_name}.csv'
    group_df.to_csv(output_file_path, index=False)

print("分割完成，每个文件以match_id命名，保存在当前工作目录中。")

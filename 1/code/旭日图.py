import pandas as pd
import plotly.express as px

# 读取Excel文件
data = pd.read_excel('旭日图2.xlsx')

# 确保所有类别都是完整的
data['总'] = data['总'].fillna(method='ffill')

# 创建旭日图
fig = px.sunburst(data, path=['总', '分'], values='比例', color='比例', color_continuous_scale='Mint')
fig.update_traces(textinfo='label+value')

import plotly.io as pio

pio.write_image(fig, 'images/2.png')

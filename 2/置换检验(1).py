import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns

# 1. 加载数据
try:
    data = pd.read_csv('数据处理及各参数权重值final/after_processing_final.csv')
except FileNotFoundError:
    raise FileNotFoundError("File not found. Please check the file path.")
except pd.errors.EmptyDataError:
    raise ValueError("The file is empty. Please check the data.")

# 2. 准备数据
def prepare_data(data):
    # 删除缺失值
    data = data.dropna(subset=['p1_Psychological_Factor', 'p2_Psychological_Factor', 'p1_Physical_Factor',
                               'p2_Physical_Factor', 'p1_skill_factors', 'p2_skill_factors','p1_server_factors','p2_server_factors',
                               'p1_momentum', 'p2_momentum', 'point_victor'])
    X = data[['p1_Psychological_Factor', 'p2_Psychological_Factor', 'p1_Physical_Factor',
               'p2_Physical_Factor', 'p1_skill_factors', 'p2_skill_factors','p1_server_factors','p2_server_factors',
               'p1_momentum', 'p2_momentum']]
    y = data['point_victor']
    return X, y

X, y = prepare_data(data)

# 归一化特征
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. 定义模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. 计算实际预测准确率
y_pred = model.predict(X_test)
actual_accuracy = accuracy_score(y_test, y_pred)

# 5. 特征重要性
importances = model.feature_importances_
feature_names = ['p1_Psychological_Factor', 'p2_Psychological_Factor', 'p1_Physical_Factor',
                  'p2_Physical_Factor', 'p1_skill_factors', 'p2_skill_factors',
                  'p1_server_factors','p2_server_factors','p1_momentum', 'p2_momentum']

feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)


# 6. 执行置换检验
n_permutations = 1000
permuted_accuracies = []

for _ in range(n_permutations):
    # 置换势头数据
    permuted_y = np.random.permutation(y_test)
    permuted_accuracy = accuracy_score(permuted_y, y_pred)
    permuted_accuracies.append(permuted_accuracy)

# 7. 计算统计量和p值
p_value = np.mean(np.array(permuted_accuracies) >= actual_accuracy)

# 8. 置换检验结果图
plt.figure(figsize=(12, 6))
sns.histplot(permuted_accuracies, bins=10, kde=True, color='#7680B4', label='Permuted Accuracies')
plt.axvline(x=actual_accuracy, color='red', linestyle='dashed', linewidth=2, label='Actual Accuracy')
plt.xlabel('Accuracy')
plt.ylabel('Frequency')


# 9. 添加图例
plt.legend(loc='upper left', bbox_to_anchor=(0.3, 1), fontsize=10, frameon=True, facecolor='white', edgecolor='black')


# 11. 输出准确率等信息
plt.text(0.7, n_permutations * 0.15, f'Actual Accuracy: {actual_accuracy:.4f}',
         color='red', fontsize=12, fontweight='bold', fontfamily='Book Antiqua', ha='right')

plt.text(0.7, n_permutations * 0.14, f'p-value: {p_value:.4f}', color='black', fontsize=12, fontweight='bold', fontfamily='Book Antiqua', ha='right')
if p_value < 0.05:
    plt.text(0.7, n_permutations * 0.13, 'Reject Null Hypothesis', color='green', fontsize=12, fontweight='bold', fontfamily='Book Antiqua', ha='right')
else:
    plt.text(0.7, n_permutations * 0.13, 'Cannot Reject Null Hypothesis', color='green', fontsize=12, fontweight='bold', fontfamily='Book Antiqua', ha='right')


#
# # 12. 显示图表
# plt.show()

# 13. 打印准确率
print("Actual Accuracy:", actual_accuracy)
plt.savefig('置换检验.png', transparent=True, dpi=600)
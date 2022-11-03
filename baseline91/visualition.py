import joblib
import pandas
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']


X_test = pandas.read_csv("datasets/test_public.csv")
X_train = pandas.read_csv("datasets/train_public.csv")
X_inter = pandas.read_csv("datasets/train_internet.csv")

# 条形图
# baseCols = ['industry', 'employer_type', 'work_year', 'class']
# for name in baseCols:
#     plt.xticks(rotation=45)
#     cnt = pd.crosstab(X_inter[name], X_inter['isDefault'])    # 构建特征与目标变量的列联表
#     cnt.plot.bar(stacked=True)#绘制堆叠条形图，便于观察不同特征值流失的占比情况
#     plt.title(name)
#     plt.xticks(rotation=45)
#     plt.savefig(f"picture/{name}.svg")
#     plt.show()    # 展示图像
#
# ### 观察流失率与入网月数的关系
# # 折线图
# groupDf = X_train[['work_year', 'isDefault']]    # 只需要用到两列数据
# pctDf = groupDf.groupby(['work_year']).sum() / groupDf.groupby(['work_year']).count()    # 计算不同入网月数对应的流失率
# pctDf = pctDf.reset_index()    # 将索引变成列
# plt.figure(figsize=(10, 5))
# plt.plot(pctDf['tenure'], pctDf['Churn'], label='Churn percentage')    # 绘制折线图
# plt.legend()    # 显示图例
# plt.show()

# # 每贷款利率密度估计图
# plt.figure(figsize=(10, 5))    # 构建图像
#
# negDf = X_train[X_train['isDefault'] == 0]
# sns.distplot(negDf['monthly_payment'], hist=False, label='0')
# posDf = X_train[X_train['isDefault'] == 1]
# sns.distplot(posDf['monthly_payment'], hist=False, label='1')
# plt.legend()
# plt.savefig(f"picture/monthly_payment.svg")
# plt.show()    # 展示图像

# # 饼状图
# p = X_train['isDefault'].value_counts()  # 目标变量正负样本的分布
#
# plt.figure(figsize=(5, 5))  # 构建图像
#
# # 绘制饼图并调整字体大小
# patches, l_text, p_text = plt.pie(p, labels=['No', 'Yes'], autopct='%1.2f%%', explode=(0, 0.1))
# # l_text是饼图对着文字大小，p_text是饼图内文字大小
# for t in p_text:
#     t.set_size(15)
# for t in l_text:
#     t.set_size(15)
#
# plt.savefig(f"picture/pie.svg")
# plt.show()  # 展示图像


# 每贷款利率密度估计图
plt.figure(figsize=(6,6))    # 构建图像

negDf = X_train[X_train['isDefault'] == 0]
sns.distplot(negDf['year_of_loan'], label='0')
posDf = X_train[X_train['isDefault'] == 1]
sns.distplot(posDf['year_of_loan'], label='1')
plt.legend()
plt.savefig(f"picture/yearOfLoanDist.svg")
plt.show()    # 展示图像
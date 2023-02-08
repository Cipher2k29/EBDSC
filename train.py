import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import model_selection
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib
import pandas
import csv
from sklearn.preprocessing import MinMaxScaler

# path = './train/11/Mixed.csv'  # 数据文件路径
path = './merged/merged_result.csv' 
# data = np.genfromtxt(path, dtype=float, delimiter=',', usecols=(0,1,3,4,5,6), skip_header=1)
# 特征对应 1-A 3-B 4-C 5-D 
# x, y = np.split(data, (5,), axis=1)
# x = MinMaxScaler().fit_transform(x)
data = np.loadtxt(path, dtype=float, delimiter=',', usecols=(0,5,6), skiprows=1)
x, y = np.split(data, (2,), axis=1)

#clf = GaussianNB() #高斯朴素贝叶斯
#clf = RFC(max_depth = 50) #随机森林    由于已经对特征进行了分析 且计算开销过大，因此不需要再进行考虑
clf = DTC(  criterion = 'entropy', 
            # max_depth = 5,    #max_depth=None
            # random_state = 12
            ) #决策树 
            #这里很奇怪 max_depth不进行设定时训练集效果一般但验证全对，若设定18左右效果较好但验证有问题
            #且训练集无论怎么放特征 看起来结果都正常，主要差异出现在验证时
#clf = LR() #LogisticRegression

# C = []
# for i in range(10):
#     tmp1 = random.uniform(0.1,100)
#     C.append(tmp1)
# print(C)
# gamma = []
# for i in range(10):
#     tmp2 = random.uniform(0.0001,10)
#     gamma.append(tmp2)
# print(gamma)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, train_size=0.8, shuffle=True)
print(x_train.shape)
print(x_test.shape)
def show_accuracy(y_hat,y_train,str):
    pass
# for i in range (10):
#     for j in range (10):
#         clf = svm.SVC(C=C[i], kernel='rbf', gamma=gamma[j], decision_function_shape='ovr')
#         #C = C[i]
#         #gamma = gamma[j]
#
#         #C = 6.166279680147067
#         #gamma = 910.7683356828577
#         print("C的值为",C[i])
#         print("gamma的值为",gamma[j])
        #clf = svm.SVC(C=C, kernel='rbf', gamma=gamma, decision_function_shape='ovr')
clf.fit(x_train, y_train.ravel())
print("SVM-输出训练集的准确率为：", clf.score(x_train, y_train))
y_hat = clf.predict(x_train)
show_accuracy(y_hat, y_train, '训练集')
print("SVM-输出测试集的准确率为：", clf.score(x_test, y_test))
y_hat = clf.predict(x_test)
show_accuracy(y_hat, y_test, '测试集')

import joblib
#save model
joblib.dump(clf, 'clf.pkl')
# joblib.dump(clf, 'result.model')

# 数据可视化
# from sklearn.tree import plot_tree
# import matplotlib.pyplot as plt
# plt.figure(figsize=(15,9))
# plot_tree(clf.fit(x_train, y_train.ravel()), fontsize=9)
# plt.savefig('./visualize.jpg')

print('\npredict:\n', clf.predict(x_train),'\n\n',clf.predict(x_test))
def show_accuracy(y_hat,y_train,str):
    pass
list = clf.predict(x_test)
# with open('Accuracy.csv', 'w', newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(list)

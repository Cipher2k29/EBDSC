import numpy as np
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.model_selection import train_test_split
import csv


path = './merged/merged_result.csv' 
data = np.loadtxt(path, dtype=float, delimiter=',', usecols=(0,5,6), skiprows=1)
x, y = np.split(data, (2,), axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, train_size=0.8, shuffle=True)
clf = DTC() #决策树

clf.fit(x_train, y_train.ravel())
print("SVM-输出训练集的准确率为：", clf.score(x_train, y_train))
y_hat = clf.predict(x_train)
show_accuracy(y_hat, y_train, '训练集')
print("SVM-输出测试集的准确率为：", clf.score(x_test, y_test))
y_hat = clf.predict(x_test)
show_accuracy(y_hat, y_test, '测试集')

import joblib
#save model
joblib.dump(clf, 'result.model')

print('\npredict:\n', clf.predict(x_train),'\n\n',clf.predict(x_test))


from posixpath import basename
import numpy as np
import time
from sklearn.model_selection import train_test_split
import joblib
from collections import Counter
import os

#path = 'E:/电磁大数据挑战赛/初赛/train/11/Mixed.csv'  # 数据文件路径
#path = './train/all'
# path = './validation/all'   #原命名，不需要排序，可以测试准确率
path = './validation/01'
# path = './validation/try/convert' #这里就是数字命名，需要进行排序

total_stat = 0
correct_stat = 0

def data_stat(file_name):
    file_name = os.path.basename(file_name)
    class_file_name = file_name.split("_",1)
    total = 0
    correct = 0
    name = class_file_name[0] 
    if class_file_name[0] == "MTT":
        if max_value == 1:
            total += 1
            correct += 1
        else:
            total += 1
    elif class_file_name[0] == "STT":
        if max_value == 2:
            total += 1
            correct += 1
        else:
            total += 1
    elif class_file_name[0] == "TAS":
        if max_value == 3:
            total += 1
            correct += 1
        else:
            total += 1
    elif class_file_name[0] == "TWS":
        if max_value == 4:
            total += 1
            correct += 1
        else:
            total += 1
    return correct, total, name

if(os.path.exists("output.txt")):   #下面模式选的a+ 需要在这里移除以前的output
    os.remove("output.txt")

#如果拿数字命名的csv去做 需要加以下几句
# newsort = os.listdir(path)
# newsort.sort(key=lambda x:int(x.split('.')[0]))
# print(newsort)

t1 = time.time()
for file in os.listdir(path):
# for file in newsort:
    if file.endswith(".csv"):
        # print(str(path + '/' + file))
        # data = np.genfromtxt(str(path + '/' + file), dtype=float, delimiter=',', usecols=(0,1,3,4,5,6), skip_header=1)
        # x, y = np.split(data, (5,), axis=1)
        data = np.genfromtxt(str(path + '/' + file), dtype=float, delimiter=',', usecols=(0,5,6), skip_header=1)
        x, y = np.split(data, (2,), axis=1)
        # print(data)

        #load model
        clf = joblib.load('clf.pkl')

        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, train_size=0.01, shuffle=False)

        # print(x_test.shape)

        list = clf.predict(x_test)
        count = Counter(list)
        max_value = max(count,key=count.get)
        # print(max_value)
        with open('output.txt', 'a+', newline='') as txtfile:
            if max_value == 1:
                txtfile.write('MTT'+'\n')
            elif max_value == 2:
                txtfile.write('STT'+'\n')
            elif max_value == 3:
                txtfile.write('TAS'+'\n')
            # elif max_value == 4:
            else:
                txtfile.write('TWS'+'\n')

#以下部分对照标签判断准确率，需要用原来的名字
        correct, total, name = data_stat(str(path + '/' + file))
        total_stat += total
        correct_stat += correct

print(total_stat)
print(correct_stat)
print('Accuracy : {} %'.format(100 * correct_stat / total_stat))

t2 = time.time()
test_time = t2 - t1
print("测试耗时：%2.2fs" % test_time)


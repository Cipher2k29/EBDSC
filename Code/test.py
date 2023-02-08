import numpy as np
from sklearn.model_selection import train_test_split
import joblib
from collections import Counter
import os
from sklearn.impute import SimpleImputer
import pandas as pd	


# path = './train/all'
# path = './train/TWS'
# path = './validation/all'
path = './test'
new_column = []
i = 0
isExists = os.path.exists('./test/convert')
if not isExists:
    os.makedirs('./test/convert')
# print(os.listdir(path))
newsort1 = os.listdir(path)[1:]
newsort1.sort(key=lambda x:int((x.split('(')[-1]).split(')')[0]))
# print(newsort1)
for file in newsort1:
    if file.endswith(".csv"):
        i = i+1
        print(str(path + '/' + file))
        data=pd.read_csv(str(path + '/' + file), index_col=False)
        data = data.loc[ :, ~data.columns.str.contains("^Unnamed")]
        # print(data)
        # print(len(data['ID']))
        length = len(data['ID'])
        new_column = np.ones(length)    #添加一列1
        # new_column = [i+3 for i in new_column]    #用于添加1 2 3 4
        data1 = pd.DataFrame(data=data)
        new_column_1 = pd.DataFrame(data=new_column)
        # print(data)
        # print(new_column)
        # print(new_column_1)
        final = pd.concat([data,new_column_1],axis=1)
        # print(final)
        final.to_csv(str('./test/convert/' + str(i) + '.csv'), index=False)




path = './test/convert'
if(os.path.exists("output.txt")):
    os.remove("output.txt")

newsort2 = os.listdir(path)
newsort2.sort(key=lambda x:int(x.split('.')[0]))
# print(newsort2)

for file in newsort2:
    if file.endswith(".csv"):
        print(str(path + '/' + file))
        data = np.genfromtxt(str(path + '/' + file), dtype=float, delimiter=',', usecols=(0,5,6), skip_header=1)
        data = SimpleImputer(missing_values=np.nan, strategy='mean').fit_transform(data)

        x, y = np.split(data, (2,), axis=1)

        #load model
        clf = joblib.load('result.model')

        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, train_size=0.01, shuffle=False)

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
            else:
                txtfile.write('TWS'+'\n')


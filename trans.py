import pandas as pd	
import os	
import numpy as np

# path = './train/all'
# path = './train/TWS'
# path = './validation/all' #这里是转换文件不改名，用于测试准确率
path = './validation/try'   #这里是转换文件并改名，用于比赛实际要求
# path = './test'

'''以下是转换文件不改名，可用于测试准确率
new_column = []
for file in os.listdir(path):
    if file.endswith(".csv"):
        print(str(path + '/' + file))
        data = pd.read_csv(str(path + '/' + file), index_col=False)
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
        # isExists = os.path.exists('./test/convert')
        isExists = os.path.exists('./validation/try/convert')
        if not isExists:
            # os.makedirs('./test/convert')
            os.makedirs('./validation/try/convert')
        final.to_csv(str('./test/convert' + '/' + file), index=False)   #这里是转换文件但不改名
'''



'''以下是转换文件并改数字命名，需要注意读取顺序'''
new_column = []
i = 0
# isExists = os.path.exists('./test/convert')
isExists = os.path.exists('./validation/try/convert')
if not isExists:
    # os.makedirs('./test/convert')
    os.makedirs('./validation/try/convert')

# newsort是专门适用于input(n).csv格式的数据
newsort = os.listdir(path)[1:]  #不算convert文件夹
newsort.sort(key=lambda x:int((x.split('(')[-1]).split(')')[0]))
print(newsort)
for file in newsort:
    if file.endswith(".csv"):
        i = i+1
        print(str(path + '/' + file))
        data = pd.read_csv(str(path + '/' + file), index_col=False)
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
        
        final.to_csv(str('./validation/try/convert/' + str(i) + '.csv'), index=False) #这里是转换文件并改数字命名

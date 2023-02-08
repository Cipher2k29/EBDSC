#将某个目录下的CSV文件合格成一个
import pandas as pd
import os
def merge_csv():
    # 待处理的目录
    input_path = './train/all/'
    # input_path = './train/validation/'
    result_path = './merged/'
    result_name = 'merged_result.csv'  # 合并后要保存的文件名
    # 进入工作目录
    # os.chdir(input_path)
    # 获取该目录下所有文件的名字
    file_list = os.listdir(input_path)
    print(input_path + file_list[0])
    # 读取第一个CSV文件并包含表头
    df = pd.read_csv(input_path + file_list[0], encoding="gbk")  # 编码默认UTF-8,根据需要需改
    # 将读取的第一个CSV文件写入合并后的文件保存
    df.to_csv(result_path + result_name, encoding="gbk", index=False)
    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件

    # for i in range(1, len(file_list)):
    print(file_list[0])
    print(file_list[1050])
    print(file_list[2100])
    print(file_list[4550])
    print('\n')
    file_name = os.path.basename(input_path + file_list[0])
    class_file_name = file_name.split("_",1)
    if class_file_name[0] == "MTT":
        for i in range(1, 399):        
            # 过滤隐藏文件
            if not file_list[i].startswith("."):
                print(file_list[i])
                # 根据文件名读取文件
                df = pd.read_csv(input_path + file_list[i], encoding="gbk")
                # index=True 在最左侧新增索引列；header=True  保留 表头
                df.to_csv(result_path + result_name, encoding="gbk", index=False, header=False, mode='a+')
    
    file_name = os.path.basename(input_path + file_list[1050])
    class_file_name = file_name.split("_",1)
    if class_file_name[0] == "STT":
        for i in range(1, 400):        
            # 过滤隐藏文件
            if not file_list[1050+i].startswith("."):
                print(file_list[1050+i])
                # 根据文件名读取文件
                df = pd.read_csv(input_path + file_list[1050+i], encoding="gbk")
                # index=True 在最左侧新增索引列；header=True  保留 表头
                df.to_csv(result_path + result_name, encoding="gbk", index=False, header=False, mode='a+')

    file_name = os.path.basename(input_path + file_list[1050+1050])
    class_file_name = file_name.split("_",1)
    if class_file_name[0] == "TAS":
        for i in range(1, 400):        
            # 过滤隐藏文件
            if not file_list[1050+1050+i].startswith("."):
                print(file_list[1050+1050+i])
                # 根据文件名读取文件
                df = pd.read_csv(input_path + file_list[1050+1050+i], encoding="gbk")
                # index=True 在最左侧新增索引列；header=True  保留 表头
                df.to_csv(result_path + result_name, encoding="gbk", index=False, header=False, mode='a+')

    file_name = os.path.basename(input_path + file_list[1050+1050+2450])
    class_file_name = file_name.split("_",1)
    if class_file_name[0] == "TWS":
        for i in range(1, 400):        
            # 过滤隐藏文件
            if not file_list[1050+1050+2450+i].startswith("."):
                print(file_list[1050+1050+2450+i])
                # 根据文件名读取文件
                df = pd.read_csv(input_path + file_list[1050+1050+2450+i], encoding="gbk")
                # index=True 在最左侧新增索引列；header=True  保留 表头
                df.to_csv(result_path + result_name, encoding="gbk", index=False, header=False, mode='a+')

if __name__ == '__main__':
    merge_csv()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm
from pathlib import Path

FILE = Path(__file__).resolve()
print(FILE)
ROOT_data = FILE.parents[0]  # data root directory
print(ROOT_data)

for md in ['train', 'validation']:  # 在数据集划分层面遍历
    for m in ['MTT', 'STT', 'TAS', 'TWS']:  # 具体到种类进行划分
        pbar = tqdm((ROOT_data / md / m).glob('*.csv'), desc=f'Converting {dir}')
        for f in pbar:
            path = ROOT_data / md / m / f.name
            csv_name = md + m + f.name
            (ROOT_data / 'analysis' / md / m).mkdir(parents=True, exist_ok=True)
            save_path = ROOT_data / 'analysis' / md / m / (f.name[:-4] + '.jpg')
            pandas_read = pd.read_csv(path)

            plt.figure(figsize=(17, 17))
            plt.title(csv_name)

            # plt.subplot(5, 2, 1)
            # plt.plot((pandas_read["TOA(ns)"][101:401] - pandas_read["TOA(ns)"][102:402]))
            # plt.subplot(5, 2, 2)
            # plt.plot((pandas_read["TOA(ns)"][1001:1101] - pandas_read["TOA(ns)"][1000:1100]))
            #这里抽连续100个数据 / 全部数据，进行分析

            plt.subplot(4, 2, 1)
            plt.title('A')
            plt.plot(pandas_read["A"][100:200])
            plt.subplot(4, 2, 2)
            plt.plot(pandas_read["A"])

            plt.subplot(4, 2, 3)
            plt.title('B')
            plt.plot(pandas_read["B"][100:200])
            plt.subplot(4, 2, 4)
            plt.plot(pandas_read["B"])

            plt.subplot(4, 2, 5)
            plt.title('C')
            plt.plot(pandas_read["C"][100:200])
            plt.subplot(4, 2, 6)
            plt.plot(pandas_read["C"])

            plt.subplot(4, 2, 7)
            plt.title('D')
            plt.plot(pandas_read["D"][100:200])
            plt.subplot(4, 2, 8)
            plt.plot(pandas_read["D"])

            plt.savefig(save_path)
            plt.close()


# -*- coding: utf-8 -*-
"""데이터 분석 및 시각화 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AemXsOW4IvJtt2wG-Bqu3kova404Fqf7
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('height.csv')
df1 = df[(df['nation']=='Korea')|(df['nation']=='Japan')]
ind = np.arange(len(df))
w = 0.3
plt.bar(ind-w/2, df['men'], width=w, label='men', color='b')
plt.bar(ind+w/2, df['women'], width=w,label='women', color='r')
plt.xticks(ind, df1)
plt.ylabel('cm')
plt.xlabel('nations')
plt.legend()
plt.show()
display(df)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('people.csv', encoding='euc-kr')
display(df)
ind = np.arange(len(df))
w = 0.2
plt.bar(ind, df['서울특별시'], width=w, label='Whole', color='b')
plt.bar(ind, df['부산광역시'], width=w,label='Seoul', color='r')
plt.xticks(ind, 지역)
plt.ylim(500000, 11000000)
plt.legend()
plt.ylabel("ㄴ")
plt.show()
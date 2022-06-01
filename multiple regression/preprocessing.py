import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# 애들이 준 데이터 전처리 코드

df = pd.read_csv('/Users/moonsung/Downloads/usingCodeForPaper/dataTest/primitive_data.csv', sep=',')

df.drop(['diravg'], axis=1, inplace=True)
df.drop(['humidcurr'], axis=1, inplace=True)
df.drop(['humidmin'], axis=1, inplace=True)

df = df[df['humidrel'] != 0]
df = df.reset_index(drop=True)
df = df[(np.abs(stats.zscore(df['humidrel'])) < 3)]

df = df[df['raindays'] != 0]
df = df.reset_index(drop=True)
df = df[(np.abs(stats.zscore(df['raindays'])) < 3)]

df = df[df['tempavg'] != 0]
df = df.reset_index(drop=True)
df = df[(np.abs(stats.zscore(df['tempavg'])) < 3)]

df = df[df['windavg'] != 0]
df = df.reset_index(drop=True)
df = df[(np.abs(stats.zscore(df['windavg'])) < 3)]

df = df[df['windmax'] != 0]
df = df.reset_index(drop=True)
df = df[(np.abs(stats.zscore(df['windmax'])) < 3)]

df = df[df['dmgarea'] != 0]
df = df.reset_index(drop=True)
df = df[(np.abs(stats.zscore(df['dmgarea'])) < 3)]

print(df.shape)
print(df.info())
df.to_csv('/Users/moonsung/Downloads/test/dataTest/paper_write_data_total_prepocessing_data.csv', encoding='utf-8')
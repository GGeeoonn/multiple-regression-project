import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pingouin as pg
import scipy.stats as stats
import statsmodels.formula.api as smf

# 애들이 준 데이터에 전처리하고 실행하면 정상작동하는 코드

df = pd.read_csv('/Users/moonsung/Downloads/usingCodeForPaper/dataTest/preprocessing_data.csv', sep=',')
dataset = (df - df.mean())/df.std()
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 5].values

# 추가
res = smf.ols(formula='dmgarea ~raindays', data=df).fit()
print(res.summary())


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red', s=3)
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Dmgarea - raindays')
plt.xlabel('Rain Days')
plt.ylabel('Damaged Area')
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.show()

import pandas as pd

df = pd.read_csv("diabetes.csv")

import matplotlib.pyplot as plt
import seaborn as sns

corr = df.corr()
sns.heatmap(corr, cmap="RdBu", square=True, annot=True)
plt.show()


temp1 = corr["target"]
temp2 = temp1[(abs(temp1) > 0.1) & (abs(temp1) < 1)]
X_col = temp2.index
X = df[X_col]
y = df[["target"]]

from statsmodels.stats.outliers_influence import variance_inflation_factor

for i in X.columns:
    VIF = variance_inflation_factor(X.values, X.columns.get_loc(i))
    if VIF > 10:
        X = X.drop(columns=i)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

from sklearn.linear_model import LinearRegression

lr_model = LinearRegression()
lr_model.fit(x_train, y_train)
coef = lr_model.coef_.round(2)
intercept = lr_model.intercept_.round(2)
print(f"线性回归方程：Y={intercept[0]}{coef[0][0]}X1+{coef[0][1]}X2+{coef[0][2]}X3{coef[0][3]}X4{coef[0][4]}X5+{coef[0][5]}X6+{coef[0][6]}X7+{coef[0][7]}X8")


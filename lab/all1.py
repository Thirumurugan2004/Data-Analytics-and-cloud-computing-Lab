
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

df = pd.read_csv('advertising.csv')
print(df.describe())

def est_coef(x, y):
    n = np.size(x)
    mx = np.mean(x)
    my = np.mean(y)

    SS_xy = np.sum(y * x) - n * my * mx
    SS_xx = np.sum(x * x) - n * mx * mx

    b1 = SS_xy / SS_xx
    b0 = my - b1 * mx
    return b0, b1

df['t'] = df['TV'] + df['radio'] + df['newspaper']
b_s, a_s = est_coef(df['t'], df['sales'])
print(b_s, a_s)

plt.scatter(df['t'], df['sales'], color='m', marker='o', s=30, label='Data')
y_pred_s = b_s + a_s * df['t']
plt.plot(df['t'], y_pred_s, color='g', label=f'Line: y = {a_s:.4f}x + {b_s:.4f}')

plt.xlabel('Total Budget (TV + radio + newspaper)')
plt.ylabel('Sales')
plt.legend()
plt.show()

x = df[['t']]
y = df['sales']
X_tr, X_te, y_tr, y_te = train_test_split(x, y, test_size=0.3, random_state=45)

deg = range(3, 11)
min_m = float('inf')
b_d = None
b_c = None
all_c = []
all_r = []
all_r2 = []

for d in deg:
    poly = PolynomialFeatures(degree=d)
    X_tr_p = poly.fit_transform(X_tr)
    X_te_p = poly.transform(X_te)

    model = LinearRegression()
    model.fit(X_tr_p, y_tr)

    y_pr = model.predict(X_te_p)

    mse = mean_squared_error(y_te, y_pr)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_te, y_pr)

    all_c.append(model.coef_)
    all_r.append(rmse)
    all_r2.append(r2)

    if mse < min_m:
        min_m = mse
        b_d = d
        b_c = model.coef_

print(f"Best Degree: {b_d}")
print(f"Coefficients for Best Degree ({b_d}):\n", b_c)
print("All Coefficients:", all_c)
print("All RMSE:", all_r)
print("All R2:", all_r2)

td = np.array([[186]])  # 149 + 22 + 15
b_d_p = PolynomialFeatures(degree=b_d)
td_p = b_d_p.fit_transform(td)
sales_pr = np.dot(td_p, b_c)

print("Predicted Sales for [149, 22, 15]:", sales_pr)

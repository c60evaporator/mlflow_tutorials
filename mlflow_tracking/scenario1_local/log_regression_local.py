# %%
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import seaborn as sns

# 次数を指定して
def polyregression(n, X, y):
    # テストデータ分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, random_state=42)
    # 多項式変換
    pf = PolynomialFeatures(degree=n)
    pf.fit(X_train)
    X_train_poly = pf.transform(X_train)
    X_test_poly = pf.transform(X_test)
    # 回帰
    lr = LinearRegression()
    lr.fit(X_train_poly, y_train)
    y_pred = lr.predict(X_test_poly)
    # 性能評価
    r2 = r2_score(y_test, y_pred)

for n in range(5):
    data = sns.load_dataset('anscombe')
    data.head()
# %%

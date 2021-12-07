# %% 手順4 実験結果のロギング
import mlflow
import seaborn as sns
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.svm import SVC

# データの読込とチューニング条件の指定
iris = sns.load_dataset("iris")  # irisデータセット取得
OBJECTIVE_VARIALBLE = 'species'  # 目的変数の指定
USE_EXPLANATORY = ['petal_width', 'petal_length', 'sepal_width', 'sepal_length']  # 説明変数の指定
y = iris[OBJECTIVE_VARIALBLE].values # 目的変数
X = iris[USE_EXPLANATORY].values  # 説明変数
estimator = SVC()  # 学習器（サポートベクターマシン）
cv = KFold(n_splits=3, shuffle=True, random_state=42)  # クロスバリデーション（KFold）
scoring = 'f1_micro'  # チューニングに使用するスコア（F1 Micro）
cv_params = {'gamma': [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100],
             'C': [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100]}  # チューニング用のパラメータ

# MLflowによるロギング開始
mlflow.sklearn.autolog()
with mlflow.start_run() as run:
    # グリッドサーチのインスタンス作成
    gridcv = GridSearchCV(estimator, cv_params, cv=cv,
                      scoring=scoring, n_jobs=-1)
    # グリッドサーチ実行
    gridcv.fit(X, y)
    # 最適パラメータの表示
    best_params = gridcv.best_params_
    best_score = gridcv.best_score_
    print(f'最適パラメータ {best_params}\nスコア {best_score}')
# %%

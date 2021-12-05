# %% 手順2 トラッキングサーバの構築
import mlflow
import configparser
import os
cfg = configparser.ConfigParser()
cfg.read('./config.ini', encoding='utf-8')
# 各種パスを指定
TRACKING_URI = cfg['Path']['tracking_uri']
# トラッキングサーバの場所を指定
mlflow.set_tracking_uri(TRACKING_URI)

# %% 手順3 エクスペリメントの作成
# Artifactストレージの場所を指定（Experimentの生成が必要）
ARTIFACT_LOCATION = cfg['Path']['artifact_location']
# Experimentの生成
EXPERIMENT_NAME = 'experiment_anscombe'
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
if experiment is None:  # 当該Experiment存在しないとき、新たに作成
    experiment_id = mlflow.create_experiment(
                            name=EXPERIMENT_NAME,
                            artifact_location=ARTIFACT_LOCATION)
else: # 当該Experiment存在するとき、IDを取得
    experiment_id = experiment.experiment_id

# %% 手順4 実験結果のロギング
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 次数を指定して多項式回帰を実行するメソッド
def poly_regression(n, X, y, ax):
    # テストデータ分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        shuffle=True, random_state=42,
                                                        test_size=0.5)
    # 多項式変換
    pf = PolynomialFeatures(degree=n)
    pf.fit(X_train)
    X_train_poly = pf.transform(X_train)
    X_test_poly = pf.transform(X_test)
    # 回帰
    lr = LinearRegression()
    lr.fit(X_train_poly, y_train)
    y_pred = lr.predict(X_test_poly)
    # R2スコアで性能評価
    r2 = r2_score(y_test, y_pred)
    mlflow.log_metric(f'r2_degree{n}', r2)  # スコアをMetricsとして記録
    # グラフ作成
    X_view = np.linspace(np.amin(X), np.amax(X), 200).reshape(200, 1)
    X_view_poly = pf.transform(X_view)
    y_pred_view = lr.predict(X_view_poly)  # 回帰線を作成
    ax.scatter(X_test.ravel(), y_test)  # テストデータを散布図プロット
    ax.plot(X_view.ravel(), y_pred_view, c='red')  # 回帰線をプロット
    ax.set_title(f'Degree={n}')

# 次数を変えてスコアを評価するメソッド
def validate_degrees(data, dataset_name):
    # Runを開始
    with mlflow.start_run(experiment_id=experiment_id) as run:
        # データセットを選択
        data_selected = data[data['dataset'] == dataset_name]
        X = data_selected['x'].to_numpy().reshape(len(data_selected), 1)
        y = data_selected['y'].to_numpy()
        mlflow.log_param('dataset', dataset_name)  # データセット名をParametersとして記録
        # グラフ用のfig, axesを作成
        fig, axes = plt.subplots(1, 4, figsize=(18, 4))
        # 次数を変えてスコアを評価
        for n in range(1, 5):
            poly_regression(n, X, y, axes[n - 1])
        # グラフをArtifactとして保存
        fig.suptitle(f'Dataset={dataset_name}', size=16)
        mlflow.log_figure(fig, f'figure_{dataset_name}.png')
        plt.show()

# 全てのデータセットでスコアの評価を実行
data = sns.load_dataset('anscombe')
# データセット1の評価
validate_degrees(data, 'I')
# データセット2の評価
validate_degrees(data, 'II')
# データセット3の評価
validate_degrees(data, 'III')
# データセット4の評価
validate_degrees(data, 'IV')
# %%

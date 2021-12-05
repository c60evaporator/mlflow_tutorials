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
# Artifactストレージの場所を指定
ARTIFACT_LOCATION = cfg['Path']['artifact_location']
# Experimentの生成
EXPERIMENT_NAME = 'experiment_simple'
os.makedirs(ARTIFACT_LOCATION, exist_ok=True)
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
if experiment is None:  # 当該Experiment存在しないとき、新たに作成
    experiment_id = mlflow.create_experiment(
                            name=EXPERIMENT_NAME,
                            artifact_location=ARTIFACT_LOCATION)
else: # 当該Experiment存在するとき、IDを取得
    experiment_id = experiment.experiment_id

# %% 手順4 実験結果のロギング
with mlflow.start_run(experiment_id=experiment_id) as run:
    # 実験条件(Parameters)
    mlflow.log_param('x', 1)
    # 評価指標(Metrics)
    mlflow.log_metric('y', 2)
    # その他のデータ(Artifacts)
    features = 'rooms, zipcode, median_price, school_rating, transport'
    mlflow.log_text(features, 'features.txt')
# %%

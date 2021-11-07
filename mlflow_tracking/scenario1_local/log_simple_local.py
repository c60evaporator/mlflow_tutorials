# %% 手順2 トラッキングサーバの構築
import mlflow
import configparser
from mlflow import tracking
cfg = configparser.ConfigParser()
cfg.read('./config.ini', encoding='utf-8')
# 各種パスを指定
TRACKING_URI = cfg['Path']['db_path']
REGISTRY_URI = cfg['Path']['registry_uri']

# トラッキングサーバの場所を指定
mlflow.set_tracking_uri(TRACKING_URI)
# レジストリサーバの場所を指定
mlflow.set_registry_uri(REGISTRY_URI)

# %% 手順3 エクスペリメントの作成
# Artifactストレージの場所を指定（Experimentの生成が必要）
ARTIFACT_LOCATION = cfg['Path']['artifact_location']
# Experimentの生成
EXPERIMENT_NAME = 'experiment_simple'
experiment_id = mlflow.get_experiment_by_name(EXPERIMENT_NAME)  # 当該Experiment存在するとき、IDを取得
if experiment_id is None:  # 当該Experiment存在しないとき、新たに作成
    experiment_id = mlflow.create_experiment(
                            name=EXPERIMENT_NAME,
                            artifact_location=ARTIFACT_LOCATION)

with mlflow.start_run(experiment_id=experiment_id):
    # 実験条件(Parameters)
    mlflow.log_param("x", 1)
    # 評価指標(Metrics)
    mlflow.log_metric("y", 2)
    # その他のデータ(Artifacts)
    features = "rooms, zipcode, median_price, school_rating, transport"
    mlflow.log_text(features, "features.txt")
# %%

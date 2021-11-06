# %% 手順2 トラッキングサーバの構築
import mlflow
import configparser
cfg = configparser.ConfigParser()
cfg.read('./config.ini', encoding='utf-8')
# トラッキングサーバの場所を指定
tracking_uri = cfg['Path']['tracking_uri']
mlflow.set_tracking_uri(tracking_uri)
# レジストリサーバの場所を指定
registry_uri = cfg['Path']['registry_uri']
mlflow.set_registry_uri(registry_uri)
# アーティファクトストレージの場所を指定（Experimentの生成が必要）
artifact_location = cfg['Path']['artifact_location']
experiment_name = 'experiment1'
# Experimentの生成
experiment_id = mlflow.get_experiment_by_name(experiment_name)
if experiment_id is None:
    experiment_id = mlflow.create_experiment(
                            name=experiment_name,
                            artifact_location=artifact_location)

with mlflow.start_run(experiment_id=experiment_id):
    # 実験条件(Parameters)
    mlflow.log_param("x", 1)
    # 評価指標(Metrics)
    mlflow.log_metric("y", 2)
    # その他のデータ(Artifacts)
    features = "rooms, zipcode, median_price, school_rating, transport"
    mlflow.log_text(features, "features.txt")
# %%

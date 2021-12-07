# %% 手順2 トラッキングサーバの構築
import mlflow
import configparser
cfg = configparser.ConfigParser()
cfg.read('./config.ini', encoding='utf-8')
# 各種パスを指定
TRACKING_URI = cfg['Path']['tracking_uri']

# トラッキングサーバの場所を指定
mlflow.set_tracking_uri(TRACKING_URI)

# %% 手順3 エクスペリメントの作成
# Experimentの生成 (artifact_locationはDockerfileのコマンドで指定しているので不要)
EXPERIMENT_NAME = 'experiment_simple'
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
if experiment is None:  # 当該Experiment存在しないとき、新たに作成
    experiment_id = mlflow.create_experiment(
                            name=EXPERIMENT_NAME)
else: # 当該Experiment存在するとき、IDを取得
    experiment_id = experiment.experiment_id

# %% 手順4 実験結果のロギング
with mlflow.start_run(experiment_id=experiment_id):
    # 実験条件(Parameters)
    mlflow.log_param('x', 1)
    # 評価指標(Metrics)
    mlflow.log_metric('y', 2)
    # その他のデータ(Artifacts)
    features = 'rooms, zipcode, median_price, school_rating, transport'
    mlflow.log_text(features, 'features.txt')

# %%

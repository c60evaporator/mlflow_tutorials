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
    mlflow.log_param("x", 1)
    # 評価指標(Metrics)
    mlflow.log_metric("y", 2)
    # その他のデータ(Artifacts)
    features = "rooms, zipcode, median_price, school_rating, transport"
    mlflow.log_text(features, "features.txt")

    # from mlflow.tracking.client import MlflowClient
    # from mlflow.tracking.fluent import _get_or_start_run
    # import os
    # import shutil
    # run_id = _get_or_start_run().info.run_id
    # text = features
    # artifact_file = "features.txt"
    # with open(artifact_file, "w") as f:
    #     f.write(text)

    # local_path = artifact_file
    # artifact_path = None
    # mlclient = MlflowClient()
    
    # ###### mlflow/tracking/_tracking_service/client.py in log_artifact
    # artifact_repo = mlclient._tracking_client._get_artifact_repo(run_id)
    # if os.path.isdir(local_path):
    #     dir_name = os.path.basename(os.path.normpath(local_path))
    #     path_name = (
    #         os.path.join(artifact_path, dir_name) if artifact_path is not None else dir_name
    #     )
    #     artifact_repo.log_artifacts(local_path, path_name, artifact_path)
    # #else:
    #     #artifact_repo.log_artifact(local_path, artifact_path)

    # ###### mlflow/utils/file_utils.py in mkdir
    # import errno
    # def mkdir(root, name=None):
    #     target = os.path.join(root, name) if name is not None else root
    #     try:
    #         os.makedirs(target)
    #     except OSError as e:
    #         if e.errno != errno.EEXIST or not os.path.isdir(target):
    #             raise e
    #     return target

    # ###### mlflow/store/artifact/local_artifact_repo.py in log_artifact
    # if artifact_path:
    #         artifact_path = os.path.normpath(artifact_path)
    # artifact_dir = (
    #     os.path.join(artifact_repo.artifact_dir, artifact_path) if artifact_path else artifact_repo.artifact_dir
    # )
    # if not os.path.exists(artifact_dir):
    #     mkdir(artifact_dir)
    # shutil.copyfile(local_path, os.path.join(artifact_dir, os.path.basename(local_path)))

# %%

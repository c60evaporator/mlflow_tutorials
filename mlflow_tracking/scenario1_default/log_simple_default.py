# %% 手順4: 実験結果の記録（デフォルト設定）
import mlflow

with mlflow.start_run() as run:
    # 実験条件(Parameters)
    mlflow.log_param('x', 1)
    # 評価指標(Metrics)
    mlflow.log_metric('y', 2)
    # その他のデータ(Artifacts)
    features = 'rooms, zipcode, median_price, school_rating, transport'
    mlflow.log_text(features, 'features.txt')

# %% デフォルトの保存場所を表示（実行フォルダ直下のmlrunsフォルダ）
import mlflow
# トラッキングサーバの場所
tracking_uri = mlflow.get_tracking_uri()
print('Current tracking uri: {}'.format(tracking_uri))
# レジストリサーバの場所
mr_uri = mlflow.get_registry_uri()
print('Current model registry uri: {}'.format(mr_uri))
# アーティファクトストレージの場所
artifact_uri = mlflow.get_artifact_uri()
print('Current artifact uri: {}'.format(artifact_uri))

# %%

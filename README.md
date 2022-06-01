# mlflow_tutorials
[MLflow公式ドキュメント](https://mlflow.org/docs/latest/tracking.html#concepts)の**4種類のシナリオ**を再現するサンプルコードです

## 各シナリオの概要
詳細は[こちらのQiita記事]()を参照ください

|シナリオ　|英名|トラッキングサーバ|バックエンド|アーティファクトストレージ|
|---|---|---|---|---|
|1|MLflow on localhost|ローカルに自動生成|ローカルストレージ|ローカルストレージ|
|2|MLFlow on localhost with SQLite|ローカルに自動生成|ローカルDB|ローカルストレージ|
|3|MLflow on localhost with Tracking Server|ローカルに手動ホスティング|ローカルDB or ストレージ|ローカルストレージ|
|4|MLflow with remote Tracking Server, backend and artifact stores|リモートサーバ|リモートDB|リモートストレージ|

・シナリオ1構成図
![scenario_1.png](https://mlflow.org/docs/latest/_images/scenario_1.png)

・シナリオ2構成図
![scenario_2.png](https://mlflow.org/docs/latest/_images/scenario_2.png)

・シナリオ3構成図

　![image](https://user-images.githubusercontent.com/59557625/144874438-d32afab5-d436-4099-84f4-512c73ff5c47.png)

・シナリオ4構成図

　![image](https://user-images.githubusercontent.com/59557625/144874860-69dcfbdb-3d73-442d-beaf-ac1744c122a7.png)

## サンプルコードの構成
サンプルコードは以下のような構成となっています。

||シナリオ1<br>(デフォルト設定)|シナリオ1<br>(別フォルダ指定)|シナリオ2|シナリオ3|シナリオ4|
|---|---|---|---|---|---|
|サーバ側のフォルダ|[/scenario1_default](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario1_default)|[/scenario1_local](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario1_local)|[/scenario2_sqlite](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario2_sqlite)|[/scenario3_trackingserver /server](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario3_trackingserver/server)|[/scenario4_remote /server](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario4_remote/server)|
|クライアント側のフォルダ　　　　　　|サーバ側と同じ|サーバ側と同じ|サーバ側と同じ|[/scenario3_trackingserver /client](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario3_trackingserver/client)|[/scenario4_remote /client](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario4_remote/client)|
|コード実行例<br>（ロギングのみ）|[a_log_simple_default.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario1_default/a_log_simple_default.py)|[a_log_simple_local.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario1_local/a_log_simple_local.py)|[a_log_simple_sqlite.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario2_sqlite/a_log_simple_sqlite.py)|[a_log_simple_trackingserver.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario3_trackingserver/client/a_log_simple_trackingserver.py)|[a_log_simple_remote.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario4_remote/client/a_log_simple_remote.py)|
|コード実行例<br>（多項式回帰の次数）|[b_log_anscombe_default.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario1_default/b_log_anscombe_default.py)|[b_log_anscombe_local.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario1_local/b_log_anscombe_local.py)|[b_log_anscombe_sqlite.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario2_sqlite/b_log_anscombe_sqlite.py)|[b_log_anscombe_trackingserver.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario3_trackingserver/client/b_log_anscombe_trackingserver.py)|[b_log_anscombe_remote.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario4_remote/client/b_log_anscombe_remote.py)|
|コード実行例<br>（パラメータチューニング）|[c_log_tuning_default.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario1_default/c_log_tuning_default.py)|[c_log_tuning_local.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario1_local/c_log_tuning_local.py)|[c_log_tuning_sqlite.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario2_sqlite/c_log_tuning_sqlite.py)|[c_log_tuning_trackingserver.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario3_trackingserver/client/c_log_tuning_trackingserver.py)|[c_log_tuning_remote.py](https://github.com/c60evaporator/mlflow_tutorials/blob/master/mlflow_tracking/scenario4_remote/client/c_log_tuning_remote.py)|

シナリオ3、シナリオ4では、サーバ側のDocker Composeを`docker-compose run`で立ち上げた状態で、クライアント側のコードを実行してください

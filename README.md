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
|サーバ側のフォルダ|[/mlflow_tracking /scenario1_default](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario1_default)|[/mlflow_tracking /scenario1_local](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario1_local)|[/mlflow_tracking /scenario2_sqlite](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario2_sqlite)|[/mlflow_tracking /scenario3_trackingserver /server](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario3_trackingserver/server)|[/mlflow_tracking /scenario4_remote /server](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario4_remote/server)|
|クライアント側のフォルダ　　　　　　　|サーバ側と同じ|サーバ側と同じ|サーバ側と同じ|[/mlflow_tracking /scenario3_trackingserver /client](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario3_trackingserver/client)|[/mlflow_tracking /scenario4_remote /client](https://github.com/c60evaporator/mlflow_tutorials/tree/master/mlflow_tracking/scenario4_remote/client)|
|コード実行例<br>（ロギングのみ）|||||
|コード実行例<br>（多項式回帰の次数）|||||
|コード実行例<br>（パラメータチューニング）|||||

シナリオ3、シナリオ4では、サーバ側のDocker Composeを`docker-compose run`で立ち上げた状態で、クライアント側のコードを実行してください

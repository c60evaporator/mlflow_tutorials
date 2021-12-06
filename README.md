# mlflow_tutorials
[MLflow公式ドキュメント](https://mlflow.org/docs/latest/tracking.html#concepts)の**4種類のシナリオ**を再現するサンプルコードです

|シナリオ|英名|トラッキングサーバ|バックエンド|アーティファクトストレージ|
|---|---|---|---|---|
|1|MLflow on localhost|ローカルに自動生成|ローカルストレージ|ローカルストレージ|
|2|MLFlow on localhost with SQLite|ローカルに自動生成|ローカルDB|ローカルストレージ|
|3|MLflow on localhost with Tracking Server|ローカルに手動ホスティング|ローカルDB or ストレージ|ローカルストレージ|
|4|MLflow with remote Tracking Server, backend and artifact stores|リモートサーバ|リモートDB|リモートストレージ|

以下のようなフォルダ構成となっています。


||シナリオ1<br>(デフォルト設定)|シナリオ1<br>(別フォルダ指定)|シナリオ2|シナリオ3|シナリオ4|
|---|---|---|---|---|---|
|サーバ側のフォルダ|[/mlflow_tracking/scenario1_default]()|[/mlflow_tracking/scenario1_local]()|[/mlflow_tracking/scenario2_sqlite]()|[/mlflow_tracking/scenario3_trackingserver/server]()|[/mlflow_tracking/scenario4_remote/server]()|
|クライアント側のフォルダ|サーバ側と同じ|サーバ側と同じ|サーバ側と同じ|[/mlflow_tracking/scenario3_trackingserver/client]()|[/mlflow_tracking/scenario4_remote/client]()|
|コード実行例<br>（ロギングのみ）|||||
|コード実行例<br>（多項式回帰の次数）|||||
|コード実行例<br>（パラメータチューニング）|||||

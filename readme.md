# 24 卒黒岩研究室 連想ゲーム開発

研究で利用するデータを収集するために連想ゲームを開発する

# 環境構築

## .env ファイルの作成

関係者から.env ファイルを譲り受けて、一番上の階層に配置する。

## コンテナ作成と起動

docker-compose で**Django + MySQL**の環境を構築する。
まずは、build する。`docker-compose.yml`等を変更しない限り 1 回やればで良い。

```
docker compose build
```

まず、データベース側のコンテナを立ち上げる

```
docker compose up -d db
```

その後、django アプリケーション側のコンテナを立ち上げる。

```
docker compose up -d web
# `web`はあってもなくても良い
```

うまくいってるかどうかは`docker-compose ps`でコンテナの状態を見れる。

```
% docker compose ps
NAME                               COMMAND                  SERVICE             STATUS              PORTS
shapley_association_game-db-1      "docker-entrypoint.s…"   db                  running             3306/tcp, 33060/tcp
shapley_association_game-web-1     "python3 manage.py r…"   web                 running             0.0.0.0:8000->8000/tcp
```

## データベースの準備

Django の`models.py`をデータベースに反映させるため`migrate`する。

```
docker compose exec web bash -c "python3 manage.py migrate"
```

これでデータベース関連の前準備は一応完了。
開発者向け: superuser とかも作っておくと便利なので[discussions](https://github.com/tomishima2904/shapley_association_game/discussions/14)の内容を参考に superuser も作ってみよう。

## 連想ゲームへのアクセス

下記の URL をブラウザに貼り付けてアクセス。
`http://0.0.0.0:8000/`もしくは`http://localhost:8000/`

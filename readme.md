# 24卒黒岩研究室 連想ゲーム開発
研究で利用するデータを収集するために連想ゲームを開発する

# 環境構築
docker-composeで**Django + MySQL + React**の環境を構築する。
まずは、buildする。`docker-compose.yml`等を変更しない限り1回やればで良い。
```
docker-compose build
```
そして、upする。うまくいかない場合は先にデータベース側のコンテナを立ち上げよう。
```
docker-compose up -d

# うまくいかない場合は先に以下のコマンドを実行するといいかも
docker-compose up -d db
```
うまくいってるかどうかは`docker-compose ps`でコンテナの状態を見れる。
パッケージの依存関係で`front`のコンテナに不具合が生じる場合は`docker-compose.yml`の`command`のところでいろいろ解消してみよう。
```
% docker-compose ps
NAME                               COMMAND                  SERVICE             STATUS              PORTS
shapley_association_game-db-1      "docker-entrypoint.s…"   db                  running             3306/tcp, 33060/tcp
shapley_association_game-front-1   "docker-entrypoint.s…"   front               running             0.0.0.0:3000->3000/tcp
shapley_association_game-web-1     "python3 manage.py r…"   web                 running             0.0.0.0:8000->8000/tcp
```

うまくいったらブラウザのアドレスバーに以下を貼り付けてアクセスする。
- Django: `http://0.0.0.0:8000/`もしくは`http://localhost:8000/`
- React: `http://0.0.0.0:3000/`もしくは`http://localhost:3000/`


# Gitの運用方法
[gitflow](https://qiita.com/katsunory/items/252c5fd2f70480af9bbb)という運用方法で行う。
この方法では基本的に`master`ではなく`develop`ブランチへpush等を行う。
## cloneする
リモートリポジトリの内容をローカルにコピーしよう。
```
git clone git@github.com:tomishima2904/shapley_association_game.git
```

## ブランチを移動・作成する
まずは、`develop`ブランチを作成して、移動する。
```
# git checkout -b develop/バージョン名
git checkout -b develop/1
```
次にリモートにある`develop`ブランチをpullする。
```
# git pull origin リモートのブランチ名:ローカルのブランチ名
git pull origin develop/1:develop/1
```
次に個人作業するブランチを作成して移動する。`feature/`の後にブランチ名は自分が何をやっているのかわかるような名前にする。
```
# git checkout -b feature/developから派生しているバージョン名/機能名
git checkout -b feature/1/tpl_index
```

## タスクが終わったら
リモートリポジトリにpushする。
```
git push origin feature/1/tpl_index
```
Githubのページに行ってプルリクエストを作成する。merge先は必ず`develop`ブランチで。そしたら富島等にレビューを頼む。

# 参考文献
[[1] Django + MySQLで開発をするときにやること](https://qiita.com/tomi2904/items/cc2b33bd8c16c26e4460)
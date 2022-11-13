# 24卒黒岩研究室 連想ゲーム開発
研究で利用するデータを収集するために連想ゲームを開発する

# 環境構築
docker-composeで**Django + MySQL**の環境を構築する。
まずは、buildする。`docker-compose.yml`等を変更しない限り1回やればで良い。
```
docker-compose build
```
そして、upする。うまくいかない場合は先にデータベース側のコンテナを立ち上げよう。
```
docker-compose up

# うまくいかない場合は先に以下のコマンドを実行する
docker-compose up -d db
```
うまくいったらブラウザのアドレスバーに`http://0.0.0.0:8000/`もしくは`http://localhost:8000/`を貼り付ける。

# Gitの運用方法
[gitflow](https://www.atlassian.com/ja/git/tutorials/comparing-workflows/gitflow-workflow)という運用方法で行う。
この方法では基本的に`master`ではなく`develop`ブランチへpush等を行う。
## cloneする
リモートリポジトリの内容をローカルにコピーしよう。
```
git clone git@github.com:tomishima2904/shapley_association_game.git
```

## ブランチを移動・作成する
まずは、`develop`ブランチを作成して、移動する。
```
git checkout -b develop/1
```
次にリモートにある`develop`ブランチをpullする。
```
git pull origin develop/1:develop/1
# git pull origin リモートのブランチ名:ローカルのブランチ名
```
次に個人作業するブランチを作成して移動する。`feature/`の後にブランチ名は自分が何をやっているのかわかるような名前にする。
```
git checkout -b feature/frontend
```

## タスクが終わったら
リモートリポジトリにpushする。
```
git push origin feature/frontend
```
Githubのページに行ってプルリクエストを作成する。merge先は必ず`develop`ブランチで。そしたら富島等にレビューを頼む。

# 参考文献
[[1] Django + MySQLで開発をするときにやること](https://qiita.com/tomi2904/items/cc2b33bd8c16c26e4460)
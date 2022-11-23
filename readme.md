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

# React環境構築
docker-composeで**Django+MySQL+React**の環境を構築する。
コンテナを起動する前にReactアプリを作成する。（すでに作成したものをgitに置いてあるので、実行しなくても問題ないと思う）
```
docker-compose run --rm front sh -c "npm install -g create-react-app && create-react-app django_front"
```
そして、起動させる
```
docker-compose up -d front
Creating django_react_front_1 ... done ←こうなったら成功
```
以下を実行すると、現在の立ち上がっているコンテナの内容がわかる
```
docker-compose ps
```

問題なく起動されたら`http://localhost:3000/`にアクセスし、Reactの画面が表示されれば成功。

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
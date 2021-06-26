# learn-linux-scraping
linux学習系webサイトから3日に1度朝9時に、記事をランダムに取得しslackに表示する。

## ディレクトリ構成
```
learn-linux-scraping/
├── docker-compose.yml
├── Dockerfile              # pythonの動作コンテナ requests_to_slack 用Dockerfile
├── README.md
└── requests_to_slack
    ├── main.py             # main関数
    ├── post_to_slack.py    # 投稿するデータを辞書形式で受け取り、json形式でslackへ投稿するメソッド
    ├── scraping.py         # 指定URLからのスクレイピング、及びpost_to_slack.pyに渡す辞書の整形メソッド
    └── settings_sample.py  # slack webhook URLの格納用ファイル
```

## 使い方
1. リポジトリのclone後docker-composeでコンテナ立ち上げ
2. `settings_sample.py` にslack webhook URLを記載し、`settings.py` に名前を変える

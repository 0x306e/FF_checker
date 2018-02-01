# FF_Checker.py
## なにこれ
  REST叩いてFollowing/Follower状態の変化, ついでにScreen Nameの変化も調べてくれるやつです.

## 使い方
  1. Python3.6.0以上をインストールします
  1. Consumer key, Consumer secretをそれぞれ取得し, settings.jsonに保存します
  1. add_account.py を実行し, Twitter Authorizationで得たPINコードを入力します
  1. ff_checker.py を実行すると, 変化があった場合にダイレクトメッセージで通知します

  定期的に実行したいのであれば, タスクスケジューラ, cron等を利用してください.

## ライセンス
  MITです.

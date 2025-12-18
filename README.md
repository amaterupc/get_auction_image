# ヤフオク画像ダウンローダー

ヤフオクの商品ページから画像を自動でダウンロードするためのPythonスクリプトです。

## 必要条件

- Python 3.x
- `requests`
- `beautifulsoup4`

## インストール

必要なライブラリをインストールしてください：

```bash
pip install requests beautifulsoup4
```

## 使い方

1. `get_auction_image.py` 内の `url` 変数をダウンロードしたいオークションページのURLに書き換えます。
2. スクリプトを実行します：

```bash
python get_auction_image.py
```

画像は `yahoo_images` フォルダ内に保存されます。

## 英語版 (English version)

See [README_EN.md](./README_EN.md).

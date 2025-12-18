# ヤフオク画像ダウンローダー

ヤフオクの商品ページから画像を自動でダウンロードするためのツールです。

## 使い方（推奨）

シェルスクリプトを使用すると、Python仮想環境のセットアップと実行を自動で行います。

```bash
./get_auction_image.sh <ヤフオク商品ページのURL>
```

画像は `yahoo_images` フォルダ内に保存されます。

## 直接実行する場合

### 必要条件

- Python 3.x
- `requests`
- `beautifulsoup4`

### セットアップ

```bash
pip install requests beautifulsoup4
```

### 実行

```bash
python get_auction_image.py <ヤフオク商品ページのURL>
```

## 英語版 (English version)

See [README_EN.md](./README_EN.md).

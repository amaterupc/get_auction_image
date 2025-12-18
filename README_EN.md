# Yahoo Auction Image Downloader

A simple Python script to download images from a Yahoo Japan Auction page.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

## Installation

```bash
pip install requests beautifulsoup4
```

## Usage

Edit the `url` variable in `get_auction_image.py` to the auction page you want to download images from, then run:

```bash
python get_auction_image.py
```

The images will be saved in a folder named `yahoo_images`.

# Yahoo Auction Image Downloader

A tool to download images from a Yahoo Japan Auction page.

## Usage (Recommended)

Using the shell script will automatically set up the Python virtual environment and run the script.

```bash
./get_auction_image.sh <Yahoo Auction URL>
```

Images will be saved in the `yahoo_images` folder.

## Running Directly

### Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

### Setup

```bash
pip install requests beautifulsoup4
```

### Execution

```bash
python get_auction_image.py <Yahoo Auction URL>
```

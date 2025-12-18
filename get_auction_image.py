import requests
from bs4 import BeautifulSoup
import urllib.parse
import os

# URL of the page
url = "https://page.auctions.yahoo.co.jp/jp/auction/o1146778518"

print(f"Fetching page: {url}")
# Send a GET request to the page
response = requests.get(url)
print(f"Response status code: {response.status_code}")

# Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all images with the specified class
img_tags = soup.find_all('img', class_='ProductImage__image is-off')
print(f"Found {len(img_tags)} images with class 'ProductImage__image'")

# Create a directory to save images
if not os.path.exists('yahoo_images'):
    os.makedirs('yahoo_images')
    print("Created directory 'yahoo_images'")

# Download and save each image
for img in img_tags:
    img_url = img.get('src')
    if img_url:
        # Convert relative URLs to absolute URLs
        img_url = urllib.parse.urljoin(url, img_url)
        print(f"Downloading image: {img_url}")
        # Get the image filename
        img_name = os.path.join('yahoo_images', os.path.basename(img_url))
        # Download and save the image
        with open(img_name, 'wb') as f:
            f.write(requests.get(img_url).content)
        print(f"Downloaded: {img_name}")

print("Download complete!")


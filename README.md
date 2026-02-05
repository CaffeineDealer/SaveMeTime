# SaveMeTime
Quick scripts to check inventory/stock data from various websites.
Current implementation covers Microcenter 

## Purpose
Educational project to learn web scraping and save time checking product availability across multiple stores.

## Current Scripts
- **main.py** - Check MicroCenter product stock across all locations

## Installation
Requires: 'uv'
```bash
uv venv
uv sync
```

## Usage
```bash
# Activate virtual environment
cd /path/to/repo
source .venv/bin/activate

# Run the script (find the PRODUCT_ID in the URL)
python main.py microcenter PRODUCT_ID

```

## Disclaimer
For educational purposes only. Please respect website terms of service and rate limits.

## Future
More scripts will be added for other retailers.
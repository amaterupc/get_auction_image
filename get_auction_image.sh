#!/bin/bash

# Determine the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Virtual environment directory name
VENV_DIR=".venv"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Install dependencies (only if they aren't already installed or to ensure they are up to date)
# Using -q for quiet installation
echo "Checking dependencies..."
pip install -q requests beautifulsoup4

# Run the Python script with all passed arguments
python3 get_auction_image.py "$@"

# Deactivate the virtual environment
deactivate

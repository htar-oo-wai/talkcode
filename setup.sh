#!/bin/bash
# Ensure we're in the project directory
echo "Starting setup and running the project..."

# Step 1: Check if virtual environment exists, create if it doesn't
if [ ! -d "venv" ]; then
    echo "Creating a virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Step 2: Activate virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate
# source .env
# Step 3: Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install --upgrade pip  # Ensure pip is up to date
pip install -r requirements.txt

echo "Starting the app: Serving at http://127.0.0.1:7860"
watchfiles "python app.py"

# End of the script
echo "Process completed successfully!"
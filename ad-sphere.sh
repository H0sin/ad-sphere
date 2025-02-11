#!/bin/bash

# Print the start message
echo "Starting installation......"

# Install Git if it's not already installed
echo "Checking if Git is installed..."
if ! command -v git &> /dev/null
then
    echo "Git not found. Installing Git..."
    sudo apt-get install -y git
else
    echo "Git is already installed."
fi

# Ask for the Git repository URL
echo "Please enter the Git repository URL:"
read GIT_REPO_URL

# Clone the project from the provided Git repository
echo "Cloning the project from the Git repository..."
git clone $GIT_REPO_URL

# Change to the project directory (assuming the project folder is the same as the repo name)
PROJECT_DIR=$(basename "$GIT_REPO_URL" .git)
cd $PROJECT_DIR

# Update package list and install necessary packages
echo "Updating package list..."
sudo apt-get update -y

# Install Python 3 and pip (if not already installed)
echo "Installing Python 3 and pip..."
sudo apt-get install -y python3 python3-pip python3-venv

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip3 install -r requirements.txt

# Check if the .env file exists, and create it if not
if [ ! -f ".env" ]; then
    echo ".env file not found. Creating a new one..."
    touch .env
else
    echo ".env file already exists. Modifying it..."
fi

# Function to prompt for values if they are missing in .env
prompt_if_missing() {
    VAR_NAME=$1
    DEFAULT_VALUE=$2

    # Check if the variable already exists in the .env file
    if ! grep -q "^$VAR_NAME=" .env; then
        # If not, prompt the user for input
        echo "Please enter your $VAR_NAME (default: $DEFAULT_VALUE):"
        read VALUE
        # If no input is provided, use the default value
        if [ -z "$VALUE" ]; then
            VALUE=$DEFAULT_VALUE
        fi
        # Add the variable to the .env file
        echo "$VAR_NAME=$VALUE" >> .env
    else
        echo "$VAR_NAME is already set. Skipping."
    fi
}

# Prompt for missing values in .env
prompt_if_missing "TELEGRAM_API_ID" "your_default_api_id"
prompt_if_missing "TELEGRAM_API_HASH" "your_default_api_hash"
prompt_if_missing "TELEGRAM_PHONE_NUMBER" "your_default_phone_number"
prompt_if_missing "MESSAGE_TO_SEND" "Hello! This is an automated message."
prompt_if_missing "USER_FILE_PATH" ""

# Print the success message
echo "Installation complete. You can now run the bot using 'python3 main.py'."

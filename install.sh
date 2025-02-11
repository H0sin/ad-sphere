#!/bin/bash

# Print the start message
echo "Starting installation......"

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

    # Prompt the user to input their Telegram API details
    echo "Please enter your TELEGRAM_API_ID:"
    read TELEGRAM_API_ID
    echo "Please enter your TELEGRAM_API_HASH:"
    read TELEGRAM_API_HASH
    echo "Please enter your TELEGRAM_PHONE_NUMBER:"
    read TELEGRAM_PHONE_NUMBER

    # Add the Telegram API configuration to the .env file
    echo "TELEGRAM_API_ID=$TELEGRAM_API_ID" >> .env
    echo "TELEGRAM_API_HASH=$TELEGRAM_API_HASH" >> .env
    echo "TELEGRAM_PHONE_NUMBER=$TELEGRAM_PHONE_NUMBER" >> .env
    echo "MESSAGE_TO_SEND='Hello! This is an automated message.'" >> .env
    echo "USER_FILE_PATH='' # Optional" >> .env

    echo ".env file created and configuration added."
else
    echo ".env file already exists. Skipping .env file creation."
fi

# Print the success message
echo "Installation complete. You can now run the bot using 'python3 main.py'."

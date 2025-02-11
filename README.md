# Automated Telegram Message Sender

This project allows you to send automated messages to users on Telegram using the Telethon library. The messages are sent to a list of users retrieved from a file or an API.

# Requirements

Before running the project, ensure that the following dependencies are installed:

- Python 3.6 or higher
- `pip`
- Telegram API credentials

# How to Obtain Telegram API Key and API Hash

To interact with Telegram's API, you'll need to obtain an **API Key** and **API Hash**. These are unique credentials that allow your application to connect with Telegram services. Here's a step-by-step guide to get them.

## Step-by-Step Guide

### 1. Visit the Telegram Developer Portal
Go to the [Telegram Developer Portal](https://my.telegram.org/auth) in your web browser.

### 2. Log in to Your Telegram Account
Log in to your Telegram account using your phone number. You'll receive a verification code that you need to enter to proceed.

### 3. Create a New Telegram Application
Once you're logged in, you need to create a new application in the Developer Portal to get your **API Key** and **API Hash**.

- Click on **API development tools** in the menu.
- You'll be redirected to a page where you can create a new application.
- Click on the **Create New Application** button.

### 4. Fill in the Application Details
Provide the necessary details for your new application:
- **App title**: Name your application (e.g., `Telegram Message Sender`).
- **Short name**: Provide a short name (for example, `telegram-bot`).
- **URL**: You can leave this blank or put your website URL (if applicable).
- **Platform**: Choose the platform (e.g., Android, iOS, or Web).
- **Description**: Optionally, you can add a description of your app.

Once you fill in these details, click on **Create Application**.

### 5. Retrieve Your API Key and API Hash
After your application is created, you'll see your **API Key** and **API Hash** displayed on the screen.

- **API Key**: This is your unique application identifier.
- **API Hash**: This is the secret key used to authenticate your application.

### 6. Store API Key and API Hash in Your Project
Now that you have your **API Key** and **API Hash**, you can store them in your project's `.env` file.

Create a `.env` file in your project's root directory and add the following lines:


## Installation

To install the project and its dependencies, follow these steps:

### 1. Download and Run the Install Script

```bash
  curl -sSL https://example.com/install.sh -o ad-sphere.sh
```
chmod +x install.sh
./install.sh
This script will:

### 2. Clone the repository

Clone the project repository to your local machine:

```bash
    git clone https://github.com/H0sin/ad-sphere.git
    cd ad-sphere
    python main.py
```

# Configuration Overview

This file describes the configuration parameters that you need to set up in your project. These parameters control various aspects such as the API configuration, Telegram credentials, and other settings.

## Configuration Parameters

### 1. **API Configuration**

- **API_CALLED_ADDRESS**:  
  This is the endpoint URL of the API you want to call.  
  Example:  
  ```bash
    API_CALLED_ADDRESS = test.com
    FIELD_GET_AS_API = telegramUsername
    HTTP_METHOD = GET
    API_SSL = TRUE
    API_TOKEN = ****************************************************************************
    TOKEN_TYPE = BEARER_TOKEN
    TOKEN_PREFIX = BEARER
    USER_FILE_PATH = Users
    
    # Telegram Configuration
    TELEGRAM_API_ID = *******
    TELEGRAM_API_HASH = ************************
    TELEGRAM_PHONE_NUMBER = 0999999999
    MESSAGE_TO_SEND =  your message 
  ```

# Error Handling and Logging for Failed Messages

This guide describes how the application handles errors and logs failed message deliveries to a file named `failed_messages.log`.

## Overview

When the application attempts to send messages via the Telegram API, any errors encountered during the process are captured and logged. These errors may occur due to issues such as invalid user IDs, network problems, or Telegram server errors. If a message cannot be sent successfully, the error message is logged in the `failed_messages.log` file along with the corresponding user ID.

## How the Logging Works

### 1. **Log File**:  
The logs for failed message deliveries are stored in a file called `failed_messages.log`. This file will contain entries with the timestamp of the error, the user ID, and the error message itself.

### 2. **Logging Format**:
Each failed message delivery attempt is logged in the following format:
```bash
  [Timestamp] - UserID - FAILED - Error_Message
```

### Key Features:
- Send messages to users via Telegram.
- Fetch user IDs from a local file or external API.
- Log the status of sent and failed messages.
- Easily configurable via a `.env` file for Telegram API credentials and other settings.
- Works with both individual users and groups.

This bot is useful for bulk messaging, notifications, or any use case where you need to automate communication with users on Telegram.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

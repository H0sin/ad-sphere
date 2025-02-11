from telethon import TelegramClient
import asyncio
import os
from dotenv import load_dotenv
from datetime import datetime
from get_users_list import Request  # Import the previous Request class

# Load environment variables
load_dotenv(dotenv_path=".env")

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE_NUMBER")
message = os.getenv("MESSAGE_TO_SEND", "Default message")
user_file_path = os.getenv("USER_FILE_PATH")  # Path to the user file if defined

# Initialize Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Function to log messages to files
def log_message(file_name, user_id, status):
    """Log the user_id and status (sent or failed) to the specified file."""
    with open(file_name, "a") as file:
        file.write(f"{datetime.now()} - {user_id} - {status}\n")

# Function to get user IDs from file or API
def get_user_ids():
    """Retrieve user IDs from a file or API depending on the environment configuration."""
    if user_file_path and os.path.exists(user_file_path):
        with open(user_file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    else:
        return Request().call_api()

async def send_messages():
    """Send messages to a list of users retrieved from a file or API. Log successful and failed message deliveries."""
    await client.start(phone_number)

    sent_log_file = "sent_messages.log"
    failed_log_file = "failed_messages.log"

    user_ids = get_user_ids()
    if isinstance(user_ids, list):
        for user_id in user_ids:
            try:
                """Fetch the user entity and send the message."""
                entity = await client.get_entity(user_id)
                await client.send_message(entity, message)
                print(f"Message sent to user {user_id}.")
                log_message(sent_log_file, user_id, "SENT")  # Log successful delivery
            except Exception as e:
                """Handle errors during message sending and log failures."""
                print(f"Error sending message to {user_id}: {e}")
                log_message(failed_log_file, user_id, f"FAILED - {e}")  # Log failed delivery
    else:
        async for user_id in user_ids:
            try:
                """Fetch the user entity and send the message."""
                entity = await client.get_entity(user_id)
                await client.send_message(entity, message)
                print(f"Message sent to user {user_id}.")
                log_message(sent_log_file, user_id, "SENT")  # Log successful delivery
            except Exception as e:
                """Handle errors during message sending and log failures."""
                print(f"Error sending message to {user_id}: {e}")
                log_message(failed_log_file, user_id, f"FAILED - {e}")  # Log failed delivery

# Run the Telegram message sending process
with client:
    client.loop.run_until_complete(send_messages())
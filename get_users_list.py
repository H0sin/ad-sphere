import json
import os
import asyncio
from importlib.resources import read_text
from typing import Any, AsyncGenerator

import aiohttp
from dotenv import load_dotenv

import json
import os
import asyncio
from typing import Any, AsyncGenerator

import aiohttp
from dotenv import load_dotenv


class Request:
    def __init__(self):
        """"""
        # Load environment variables from .env file
        """"""
        load_dotenv(dotenv_path=".env")

        """"""
        # Initialize configuration from environment variables
        """"""
        self.API_CALLED_ADDRESS = os.getenv("API_CALLED_ADDRESS")
        self.FIELD_GET_AS_API = os.getenv("FIELD_GET_AS_API")
        self.API_TOKEN = os.getenv("API_TOKEN")
        self.TOKEN_PREFIX = os.getenv("TOKEN_PREFIX")
        self.TOKEN_TYPE = os.getenv("TOKEN_TYPE")
        self.API_SSL = os.getenv("API_SSL", "false").lower() == "true"
        self.HTTP_METHOD = os.getenv("HTTP_METHOD")

    def __generate_url__(self) -> str:
        """"""
        # Generate the full API URL based on SSL configuration
        """"""
        protocol = "https" if self.API_SSL else "http"
        return f"{protocol}://{self.API_CALLED_ADDRESS}"

    async def call_api(self) -> AsyncGenerator[Any, Any]:
        """"""
        # Call the API and yield the results asynchronously
        # Handles both GET and POST methods
        """"""
        try:
            url = self.__generate_url__()

            """"""
            # Set up request headers, including Authorization
            """"""
            headers = {
                "Authorization": f"{self.TOKEN_PREFIX} {self.API_TOKEN}",
            }

            async with aiohttp.ClientSession() as session:
                if self.HTTP_METHOD == "GET":
                    """"""
                    # Perform a GET request and process the response
                    """"""
                    async with session.get(url, headers=headers) as response:
                        results = await response.json()
                        for res in results.get("data", {}).get("entities", []):
                            if res.get(self.FIELD_GET_AS_API):
                                yield res[self.FIELD_GET_AS_API]

                elif self.HTTP_METHOD == "POST":
                    """"""
                    # Perform a POST request and process the response
                    """"""
                    payload = {
                        "query": {
                            "field": self.FIELD_GET_AS_API,
                        }
                    }
                    async with session.post(url, headers=headers, json=payload) as response:
                        results = await response.json()
                        for res in results.get("data", {}).get("entities", []):
                            if res.get(self.FIELD_GET_AS_API):
                                yield res[self.FIELD_GET_AS_API]

        except Exception as e:
            """"""
            # Print any exceptions that occur during the API call
            """"""
            print(f"Error during API call: {e}")


if __name__ == '__main__':
    async def main():
        """"""
        # Initialize the Request class and process API responses
        """"""
        request = Request()

        async for item in request.call_api():
            print(item)


    """"""
    # Run the asynchronous main function
    """"""
    asyncio.run(main())

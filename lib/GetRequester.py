# lib/GetRequester.py
import requests
import json  # Import the json module

class GetRequester:
    def __init__(self, url):
        """
        Initializes the GetRequester with the provided URL.
        """
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the URL and returns the body of the response in bytes.
        """
        response = requests.get(self.url)
        
        # Check if the response was successful
        if response.status_code == 200:
            return response.content  # Return response body as bytes
        else:
            raise Exception(f"Error: Unable to fetch data from {self.url}, status code: {response.status_code}")

    def load_json(self):
        """
        Loads JSON data from the URL by calling get_response_body.
        Returns a Python list or dictionary made up of data converted from the JSON response.
        """
        response_body = self.get_response_body()
        
        # Decode the bytes to a string and then load it as JSON
        return json.loads(response_body.decode('utf-8'))  # Decode bytes and load JSON

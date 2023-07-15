import requests
import json
import argparse
from requests_oauthlib import OAuth1
import os
import sys
import base64


class NounWrapper:


    def __init__(self):
        """Initializes the class instance.
        
        This method is called when a new instance of the class is created. It sets up the authentication for the class instance.
        
        Args:
            self: The class instance.
        
        Returns:
            None
        """
        self.setup_authentication()
        pass

    def setup_authentication(self):
        """Sets up authentication for the function.

        This function retrieves the NOUN_API_KEY and NOUN_API_SECRET from the environment variables and sets them as attributes of the object. It also creates an OAuth1 object for authentication.

        Raises:
            Exception: If either NOUN_API_KEY or NOUN_API_SECRET is not found in the environment variables.

        Returns:
            None
        """
        # store your keys in ~/.bashrc, reload with command:
        # source ~/.bashrc
        try:
            self.NOUN_API_KEY = os.getenv("NOUN_API_KEY")
            self.NOUN_API_SECRET = os.getenv("NOUN_API_SECRET")
            print(f"NOUN_API_KEY,{self.NOUN_API_KEY}")
            print(f"NOUN_API_SECRET,{self.NOUN_API_SECRET}")
            if self.NOUN_API_KEY is None or self.NOUN_API_SECRET is None:
                raise Exception
            self.auth = OAuth1(self.NOUN_API_KEY, self.NOUN_API_SECRET)
        except Exception as e:
            print(
                f"Error: could not find NOUN_API_KEY or NOUN_API_SECRET in environment variables. {e}")
            sys.exit(1)

    def parse_arguments(self):
        """Parses the command line arguments.

        Returns:
            The parsed command line arguments.
        """
        # Create the parser
        parser = argparse.ArgumentParser()
        parser.add_argument('--search', type=str, help='The string to search.')

        # Parse the arguments
        self.args = parser.parse_args(sys.argv[1:])

        return self.args

    def search_icons(self, search_term):
        """Searches for icons using the Noun Project API.

        Args:
            search_term (str): The term to search for icons.

        Returns:
            dict: A dictionary containing the response from the API.

        Raises:
            None

        Example:
            search_icons("cat")
        """
        url = f'https://api.thenounproject.com/v2/icon?query={search_term}&limit_to_public_domain=1&thumbnail_size=42&include_svg=1&limit=1'
        # headers = {'Authorization': f'Bearer {API_KEY}:{API_SECRET}'}
        response = requests.get(url, auth=self.auth)

        if response.status_code != 200:
            print(f'Error retrieving icon: {response.status_code}')
            return None

        return response.json()

    def save_metadata(self, search_term, metadata):
        """Saves the metadata for a given search term.

        Args:
            search_term (str): The search term used to retrieve the metadata.
            metadata (dict): The metadata to be saved.

        Returns:
            None

        Raises:
            IOError: If there is an error while saving the metadata.

        Example:
            save_metadata("apple", {"color": "red", "size": "medium"})
        """
        with open(f'metadata/{search_term}.json', 'w') as f:
            json.dump(metadata, f, indent=4)

    def b64_to_str(self, b64_data) -> str:
        """Converts a base64 encoded string to a regular string.

        Args:
            b64_data (str): The base64 encoded string to be converted.

        Returns:
            str: The converted regular string.
        """
        base64_bytes = b64_data.encode("utf-8")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("utf-8")
        return sample_string

    # Save svg file

    def save_svg_file(self, search_term, icon_id, icon_color='ffffff'):
        """Save an SVG file from the Noun Project API.

        Args:
            search_term (str): The search term used to find the icon.
            icon_id (str): The ID of the icon to download.
            icon_color (str, optional): The color of the icon in hexadecimal format. Defaults to 'ffffff'.

        Returns:
            None

        Raises:
            None

        Example:
            save_svg_file('cat', '12345', 'ff0000')
        """
        formats = ['svg']

        url = f'https://api.thenounproject.com/v2/icon/{icon_id}/download?color={icon_color}&filetype=svg'

        for format in formats:

            # Get the svg file via http request
            response = requests.get(url, auth=self.auth)

            if response.status_code != 200:
                print(
                    f'Error retrieving icon in {format} format: {response.status_code}, [{response.reason}], url: {url}')
                continue

            # Write the svg file
            with open(f'svg/{search_term}.{format}', 'w') as f:
                decoded_data = self.b64_to_str(
                    response.json()['base64_encoded_file'])
                f.write(decoded_data)


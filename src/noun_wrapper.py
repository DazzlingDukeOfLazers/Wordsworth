import requests
import json
import argparse
from requests_oauthlib import OAuth1
import os
import sys


class NounWrapper:
    def __init__(self):
        self.setup_authentication()
        pass

    def setup_authentication(self):
        # store your keys in ~/.bashrc, reload with command:
        # source ~/.bashrc
        self.API_KEY = os.getenv("WORDSWORTH_API_KEY")
        self.API_SECRET = os.getenv("WORDSWORTH_API_SECRET")
        self.auth = OAuth1(self.API_KEY, self.API_SECRET)

    def parse_arguments(self):
        # Create the parser
        parser = argparse.ArgumentParser()
        parser.add_argument('--search', type=str, help='The string to search.')

        # Parse the arguments
        self.args = parser.parse_args(sys.argv[1:])

        return self.args

    def get_icon(self, search_term):
        url = f'https://api.thenounproject.com/v2/icon?query={search_term}&limit_to_public_domain=1&thumbnail_size=42&include_svg=1&limit=1'
        # headers = {'Authorization': f'Bearer {API_KEY}:{API_SECRET}'}
        response = requests.get(url, auth=self.auth)

        if response.status_code != 200:
            print(f'Error retrieving icon: {response.status_code}')
            return None

        return response.json()

    def save_metadata(self, search_term, metadata):
        with open(f'metadata/{search_term}.json', 'w') as f:
            json.dump(metadata, f, indent=4)

    def save_icon_files(self, search_term, icon_url):
        formats = ['svg']

        for format in formats:
            response = requests.get(icon_url)

            if response.status_code != 200:
                print(
                    f'Error retrieving icon in {format} format: {response.status_code}')
                continue

            with open(f'svg/{search_term}.{format}', 'wb') as f:
                f.write(response.content)

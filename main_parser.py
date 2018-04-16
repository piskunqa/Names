import os
import requests


class Parser:
    MAIN_URL = 'https://trademarkia.com/trademarks-search.aspx?tn={0}'

    def parse_file(self):
        with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r') as file:
            return [i.strip() for i in file.readlines()]

    def get_result(self, name):
        response = requests.get(self.MAIN_URL.format(name))
        if 'pricelist' in response.text:
            self.append_result(name)

    def append_result(self, text):
        with open(os.path.join(os.path.dirname(__file__), 'results.txt'), 'a') as file:
            file.write("{0}\n".format(text))

    def clear_results(self):
        with open(os.path.join(os.path.dirname(__file__), 'results.txt'), 'w') as file:
            file.write("")

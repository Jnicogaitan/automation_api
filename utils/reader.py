from random import randrange
import json
import logging


class Reader:

    def __init__(self):
        self.array = []

    def hasData(self):
        length = len(self.array)

        if length > 0:
            return True
        return False

    def Random(self):
        length = len(self.array)

        if length > 0:
            random_index = randrange(0, length - 1) if length > 1 else 0
            return self.array.pop(random_index)

    def load(self, json_file):
        logging.debug('Reader: reading the file')

        try:
            with open(json_file, 'r') as data_file:
                self.array = json.loads(data_file.read())
        except Exception as error:
            logging.debug(f'>>> Reader: No data was loaded, error: {error}')

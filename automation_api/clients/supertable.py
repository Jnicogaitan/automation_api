import os
from pymongo import MongoClient
from automation_api.enums import DevelopmentEnvironments


class SupertableClient:

    def __init__(self):
        self._user = os.environ['USER']
        self._password = os.environ['PASSWORD']
        self._host = os.environ['HOST']
        self._port = os.environ['PORT']
        self._db = os.environ['DB']
        self._url =  f'mongodb://{self._user}:{self._password}@{self._host}:{self._port}/{self._db}'
        self._db_instance = MongoClient(self._url)


    def get_collection(self, environment: DevelopmentEnvironments, collection_name: str):
        assert DevelopmentEnvironments(environment), 'Environment does not exist or not allowed.'
        return self._db_instance[environment.value][collection_name]

    def close(self):
        pass

    def server_info(self):
        pass

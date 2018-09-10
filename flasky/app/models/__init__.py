import json


class BaseModel(object):
    def __init__(self):
        self.id = None

    def json(self):
        return self.__dict__

    @classmethod
    def db_file(cls):
        path = f'flasky/app/data/{cls.__name__}.txt'

        return path

    @classmethod
    def all(cls):
        data = json.load(cls.db_file())

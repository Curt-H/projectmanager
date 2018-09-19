import unittest
from flasky.app.models import BaseModel


class BM(BaseModel):
    def __init__(self, form):
        super().__init__(form)

    @classmethod
    def db_path(cls):
        path = f'{cls.__name__}.txt'
        return path


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        print('Start Testing')

    def tearDown(self):
        print('Testing Finished\n')

    def test_init(self):
        b = BM(dict())
        self.assertEqual(b.id, None)

    def test_json(self):
        b = BM(dict())
        self.assertEqual(b.json(), b.__dict__)

    def test_db_file(self):
        b = BM(dict())
        db_path = 'BM.txt'
        self.assertEqual(b.db_path(), db_path)

    def test_all_save(self):
        with open('BM.txt', 'w', encoding='utf-8') as f:
            f.write('[]')
        b1 = BM(dict())
        b2 = BM(dict())
        b1.save()
        b2.save()
        self.assertEqual(len(b2.all()), 2)


if __name__ == '__main__':
    unittest.main()

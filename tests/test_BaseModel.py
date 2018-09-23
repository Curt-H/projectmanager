import unittest
from flasky.app.models import BaseModel


class BM(BaseModel):
    def __init__(self, form):
        super().__init__(form)
        self.test = form.get('test', 'test')

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

    def test_find(self):
        with open('BM.txt', 'w', encoding='utf-8') as f:
            f.write('[]')

        for i in range(10):
            b = BM(dict())
            b.save()

        m1 = BM.find_by(id=1)
        m2 = BM.find_by(id=100)
        m3 = BM.find_all(test='test')
        m4 = BM.find_all(test='')

        self.assertEqual(m1.id, 1)
        self.assertEqual(m2, None)
        self.assertEqual(len(m3), 10)
        self.assertEqual(m4, [])

    def test_delete(self):
        with open('BM.txt', 'w', encoding='utf-8') as f:
            f.write('[]')

        for i in range(10):
            b = BM(dict())
            b.save()

        BM.delete_by(id=9)
        m3 = BM.all()
        print([m.id for m in BM.all()])
        m4 = BM.delete_by(test='test')

        self.assertEqual(9, len(m3))
        self.assertEqual('删除完成', m4)
        self.assertEqual(0, len(BM.all()))

    def test_new(self):
        with open('BM.txt', 'w', encoding='utf-8') as f:
            f.write('[]')

        form = dict(
            test='pass'
        )

        a = BM.new(form)

        self.assertEqual('pass', a.test)
        self.assertEqual(0, a.id)


if __name__ == '__main__':
    unittest.main()

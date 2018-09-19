import json
import os


def load(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def save(fname, data):
    """
    将数据以json格式输出
    :param fname: 文件名
    :param data: 数据
    :return:  
    """
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(data, f)

    return 0


class BaseModel(object):
    def __init__(self, form):
        self.id = form.get('id', None)

    def json(self):
        return self.__dict__

    @classmethod
    def db_path(cls):
        path = f'../data/{cls.__name__}.txt'

        return path

    @classmethod
    def all(cls):
        """
        读取所有实例
        :return:
        """
        data = load(cls.db_path())
        ms = [cls(m) for m in data]

        return ms

    def save(self):
        """
        将数据保存到文本
        :return:
        """
        is_new = False
        ms = self.all()

        # 确定id, 如果为空, 则是上一位ID号加1, 反则更新对应数据
        if self.id is None:
            if len(ms) == 0:
                self.id = 0
            else:
                self.id = ms[-1].id + 1
            ms.append(self)
        else:
            for m in ms:
                if self.id == m.id:
                    m = self
                else:
                    is_new = True

        data = [m.json() for m in ms]
        print(data)
        state = save(self.db_path(), data)

        if state == 0:
            return 0
        else:
            return 1

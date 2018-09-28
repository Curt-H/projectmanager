import json
import os

from flasky.app import log


def load(fname):
    """
    从txt文件加载JSON数据
    :param fname: 文件名
    :return: JSON字符串
    """
    # Make sure if the file exists
    path = os.path.split(fname)[0]
    if not os.path.exists(path):
        log('原文件不存在, 准备创建')
        os.makedirs(path)
    if not os.path.exists(fname):
        with open(fname, 'w', encoding='utf-8') as f:
            f.write('[]')

    with open(fname, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def save(fname, data):
    """
    将数据以json格式输出
    :param fname: 文件名
    :param data: 数据
    :return: 0
    """
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(data, f)

    return 0


class BaseModel(object):
    def __init__(self, form):
        """
        Model的基类
        :param form:表单数据
        """
        self.id = form.get('id', None)

    def json(self):
        """
        将类的属性以字典形式返回
        :return:
        """
        return self.__dict__

    @classmethod
    def db_path(cls):
        """
        数据存放的位置
        :return: txt的文件位置
        """
        path = f'data\\{cls.__name__}.txt'

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
        ms = self.all()

        # 确定id, 如果为空, 则是上一位ID号加1, 反则更新对应数据
        if self.id is None:
            if len(ms) == 0:
                self.id = 0
            else:
                self.id = ms[-1].id + 1
            ms.append(self)
        else:
            for i, m in enumerate(ms):
                if self.id == m.id:
                    ms[i] = self

        data = [m.json() for m in ms]
        save(self.db_path(), data)

        return self

    @classmethod
    def find_by(cls, **kwargs):
        """
        根据条件查找对应的类数据
        :param kwargs: 不定关键字参数, 可以引用多个条件
        :return: 查找的类, 没找到就返回None
        """
        ms = cls.all()
        is_what_we_find = True

        for m in ms:
            for k, v in kwargs.items():
                if getattr(m, k, None) != v:
                    is_what_we_find = False

            if is_what_we_find:
                return m
            else:
                is_what_we_find = True

        return None

    @classmethod
    def find_all(cls, **kwargs):
        """
        查找符合条件的所有实例
        :param kwargs:
        :return: 查找的类list, 没找到就返回空list
        """
        ms = cls.all()
        is_what_we_find = True
        result = []

        for m in ms:
            for k, v in kwargs.items():
                if getattr(m, k, None) != v:
                    is_what_we_find = False

            if is_what_we_find:
                result.append(m)
            else:
                is_what_we_find = True

        return result

    @classmethod
    def delete_by(cls, **kwargs):
        """
        删除符合条件的所有实例
        :param kwargs:
        :return: '删除完成'
        """
        ms = cls.all()
        delete_list = []

        for i, m in enumerate(ms):
            is_what_we_find = False
            for k, v in kwargs.items():
                if getattr(m, k, None) == v and hasattr(m, k):
                    is_what_we_find = True

            if is_what_we_find:
                delete_list.append(m)

        for m in delete_list:
            ms.remove(m)

        data = [m.json() for m in ms]
        save(cls.db_path(), data)
        return '删除完成'

    @classmethod
    def new(cls, form):
        """
        新建一个实例并储存到数据文件里
        :param form:
        :return:
        """
        m = cls(form)
        m = m.save()

        return m

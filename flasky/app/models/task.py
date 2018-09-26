from flasky.app.models import BaseModel
from flasky.app.util import format_time, log


class Task(BaseModel):
    def __init__(self, form):
        super().__init__(form)
        self.project = form.get('project', '其他')
        self.content = form.get('content', '')
        self.deadline = form.get('deadline', '未指定')

    @classmethod
    def all(cls):
        ts = super().all()
        for i, t in enumerate(ts):
            ts[i].time = format_time(tuple(t.deadline), '%Y-%m-%d')
        return ts

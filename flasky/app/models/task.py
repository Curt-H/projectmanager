from flasky.app.models import BaseModel
from flasky.app.util import format_time, log


class Task(BaseModel):
    def __init__(self, form):
        super().__init__(form)
        self.project = form.get('project', '其他')
        self.content = form.get('content', '')
        self.deadline = format_time(tuple(t.deadline), '%Y-%m-%d')
        self.time = form.get('deadline', '未指定')
        self.finish = form.get('finish', False)

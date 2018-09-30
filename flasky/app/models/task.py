from flasky.app.models import BaseModel
from flasky.app.util import format_time, log


class Task(BaseModel):
    def __init__(self, form):
        super().__init__(form)
        self.project = form.get('project', '其他')
        self.content = form.get('content', '')
        self.deadline = form.get('deadline', '未指定')
        self.time = format_time(tuple(self.deadline), '%Y-%m-%d')
        self.finish = form.get('finish', False)

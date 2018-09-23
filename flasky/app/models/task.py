from flasky.app.models import BaseModel


class Task(BaseModel):
    def __init__(self, form):
        super().__init__(form)
        self.project = form.get('project', '其他')
        self.content = form.get('content', '')
        self.deadline = form.get('deadline', '未指定')

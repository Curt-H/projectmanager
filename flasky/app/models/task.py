from flasky.app.models import BaseModel


class Task(BaseModel):
    def __init__(self, form):
        super().__init__(form)
        self.pn = form.get('pn', None)
        self.type = form.get('type', None)
        self.task_content = form.get('task_content', None)
        self.creat_time = form.get('creat_time', None)  # an int variable
        self.deadline = form.get('deadline', None)  # an int variable
        self.finish = form.get('finish', False)

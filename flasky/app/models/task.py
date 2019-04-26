from flasky.app.models import BaseModel


class Task(BaseModel):
    def __init__(self, form):
        super().__init__(form)
        self.project = form.get('project', '其他')
        self.task_content = form.get('task_content', 'None')
        self.creat_time = form.get('creat_time', '')  # an int variable
        self.deadline = form.get('deadline', '未指定')  # an int variable
        self.finish = form.get('finish', False)

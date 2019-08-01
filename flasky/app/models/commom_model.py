from flasky.app.models import BaseModel


class Work(BaseModel):
    def __init__(self, form):
        super(Work, self).__init__(form)
        self.pn = form.get('pn', None)
        self.type = form.get('type', None)
        self.task_content = form.get('task_content', None)
        self.creat_time = form.get('creat_time', None)  # an int variable
        self.deadline = form.get('deadline', None)  # an int variable
        self.finish = form.get('finish', False)


class Study(BaseModel):
    def __init__(self, form):
        super(Study, self).__init__(form)
        self.lesson = form.get('lesson', None)
        self.progress = form.get('progress', None)
        self.time = form.get('time', None)


class User(BaseModel):
    def __init__(self, form):
        super(User, self).__init__(form)
        self.username = form.get('username')
        self.password = form.get('password')


class Session(BaseModel):
    def __init__(self, form):
        super(Session, self).__init__(form)
        self.user_id = form.get('user_id')
        self.expire_time = form.get('expire_time')

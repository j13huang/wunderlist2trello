class WList(object):

    def __init__(self, json_data):
        self.wid = json_data['id']
        self.title = json_data['title']
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __repr__(self):
        return '{}: {}'.format(self.wid, self.title)

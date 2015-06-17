class WSubtask(object):

    def __init__(self, json_data):
        self.wid = json_data['id']
        self.title = json_data['title']
        self.task_id = json_data['task_id']
        self.completed = json_data['completed']

    def __repr__(self):
        return '{}->{}: {} ({})'.format(self.task_id, self.wid, self.title, self.completed)

class WTask(object):

    def __init__(self, json_data):
        self.wid = json_data['id']
        self.title = json_data['title']
        self.completed = json_data['completed']
        self.list_id = json_data['list_id']
        self.subtasks = []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)
    
    def __repr__(self):
        return '{}: {} ({})'.format(self.wid, self.title, self.completed)

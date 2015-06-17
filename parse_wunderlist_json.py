import wlist
import wtask
import wsubtask
import json
from trello import TrelloClient

def parse_json(filename):
    wunderlist_json = None
    with open(filename, 'r') as f:
        wunderlist_json = json.load(f)

    data = wunderlist_json['data']
    json_lists = data['lists']
    json_tasks = data['tasks']
    json_subtasks = data['subtasks']

    lists = {}
    tasks = {}
    subtasks = {}
    for json_list in json_lists:
        list_obj = wlist.WList(json_list) 
        lists[list_obj.wid] = list_obj
    
    for json_task in json_tasks:
        task_obj = wtask.WTask(json_task) 
        tasks[task_obj.wid] = task_obj
        lists[task_obj.list_id].add_task(task_obj)

    for json_subtask in json_subtasks:
        subtask_obj = wsubtask.WSubtask(json_subtask) 
        subtasks[subtask_obj.wid] = subtask_obj
        tasks[subtask_obj.task_id].add_subtask(subtask_obj)

    for task in tasks.itervalues():
        if not task.completed and not task.title.startswith('#'):
        #if not task.title.startswith('#'):
            print task
            print task.subtasks
            print '--------------'

    #for subtask in subtasks.itervalues():
        #if not subtask.completed and not subtask.title.startswith('#'):
            #print subtask

    #print wunderlist_json
    #import pprint
    #pprint.pprint(tasks)
    #print lists, tasks, subtasks
    return (tasks, subtasks)

if __name__ == '__main__':
    tasks, subtasks = parse_json('wunderlist-2015062-16-44-47.json')




import json

def parse_json(filename):
    wunderlist_json = None
    with open(filename, 'r') as f:
        wunderlist_json = json.load(f)

    print wunderlist_json

if __name__ == '__main__':
    parse_json('wunderlist-2015062-16-44-47.json')




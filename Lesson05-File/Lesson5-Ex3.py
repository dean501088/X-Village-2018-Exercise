import json

with open('SearchShowAction.do.json') as f:
    order = json.load(f)
    print(json.dumps(order, indent=4))
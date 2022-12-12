import json
from tweet import Tweet

def load_db():
    try:
        with open('db.json', 'r') as f:
            data = json.loads(f.read())

        return data
    except:
        return {}

def create_or_update_db(request):
    db = load_db()
    for data in request:
        db[data.id] = getattr(Tweet(**data), 'get')()
    
    with open('db.json', 'w') as f:
        f.write(json.dumps(db))
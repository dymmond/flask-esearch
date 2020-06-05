from datetime import datetime

from flask import Flask, make_response
from flask_esearch import ESearch

app = Flask(__name__)

# CREATE A ESearch CLIENT
es = ESearch()
es.init_app(app)


@app.route('/')
def hello_world():
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    try:
        res = es.index(index="test-index", id=1, body=doc)
        return make_response(print(res['result']), 200)
    except Exception:
        res = es.get(index="test-index", id=1)
        return make_response(res['_source'], 200)


app.run(debug=True, port=5001)

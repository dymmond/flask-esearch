# Flask-ESearch

This is a Flask extension proving simple integration with Elasticsearch using python 3

## Requirements

 1. Flask >= 1.XXX
 2. Elasticsearch>=6.4.6, <=7.7.1
 3. Python 3.6 or later

## How to use

 1. Install the package:

    ```shell script
    pip install Flask-ESearch
    ```

 2. In your main app file:

    ```python
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
    
    ```

The above is an example of a Flask app integrating Flask-ESearch and an endpoint

 1. The instance allows to perform Elasticsearch queries. More info [here](https://elasticsearch-py.readthedocs.io/en/master/).
 2. Testing access `http://127.0.0.1:5001/`.
    1. If is the first access, will show `Created` or else the record inserted

## Custom Settings

In order to add your elasticsearch settings, the package allows to change those 2 properties and override them in your settings file.

| Name          | Type          | Default Value  |
| ------------- |:-------------:| -----:|
| ELASTICSEARCH_HOST  | string | localhost:9200 |
| ELASTICSEARCH_HTTP_AUTH  | string | None |

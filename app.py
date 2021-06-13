from flask import Flask
from redis import Redis
from rq import Queue
from counter import visit

app = Flask(__name__)
q = Queue(connection=Redis())


@app.route('/visit')
def count_visit():
    count = q.enqueue(visit)
    return "Visit has been registered"


@app.route('/')
def return_visit_count():
    count = Redis().get('count').decode('utf-8') if Redis().get('count') else '0'
    return (f'<h1> Congrats! Your are the visitor no.: {count} </h1>')

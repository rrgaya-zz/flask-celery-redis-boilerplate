import time
import redis
from flask import Flask
from celery import Celery


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
# db = redis.Redis(host='localhost', port=6379, decode_responses=True)


app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def my_background_task(arg1, arg2):
    # some long running task here
    result = "TASK IS DONE WITH CELERY"
    return result


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    # task = my_background_task.delay(10, 20)
    # task = my_background_task.apply_async(args=[10, 20])
    return 'Hello World! I have been seen {} times.\n'.format(count)
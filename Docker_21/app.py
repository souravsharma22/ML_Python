from flask import Flask
import time
import redis
import redis.exceptions

app = Flask(__name__)
cache = redis.Redis(host='redis', port= 6379)

def git_hit_count():
    retries=5
    while True:
        try:
            cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries==0:
                raise exc
            retries -=1
            time.sleep(0.5)

@app.route('/')
def hello():
    return "Hello Sourav i have seen this {} times.\n".format(git_hit_count)

if __name__ == "__main__":
    app.run(debug=True)
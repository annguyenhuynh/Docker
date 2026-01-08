import time
import redis
from flask import Flask
import redis.exceptions

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379, decode_responses=True)

def get_hit_counts():
    retries = 5
    while retries > 0:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError:
            retries -= 1
            time.sleep(0.5)
    return "Redis unavailable"

@app.route("/")
def hello():
    count = get_hit_counts()
    return f"Hello World! I have seen this page {count} times.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


from flask import Flask
from flask_mongoengine import MongoEngine
from flask_caching import Cache

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/newdb'
}
app.config["CACHE_TYPE"] = "redis"
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379/0"

db = MongoEngine()
db.init_app(app)

cache = Cache(app)

if __name__ == '__main__':
    app.run()

from flask import Flask, request, Response
from flask_caching import Cache
from database.db import initialize_db
from database.models import Advert

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/newdb'
}
app.config["CACHE_TYPE"] = "redis"
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379/0"

initialize_db(app)

cache = Cache(app)


@app.route('/')
def get_all_adverts():
    adverts = Advert.objects.to_json()
    return Response(adverts, mimetype="application/json", status=200)


@app.route('/add', methods=['POST'])
def add_advert():
    body = request.get_json()
    advert = Advert(**body).save()
    result = advert.to_json()
    return Response(result, mimetype="application/json", status=200)


@app.route('/ads/<id>', methods=['GET'])
@cache.cached()
def get_advert(id):
    if request.method == 'GET':
        result = Advert.objects.get(id=id).to_json()
        return Response(result,
                        mimetype="application/json, charset=utf-8", status=200)


if __name__ == '__main__':
    app.run()

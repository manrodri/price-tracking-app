from flask import Blueprint, request, render_template
from models.store import Store
import json

store_blueprint = Blueprint('stores', __name__)


@store_blueprint.route('/')
def index():
    stores = Store.all()
    return render_template('stores/index.html', stores=stores)


@store_blueprint.route('/new', methods=['GET', 'POST'])
def create_store():
    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        # some validation here? valid json???
        query = json.loads(request.form['query'])
        # try and catch ?? async/await ??
        Store(name, url_prefix, tag_name, query).save_to_mongo()

    return render_template('stores/new_store.html')

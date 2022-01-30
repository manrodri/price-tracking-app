from flask import Blueprint, request, render_template, redirect, url_for
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


@store_blueprint.route("/edit/<string:store_id>", methods=['GET', 'POST'])
def edit_store(store_id):
    store = Store.get_by_id(store_id)

    if request.method == 'POST':
        name = request.form['name']
        store.name = name
        url_prefix = request.form['url_prefix']
        store.url_prefix = url_prefix
        tag_name = request.form['tag_name']
        store.tag_name = tag_name
        query = request.form['query']
        store.query = query

        store.save_to_mongo()
        redirect(url_for('.index'))

    return render_template('stores/edit_store.html', store=store)


@store_blueprint.route('/delete/<string:store_id>')
def delete_store(store_id):
    store = Store.get_by_id(store_id)

    store.remove_from_mongo()
    redirect(url_for('.index'))


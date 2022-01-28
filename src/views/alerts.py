from flask import Blueprint, request, render_template
from models.alert import Alert
from models.item import Item
from models.store import Store

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    alerts = Alert.all()
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET', 'POST'])
def new_alert():
    if request.method == 'POST':
        item_url = request.form['item_url']
        print(f"item_url: {item_url}")
        prince_limit = float(request.form['price_limit'])
        print(f"limit: {prince_limit}")

        store = Store.find_by_url(item_url)
        print(f"store: {store.__repr__()}")
        print(f"store.tag_name: {store.tag_name}")
        print(f"store.query: {store.query}")
        item = Item(item_url, store.tag_name, store.query)
        item.save_to_mongo()
        item_id = item._id

        Alert(item_id, float(prince_limit)).save_to_mongo()

    return render_template('alerts/new_alert.html')

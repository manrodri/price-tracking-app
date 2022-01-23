# ebay_url = "https://www.ebay.co.uk/itm/353837129498?hash=item5262561f1a:g:UysAAOSwoxJhvllr"
#
# TAG_NAME = "span"
# QUERY = {"class": "notranslate"} # default is a class
#
# honda_civic = Item(ebay_url, TAG_NAME, QUERY)
# honda_civic.save_to_mongo()

# alert = Alert('e02255979aee4d8eb86ce4634e36a640', 5000)
# alert.save_to_mongo()

from flask import Flask
from views.items import item_blueprint
from views.alerts import alert_blueprint

app = Flask(__name__)

app.register_blueprint(item_blueprint, url_prefix='/items')
app.register_blueprint(alert_blueprint, url_prefix='/alerts')

if __name__ == '__main__':
    app.run(debug=True)

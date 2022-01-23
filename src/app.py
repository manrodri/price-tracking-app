# ebay_url = "https://www.ebay.co.uk/itm/353837129498?hash=item5262561f1a:g:UysAAOSwoxJhvllr"
#
# TAG_NAME = "span"
# QUERY = {"class": "notranslate"} # default is a class
#
# honda_civic = Item(ebay_url, TAG_NAME, QUERY)
# honda_civic.save_to_mongo()

# alert = Alert('e02255979aee4d8eb86ce4634e36a640', 5000)
# alert.save_to_mongo()

from flask import Flask, render_template, request
import json
from models.item import Item

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])
        print(f"type of query is: {type(query)}")

        Item(url, tag_name, query).save_to_mongo()

    return render_template('new_item.html')


if __name__ == '__main__':
    app.run(debug=True)

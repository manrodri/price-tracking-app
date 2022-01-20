from models.item import Item


ebay_url = "https://www.ebay.co.uk/itm/353837129498?hash=item5262561f1a:g:UysAAOSwoxJhvllr"

TAG_NAME = "span"
QUERY = {"class": "notranslate"} # default is a class

honda_civic = Item(ebay_url, TAG_NAME, QUERY)
honda_civic.save_to_mongo()

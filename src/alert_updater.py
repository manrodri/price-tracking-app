from models.alert import Alert

alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()  # there must be a relation Alert/item
    alert.notify_if_price_reached()  # think about how to send notifications and to who? (user)

if not alerts:
    print(f"No alerts have been created. Add an item and alert to begin!")


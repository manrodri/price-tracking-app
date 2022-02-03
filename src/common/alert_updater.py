from models.alert import Alert
import os


alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()  # think about how to send notifications and to who? (user)

if not alerts:
    print(f"No alerts have been created. Add an item and alert to begin!")


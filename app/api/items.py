from flask import jsonify
from ..models import Item, Store, ItemStore
from . import api

# route gets information on item and locations stocking the item given the item id
@api.route('/items/<int:id>')
def get_item(id):
    store_ids = [item.store_id for item in ItemStore.query.filter_by(item_id=id).all()]
    stores = [Store.query.get_or_404(store_id) for store_id in store_ids]
    item = Item.query.get_or_404(id)
    return jsonify({'item': item.to_json(), 'stores': [(store.to_json()) for store in stores]})
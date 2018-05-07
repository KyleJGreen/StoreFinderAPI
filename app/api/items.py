from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Item, Store, ItemStore
from . import api
from .decorators import permission_required
from .errors import forbidden


@api.route('/items/<int:id>')
def get_item(id):
    store_ids = [item.store_id for item in ItemStore.query.filter_by(item_id=id).all()]
    stores = [Store.query.get_or_404(store_id) for store_id in store_ids]
    item = Item.query.get_or_404(id)
    return jsonify({'item': item.to_json(), 'stores': [(store.to_json()) for store in stores]})
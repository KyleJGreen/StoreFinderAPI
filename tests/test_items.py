import unittest
from app import create_app, db
from app.models import Item, Store, ItemStore
from app.api.items import get_item


class ItemTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # tests whether the returned json has the expected keys
    def test_get_item(self):
        item_store = ItemStore(item_id=12, store_id=14)
        item = Item(item_id=12, item_name='hat', item_description='goes on head',
                 category='clothing', artisan_id=14)
        store = Store(store_id=12, store_name='Local Space', address_line_one='3452 W Adams St',
                  address_line_two='Suite #7', city='Chicago', state='IL', zip='60603')
        db.session.add(item_store)
        db.session.add(item)
        db.session.add(store)
        db.session.commit()

        expected_keys = ['item', 'stores']
        self.assertEqual(sorted(get_item(item.item_id).keys()), sorted(expected_keys))
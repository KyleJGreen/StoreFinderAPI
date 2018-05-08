import unittest
from app import create_app, db
from app.models import ItemStore


class ItemModelTestCase(unittest.TestCase):
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
    def test_to_json(self):
        i = ItemStore(item_id=12, store_id=14)
        db.session.add(i)
        db.session.commit()
        with self.app.test_request_context('/'):
            json_user = i.to_json()
        expected_keys = ['url', 'item_id', 'store_id']
        self.assertEqual(sorted(json_user.keys()), sorted(expected_keys))
        self.assertEqual('/api/v1/users/' + str(i.id), json_user['url'])

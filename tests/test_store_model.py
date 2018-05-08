import unittest
from app import create_app, db
from app.models import Store

class StoreModelTestCase(unittest.TestCase):
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
        s = Store(store_id=12, store_name='Local Space', address_line_one='3452 W Adams St',
                  address_line_two='Suite #7', city='Chicago', state='IL', zip='60603')
        db.session.add(s)
        db.session.commit()
        with self.app.test_request_context('/'):
            json_user = s.to_json()
        expected_keys = ['url', 'store_id', 'store_name', 'address_line_one',
                         'address_line_two', 'city', 'state', 'zip']
        self.assertEqual(sorted(json_user.keys()), sorted(expected_keys))
        self.assertEqual('/api/v1/users/' + str(s.store_id), json_user['url'])
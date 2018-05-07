from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin
from app.exceptions import ValidationError
from . import db, login_manager


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class Artisan(db.Model):
    __tablename__ = 'artisans'
    artisan_id = db.Column(db.Integer, primary_key=True)
    artisan_name = db.Column(db.Text)
    email = db.Column(db.Text)
    website = db.Column(db.Text)
    phone_number = db.Column(db.Text)

class Store(db.Model):
    __tablename__ = 'store'
    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.Text)
    address_line_one = db.Column(db.Text)
    address_line_two = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip = db.Column(db.Integer)

    def to_json(self):
        json_store = {
            'url': url_for('api.get_item', id=self.store_id),
            'store_id': self.store_id,
            'store_name': self.store_name,
            'address_line_one': self.address_line_one,
            'address_line_two': self.address_line_two,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
        }
        return json_store

class Item(db.Model):
    __tablename__ = 'item'
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    item_description = db.Column(db.Text)
    category = db.Column(db.Text, nullable=False)
    artisan_id = db.Column(db.Integer, db.ForeignKey('artisans.artisan_id'))

    def to_json(self):
        json_item = {
            'url': url_for('api.get_item', id=self.item_id),
            'item_id': self.item_id,
            'item_name': self.item_name,
            'item_description': self.item_description,
            'category': self.category,
            'artisan_id': self.artisan_id
        }
        return json_item

    # @staticmethod
    # def from_json(store):
    #     body = store.get('body')
    #     if body is None or body == '':
    #         raise ValidationError('comment does not have a body')
    #     return Store(body=body)

class ItemStore(db.Model):
    __tablename__ = 'item_store'
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'), primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'), primary_key=True)

    def to_json(self):
        json_item_store = {
            'url': url_for('api.get_item', id=self.item_id),
            'item_id': self.item_id,
            'store_id': self.store_id
        }
        return json_item_store
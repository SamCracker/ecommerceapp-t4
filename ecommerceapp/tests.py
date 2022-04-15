import pytest
from ecommerceapp.models import app, db
from flask import Flask, session
from .models import *
from difflib import SequenceMatcher
import string
import base64, json
import random
from flask import Flask, request, jsonify, make_response, session, app, Response, url_for
from ecommerceapp import app, db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate, MigrateCommand

from datetime import datetime, timedelta
import os
from sqlalchemy.orm import sessionmaker

import json
import jwt
from functools import wraps
from .models import *

class Test_API:
    client = app.test_client()

    @pytest.fixture(autouse=True, scope='session')
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

    # Product table
    def test_product_table(self):
        all_prods = Product.query.all()
        num=0
        for prod in all_prods:
            num+=1
        assert num==2
    
    # User
    def test_user_table(self):
        all_users = User.query.all()
        num=0
        for useri in all_users:
            num+=1
        assert num==4
    
    # Category
    def test_category_table(self):
        all_cats = Category.query.all()
        num=0
        for cat in all_cats:
            num+=1
        assert num==5
    
    # Category
    def test_category_table(self):
        all_cats = Category.query.all()
        num=0
        for cat in all_cats:
            num+=1
        assert num==5
    
    # CartProduct
    def test_cartproduct_table(self):
        all_cats = CartProduct.query.all()
        num=0
        for cats in all_cats:
            num += 1
        assert num==1

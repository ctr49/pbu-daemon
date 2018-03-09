# encoding: utf-8

"""
Copyright (c) 2012 - 2016, Ernesto Ruge
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from werkzeug.security import check_password_hash
from passlib.hash import bcrypt
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from hashlib import sha256
from flask_login import login_user
from ..extensions import mail
from flask import current_app, render_template
from mongoengine import Document, BooleanField, ReferenceField, DateTimeField, StringField, ListField, \
    DecimalField, EmailField, IntField, GeoJsonBaseField


class User(Document):
    created = DateTimeField(default=datetime.utcnow())
    modified = DateTimeField(default=datetime.utcnow())
    last_login = DateTimeField()

    email = StringField()
    password = StringField()
    active = BooleanField()
    type = StringField()

    subscription_frequency = StringField(default='week') #day, week
    html_emails = BooleanField(default=True)


    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<User %r>' % self.email

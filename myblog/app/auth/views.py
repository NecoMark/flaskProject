#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author:ljyang
"""
from flask import Blueprint
from forms import LoginForm
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

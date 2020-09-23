#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    return app

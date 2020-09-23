#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
from flask import Flask
# from instance.config import app_config



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    return app

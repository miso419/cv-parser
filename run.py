#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import request
from app import create_app
from app.common.response_helper import response
from app.managers.parser import parse

app = create_app()


@app.route('/')
def index():
    return 'TEST'


@app.route('/', methods=['POST'])
def parse_cv():
    return response(parse, request.get_json())


if __name__ == '__main__':
    # host must be 0.0.0.0 for Docker to access
    app.run(port=4005, host='0.0.0.0', threaded=True)

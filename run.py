#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import create_app


app = create_app()


@app.route('/')
def index():
    return 'TEST'


if __name__ == '__main__':
    # host must be 0.0.0.0 for Docker to access
    app.run(port=4005, host='0.0.0.0', threaded=True)

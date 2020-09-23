#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import create_app


config_name = 'development'
app = create_app(config_name)


@app.route('/')
def index():
    return 'AI SERVICE - {0}'.format(config_name)


if __name__ == '__main__':
    # host must be 0.0.0.0 for Docker to access
    app.run(port=4005, host='0.0.0.0', threaded=True)

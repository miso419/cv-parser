#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import jsonify


def response(execute_func, *args, **kwargs):
    result = execute_func(*args, **kwargs)
    return jsonify(result), 200

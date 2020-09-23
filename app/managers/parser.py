#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.managers.nlp_common import get_doc, get_nlp_doc_json
from app.managers.personal_details import get_name


def parse(data):
    doc = get_doc(data['decomposedText'])
    # result = get_nlp_doc_json(doc) -- debug

    name = get_name(doc)
    result = {'name': name}
    return result

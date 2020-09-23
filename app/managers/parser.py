#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.managers.nlp_common import get_doc, get_nlp_doc_json
from app.managers.personal_details import get_name, get_email


def parse(data):
    source_text = data['decomposedText']
    doc = get_doc(source_text)
    # result = get_nlp_doc_json(doc) -- debug

    name = get_name(doc)
    email = get_email(source_text)
    result = {'name': name, 'email': email}
    return result

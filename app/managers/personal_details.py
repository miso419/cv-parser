#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.managers.nlp_common import extract_named_entities


def get_name(nlp_doc):
    names = extract_named_entities(nlp_doc, 'PERSON')
    return names[0] if len(names) > 0 else None

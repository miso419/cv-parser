#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from app.managers.nlp_common import extract_named_entities, extract_matched_spans


def get_name(nlp_doc):
    names = extract_named_entities(nlp_doc, 'PERSON')
    return names[0] if len(names) > 0 else None


def get_email(source_text):
    EMAIL_REGEX = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    pattern = re.compile(EMAIL_REGEX, re.IGNORECASE)
    emails = re.findall(pattern, source_text)
    return emails[0] if len(emails) > 0 else None


def get_phone(source_text):
    EN_PHONE_REGEX = r"((?:(?:\+?61 ?)?(?:(?:\(?0?[2|3|7|8]\)?) ?[0-9]{3,4} ?[0-9]{3,4}|0?4 ?[0-9]{2} ?[0-9]{3} ?[0-9]{3})|1(?:3|8)00 ?[0-9]{3} ?[0-9]{3}|133 ?[0-9]{3}))"
    pattern = re.compile(EN_PHONE_REGEX, re.IGNORECASE)
    phones = re.findall(pattern, source_text)
    return phones[0] if len(phones) > 0 else None

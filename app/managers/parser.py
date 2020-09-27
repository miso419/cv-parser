#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.managers.nlp_common import get_doc, get_matches, get_nlp_doc_json
from app.managers.personal_details import get_name, get_email, get_phone
from app.managers.educations import get_educations
from app.managers.experiences import get_experiences
from app.managers.skills import get_skills


def get_spacy_json(data):
    doc = get_doc(data['decomposedText'])
    return get_nlp_doc_json(doc)


def parse(data):
    source_text = data['decomposedText']
    doc = get_doc(source_text)
    matches = get_matches(doc)

    name = get_name(doc)
    email = get_email(source_text)
    phone = get_phone(source_text)
    education = get_educations(doc, matches)
    experiences = get_experiences(doc, matches)
    skills = get_skills(doc)
    result = {'name': name, 'email': email,
              'phone': phone, 'education': education, 'experiences': experiences, 'skills': skills}
    return result

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

nlp = spacy.load('en_core_web_lg')
matcher = Matcher(nlp.vocab)

# Customer matchers
phone_pattern = [
    {"ORTH": "(", "OP": "?"},
    {"IS_DIGIT": True, "OP": "?"},
    {"ORTH": ")", "OP": "?"},
    {"IS_DIGIT": True},
    {"ORTH": "-", "OP": "?"},
    {"IS_DIGIT": True},
    {"ORTH": "-", "OP": "?"},
    {"IS_DIGIT": True, "OP": "?"}
]
matcher.add('PhoneNumber', None, phone_pattern)


def get_doc(source_text):
    return nlp(source_text)


def get_matches(doc):
    return matcher(doc)


def extract_named_entities(doc, entity_type=None):
    raw_list = [entity.text.strip()
                for entity in doc.ents if entity_type is None or entity.label_ == entity_type]
    return list(set(raw_list))  # Get unique names


def extract_matched_spans(doc, matches, match_key):
    raw_list = [re.sub(r'\s+', ' ', doc[start:end].text.strip())
                for match_id, start, end in matches if nlp.vocab.strings[match_id] == match_key]
    return list(set(raw_list))  # Get unique names


def get_nlp_doc_json(doc):
    tokens = [{"text": w.text, "lemma": w.lemma_, "pos": w.pos_, "dep": w.dep_,
               "shape": w.shape_, "alpha": w.is_alpha, "stop": w.is_stop} for w in doc]
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"tokens": tokens, "entities": entities}

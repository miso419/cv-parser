#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import spacy

nlp = spacy.load('en_core_web_lg')


def get_doc(source_text):
    return nlp(source_text)


def extract_named_entities(doc, entity_type=None):
    raw_list = [re.sub(r'\s+', ' ', entity.text.strip())
                for entity in doc.ents if entity_type is None or entity.label_ == entity_type]
    return list(set(raw_list))  # Get unique names


def get_nlp_doc_json(doc):
    tokens = [{"text": w.text, "lemma": w.lemma_, "pos": w.pos_, "dep": w.dep_,
               "shape": w.shape_, "alpha": w.is_alpha, "stop": w.is_stop} for w in doc]
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"tokens": tokens, "entities": entities}

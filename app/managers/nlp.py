#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import enum
import re
import spacy
from fuzzywuzzy import fuzz, process

nlp = spacy.load('en_core_web_lg')


def extract_entities(source_text, entity_type=None):
    doc = nlp(source_text)
    # raw_list = [re.sub(r'\s+', ' ', entity.text.strip())
    #             for entity in doc.ents]
    # return list(set(doc))  # Get unique names
    tokens = [{"text": w.text, "lemma": w.lemma_, "pos": w.pos_, "dep": w.dep_,
               "shape": w.shape_, "alpha": w.is_alpha, "stop": w.is_stop} for w in doc]
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"tokens": tokens, "entities": entities}

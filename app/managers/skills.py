#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from spacy.tokens import Span
from spaczz.matcher import FuzzyMatcher

nlp = spacy.blank("en")
doc = nlp("")
matcher = FuzzyMatcher(nlp.vocab)

def add_entry(
  matcher, doc, i, matches
):
  _match_id, start, end, ratio = matches[i]
  entity = Span(doc, start, end, label="id")
  if ratio > 95
    doc.ents += (entity,) 

with open ('skills.json') as json_file:
  data = json.load(json_file)
    for skill in data
      matcher.add(skill['id'], [nlp(skill['name'])], on_match=add_entry) # non-custom additions are possible

def get_skill_matches(nlp_doc):
    for token in nlp_doc.ents
      matcher(token)
    
    return doc.ents

from app.managers.nlp import extract_entities


def parse(data):
    result = extract_entities(data['decomposedText'])
    return result

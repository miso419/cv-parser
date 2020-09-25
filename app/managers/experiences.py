from app.managers.nlp_common import extract_named_entities, extract_matched


def is_institution(value):
    ins_types = ['univ', 'college', 'institut']
    for ins_type in ins_types:
        if ins_type in value.lower():
            return True

    return False


def get_companies(nlp_doc):
    all_orgs = extract_named_entities(nlp_doc, 'ORG')
    return [org for org in all_orgs if is_institution(org)]


def get_experiences(nlp_doc, matches):
    matched = extract_matched(matches, 'Experience1')
    print('get_experiences: ', matched)
    mat = matched[0] if len(matched) > 0 else None

    if mat is None:
        return None

    startIndex = mat['end']
    line = ''
    exp_list = []

    for w in nlp_doc[startIndex:]:
        print(w)

    return []

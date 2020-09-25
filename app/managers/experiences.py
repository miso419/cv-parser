from app.managers.nlp_common import extract_named_entities, extract_matched


def get_companies(nlp_doc):
    all_orgs = extract_named_entities(nlp_doc, 'ORG')
    new_orgs = []
    for org in all_orgs:
        splits = org.split('\n\n\n\n')
        new_org = org[1] if len(splits) > 0 else org[0]
        new_orgs.append(new_org)

    return new_orgs


def extract_company(orgs, line):
    matched_org = [org for org in orgs if org in line]
    institution = matched_org[0] if len(matched_org) > 0 else None
    return {'institution': institution} if institution else None


def get_experiences(nlp_doc, matches):
    matched = extract_matched(matches, 'Experience1')
    print('get_experiences: ', matched)
    mat = matched[0] if len(matched) > 0 else None

    if mat is None:
        return None

    all_orgs = get_companies(nlp_doc)

    startIndex = mat['end']
    line = ''
    exp_list = []

    for w in nlp_doc[startIndex:]:
        # Section
        if w.shape_ == "\n\n\n\n":
            nwe_com = extract_company(all_orgs, line)
            if nwe_com:
                exp_list.append(nwe_com)
            line = ''
            continue

        line = line + ' ' + w.text

    return []

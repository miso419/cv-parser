from app.managers.nlp_common import extract_named_entities, extract_matched


def extract_edu(orgs, line):
    matched_org = [org for org in orgs if org in line]
    institution = matched_org[0] if len(matched_org) > 0 else None
    return {'institution': institution} if institution else None


def is_institution(value):
    ins_types = ['univ', 'college', 'institut']
    for ins_type in ins_types:
        if ins_type in value.lower():
            return True

    return False


def get_institutions(nlp_doc):
    all_orgs = extract_named_entities(nlp_doc, 'ORG')
    return [org for org in all_orgs if is_institution(org)]


def get_educations(nlp_doc, matches):
    matched = extract_matched(matches, 'Education1')
    mat = matched[0] if len(matched) > 0 else None

    if mat is None:
        return None

    all_institutes = get_institutions(nlp_doc)

    startIndex = mat['end']
    line = ''
    edu_list = []

    for w in nlp_doc[startIndex:]:
        # Section
        if w.shape_ == "\n\n\n\n":
            break

        # Line break
        if w.shape_ == "\n\n":
            new_edu = extract_edu(all_institutes, line)
            if new_edu:
                edu_list.append(new_edu)
            line = ''
            continue

        line = line + ' ' + w.text

    return edu_list

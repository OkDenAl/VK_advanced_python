import json


class RequiredFieldsIsNoneError(Exception):
    pass


class KeywordsIsNoneError(Exception):
    pass


class KeywordCallbackIsNoneError(Exception):
    pass


def parse_json(json_str, keyword_callback, required_fields=None,
               keywords=None):
    json_decode = json.loads(json_str)

    if required_fields is None:
        raise RequiredFieldsIsNoneError("required_fields is none")
    if keywords is None:
        raise KeywordsIsNoneError("keywords is none")
    if keyword_callback is None:
        raise KeywordCallbackIsNoneError("keyword callback is none")

    for required_field in required_fields:
        for json_key in json_decode:
            if json_key.lower() == required_field.lower():
                for keyword in keywords:
                    for word in json_decode[json_key].split():
                        if keyword.lower() == word.lower():
                            keyword_callback(required_field, keyword)

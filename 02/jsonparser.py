import json


class InvalidRequiredFieldError(Exception):
    pass


def parse_json(json_str, keyword_callback, required_fields=None,
               keywords=None):
    json_decode = json.loads(json_str)
    if required_fields is None:
        required_fields = list(json_decode.keys())
    if keywords is None:
        keywords = []
        for val in json_decode.values():
            keywords += (val.split())
        keywords = list(set(keywords))
    for required_field in required_fields:
        if required_field in json_decode:
            for keyword in keywords:
                if keyword in json_decode[required_field]:
                    keyword_callback(keyword)
        else:
            raise InvalidRequiredFieldError("invalid required field")

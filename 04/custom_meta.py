class CustomMeta(type):
    def create_custom_setattr(cls, key, value):
        if key[:7] != "custom_" and not (key.endswith('__')
                                         and key.startswith('__')):
            key = f'custom_{key}'
        object.__setattr__(cls, key, value)

    def __new__(cls, name, bases, classdict, **kwargs):
        new_keys = []
        for key in classdict:
            if not (key.endswith('__') and key.startswith('__')):
                new_key = "custom_" + key
                new_keys.append((new_key, classdict[key], key))
        classdict["__setattr__"] = cls.create_custom_setattr
        for k in new_keys:
            classdict[k[0]] = k[1]
            del classdict[k[2]]
        return super().__new__(cls, name, bases, classdict, **kwargs)

    def __setattr__(cls, key, value):
        if key[:7] != "custom_" and not (key.endswith('__')
                                         and key.startswith('__')):
            key = f'custom_{key}'
        super().__setattr__(key, value)

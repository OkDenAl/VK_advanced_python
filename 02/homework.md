# Домашнее задание #02

### Написать функцию, которая в качестве аргументов принимает строку json, список полей, которые необходимо обработать, список имён, которые нужно найти и функцию-обработчика имени, который срабатывает, когда в каком-либо поле было найдено ключевое имя.

Функция, должна принимать строку, в которой содержится json, и произвести парсинг этого json.
Упростим немного и представим, что json представляет из себя только коллекцию ключей-значений.
Причём ключами и значениями являются только строки.

```py
def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback)
```

Например, представим, что json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}', а required_fields = ["key1"], keywords = ["word2"]. Тогда keyword_callback будет вызвана только для слова 'word2' для ключа 'key1'.

Распарсить json можно так:
```py
import json

...
json_doc = json.loads(json_str)

```

Можно использовать ещё ujson, но его предварительно нужно установить с помощью pip.

### Написать декоратор, который считает среднее время выполнения последних k вызовов.

```py
@mean(10)
def foo(arg1):
    pass

@mean(2)
def boo(arg1):
    pass

for _ in range(100):
    foo("Walter")
```

### Использовать mock-объект при тестировании
Использовать mock-объект, например, keyword_callback и проверить, что заглушка вызывалась n число раз.

### Узнать степень покрытия тестами с помощью библиотеки coverage

### Использовать flake8 и pylint для проверки кода

### Использовать factory boy (опционально!!!)
Для генерации данных и ключевых слов, можно использовать factory boy (см. файл factory_boy_example.py).


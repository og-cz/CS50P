import re

def test(word):
    find = re.findall(r'\bum\b', word, re.IGNORECASE)
    return len(find)


test('um idk um')
test('yum um ummy')
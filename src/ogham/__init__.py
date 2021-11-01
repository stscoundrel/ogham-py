from .mappings import get_ogham_mapping


def transform(content: str, mapping: 'dict[str, str]') -> str:
    result = ''

    for letter in content:
        result += mapping.get(letter.lower(), letter)

    return result


def ogham_to_letters(content: str) -> str:
    mapping = get_ogham_mapping()
    result = transform(content, mapping)

    return result

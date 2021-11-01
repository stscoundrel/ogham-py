from .mappings import get_ogham_mapping


def transform(content: str, mapping: 'dict[str, str]') -> str:
    result = ''

    for part in content:
        letter = part.lower()

        if letter in mapping:
            result += mapping.get(letter)
        else:
            result += part

    return result


def ogham_to_letters(content: str) -> str:
    mapping = get_ogham_mapping()
    result = transform(content, mapping)

    return result

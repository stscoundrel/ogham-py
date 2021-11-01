from . import mappings


def transform(content: str, mapping: 'dict[str, str]') -> str:
    result = ''

    for letter in content:
        result += mapping.get(letter.lower(), letter)

    return result

def replace(content: str, mapping: 'dict[str, str]') -> str:
    result = content

    for dual_letter, ogham in mapping.items():
        result = result.replace(dual_letter, ogham)

    return result

def ogham_to_letters(content: str) -> str:
    mapping = mappings.get_ogham_mapping()
    result = transform(content, mapping)

    return result

def letters_to_ogham(content: str) -> str:
    letter_mapping = mappings.get_letter_mapping()
    dual_mapping = mappings.get_dual_letter_mapping()

    dual_letter_result = replace(content, dual_mapping)
    result = transform(dual_letter_result, letter_mapping)

    # Append expected start/end characters.
    return "᚛" + result + "᚜"
from src.ogham import ogham_to_letters


def test_transforms_ballaqueeney_ogham_stone():
    ogham = '᚛ᚁᚔᚃᚐᚔᚇᚑᚅᚐᚄᚋᚐᚊᚔᚋᚒᚉᚑᚔ᚜ ᚛ᚉᚒᚅᚐᚃᚐ[ᚂᚔ]᚜'
    expected = 'bivaidonasmaqimucoi cunava[li]'

    result = ogham_to_letters(ogham)

    assert result == expected


def test_transforms_breastagh_ogham_stone():
    ogham = '᚛ᚂᚓᚌᚌ[--]ᚄᚇ[--]ᚂᚓᚌᚓᚄᚉᚐᚇ᚜ ᚛ᚋᚐᚊ ᚉᚑᚏᚏᚁᚏᚔ ᚋᚐᚊ ᚐᚋᚋᚂᚂᚑᚌᚔᚈᚈ᚜'
    expected = 'legg[--]sd[--]legescad maq corrbri maq ammllogitt'

    result = ogham_to_letters(ogham)

    assert result == expected


def test_transforms_text_cunalegi_descendant_of_qunacanos():
    ogham = '᚛ᚉᚒᚅᚐᚂᚓᚌᚔ ᚐᚃᚔ ᚊᚒᚅᚐᚉᚐᚅᚑᚄ᚜'
    expected = 'cunalegi avi qunacanos'

    result = ogham_to_letters(ogham)

    assert result == expected


def test_transforms_text_netacari_nephew_of_cagi():
    ogham = '᚛ᚅᚓᚈᚐᚉᚐᚏᚔᚅᚓᚈᚐᚉᚉᚐᚌᚔ᚜'
    expected = 'netacarinetaccagi'

    result = ogham_to_letters(ogham)

    assert result == expected


def test_transforms_nettasagri_briaci():
    ogham = '᚛ᚅᚓᚈᚈᚐᚄᚐᚌᚏᚔ ᚋᚐᚊᚔ ᚋᚒᚉᚑᚓ ᚁᚏᚔᚐᚉᚔ᚜'
    expected = 'nettasagri maqi mucoe briaci'

    result = ogham_to_letters(ogham)

    assert result == expected


def test_transforms_latin_text_written_in_ogham():
    ogham = '᚛ᚅᚒᚋᚒᚄ ᚆᚑᚅᚑᚏᚐᚈᚒᚏ ᚄᚔᚅᚓ᚜ ᚛ᚅᚒᚋᚑ ᚅᚒᚂᚂᚒᚄ ᚐᚋᚐᚈᚒᚏ᚜'
    expected = 'numus honoratur sine numo nullus amatur'

    result = ogham_to_letters(ogham)

    assert result == expected


def test_transforms_forfeda_characters():
    ogham = '᚛ᚕᚖᚗᚘᚚᚙ᚜'
    expected = 'koiuiiopai'

    result = ogham_to_letters(ogham)

    assert result == expected

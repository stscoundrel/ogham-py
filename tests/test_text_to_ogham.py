from src.ogham import letters_to_ogham


def test_appends_start_and_prepends_end_characters():
    expected = '᚛᚜'
    text = ''

    result = letters_to_ogham(text)

    assert result == expected


def test_transforms_text_netacari_nephew_of_cagi():
    expected = '᚛ᚅᚓᚈᚐᚉᚐᚏᚔᚅᚓᚈᚐᚉᚉᚐᚌᚔ᚜'
    text = 'netacarinetaccagi'

    result = letters_to_ogham(text)

    assert result == expected


def test_transforms_text_cunalegi_descendant_of_qunacanos():
    expected = '᚛ᚉᚒᚅᚐᚂᚓᚌᚔ ᚐᚃᚔ ᚊᚒᚅᚐᚉᚐᚅᚑᚄ᚜'
    text = 'CUNALEGI AVI QUNACANOS'

    result = letters_to_ogham(text)

    assert result == expected


def test_transforms_text_son_of_the_tribe_corbagnus_glasiconas():
    expected = '᚛ᚋᚐᚊᚔ ᚋᚒᚉᚑᚔ ᚉᚑᚏᚁᚐᚌᚅᚔ ᚌᚂᚐᚄᚔᚉᚑᚅᚐᚄ᚜'
    text = 'MAQI MUCOI CORBAGNI GLASICONAS'

    result = letters_to_ogham(text)

    assert result == expected


def test_transforms_text_here_is_corb_son_of_labraid():
    expected = '᚛ᚉᚑᚏᚁᚔᚕᚑᚔᚋᚐᚊᚔᚂᚐᚏᚔᚇ᚜'
    text = 'CORBIKOIMAQILARID'

    result = letters_to_ogham(text)

    assert result == expected


def test_transforms_text_cunnetas_neta_segamonas():
    expected = '᚛ᚉᚒᚅᚅᚓᚈᚐᚄ ᚋᚐᚊᚔ ᚌᚒᚉᚑᚔ ᚅᚓᚈᚐ ᚄᚓᚌᚐᚋᚑᚅᚐᚄ᚜'
    text = 'CUNNETAS MAQI GUCOI NETA SEGAMONAS'

    result = letters_to_ogham(text)

    assert result == expected


def test_transforms_two_letter_parts():
    expected = '᚛ᚖ ᚗ ᚘ ᚙ᚜'
    text = 'oi ui io ai'

    result = letters_to_ogham(text)

    assert result == expected



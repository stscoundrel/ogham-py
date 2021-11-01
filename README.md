# Ogham

Convert Ogham inscriptions to latin text & vice versa.

Python port of the original [Node.js library](https://github.com/stscoundrel/ogham).

### Install

`pip install ogham`

#### Usage

You can either transform ogham to text, or text to ogham.

Latin text to ogham:

```python
from ogham import letters_to_ogham

# "Netacari, nephew of Cagi", from Castletimon, Brittas Bay, Co Wicklow 
result = letters_to_ogham('netacarinetaccagi')

print(result) # ᚛ᚅᚓᚈᚐᚉᚐᚏᚔᚅᚓᚈᚐᚉᚉᚐᚌᚔ᚜
```

Ogham to latin text:

```python
from ogham import ogham_to_letters

# "Nettasagri, Briaci", from Bridell, Pembrokeshire
result = ogham_to_letters('᚛ᚅᚓᚈᚈᚐᚄᚐᚌᚏᚔ ᚋᚐᚊᚔ ᚋᚒᚉᚑᚓ ᚁᚏᚔᚐᚉᚔ᚜')

print(result) # nettasagri maqi mucoe briaci
```

### About Ogham

Ogham (or ogam) is an Early Medieval alphabet used primarily to write the early Irish language, and later the Old Irish language. Used roughly from 4th to 10th centuries AD.

import re
import os
from pathlib import Path


CYRILLIC_SYMBOLS = [*"абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"]
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()



def normalize_file(file: Path)-> str: 
    translate_name = re.sub('\W', '_', file.name.translate(TRANS))[:-len(file.suffix)] + file.suffix
    return translate_name

def normalize_archiv(name: str)-> str: 
    translate_name = re.sub('\W', '_', name.translate(TRANS))
    return translate_name

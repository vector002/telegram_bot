# tarjimon.py

def lotin_to_kirill(text):
    text = text.lower()
    sozlash = {
        'yo': 'ё', 'ya': 'я', 'yu': 'ю', 'sh': 'ш', 'ch': 'ч', 'o‘': 'ў', 'g‘': 'ғ',
        'a': 'а', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'ҳ', 'i': 'и',
        'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'q': 'қ',
        'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'в', 'x': 'х', 'y': 'й', 'z': 'з',
        "'": 'ъ'
    }
    for lot, kir in sorted(sozlash.items(), key=lambda x: -len(x[0])):
        text = text.replace(lot, kir)
    return text

def kirill_to_lotin(text):
    text = text.lower()
    sozlash = {
        'ё': 'yo', 'я': 'ya', 'ю': 'yu', 'ш': 'sh', 'ч': 'ch', 'ў': "o‘", 'ғ': "g‘",
        'а': 'a', 'б': 'b', 'д': 'd', 'е': 'e', 'ф': 'f', 'г': 'g', 'ҳ': 'h', 'и': 'i',
        'ж': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'қ': 'q',
        'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'в': 'v', 'х': 'x', 'й': 'y', 'з': 'z',
        'ъ': "'"
    }
    for kir, lot in sorted(sozlash.items(), key=lambda x: -len(x[0])):
        text = text.replace(kir, lot)
    return text

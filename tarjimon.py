# translit.py

def lotin_to_kirill(text):
    import re
    from transliterate import to_cyrillic
    return to_cyrillic(text)

def kirill_to_lotin(text):
    import re
    from transliterate import to_latin
    return to_latin(text)

# tarjimon.py

# Lotin yozuvini Kirilga o'zgartirish
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

# Kiril yozuvini Lotinga o'zgartirish
def kirill_to_lotin(text):
    text = text.lower()
    sozlash = {
        'ё': 'yo', 'я': 'ya', 'ю': 'yu', 'ш': 'sh', 'ч': 'ch', 'ў': "o‘", 'ғ': "g‘",
        'а': 'a', 'б': 'b', 'д': 'd', 'е': 'e', 'ф': 'f', 'г': 'g', 'ҳ': 'h', 'и': 'i',
        'ж': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'қ': 'q',
        'р': 'r', 'с': 's', 'т': 'т', 'у': 'u', 'в': 'v', 'х': 'x', 'й': 'y', 'з': 'z',
        'ъ': "'"
    }
    for kir, lot in sorted(sozlash.items(), key=lambda x: -len(x[0])):
        text = text.replace(kir, lot)
    return text

# Katta matnni bo'lib tarjima qilish
def process_large_text(text, chunk_size=1000):
    # Matnni kichik qismlarga bo'lib chiqamiz
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    # Har bir bo'limni tarjima qilish
    translated_text = ''
    for chunk in chunks:
        translated_text += lotin_to_kirill(chunk)  # yoki kirill_to_lotin, agar kerak bo'lsa
    
    return translated_text

# Faylni o'qish va tarjima qilib, yangi faylga yozish
def process_and_save_large_text(input_file, output_file, chunk_size=1000):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Matnni bo'lib, tarjima qilish
    translated_text = process_large_text(text, chunk_size)
    
    # Natijani faylga yozish
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

# Terminaldan matnni qabul qilib, tarjima qilish
def translate_from_input():
    input_text = input("Matnni kiriting: ")
    translated_text = process_large_text(input_text)
    print("Tarjima qilingan matn: ")
    print(translated_text)

# Asosiy kod - Fayldan o'qish va natijani faylga yozish
if __name__ == "__main__":
    # Faylni tarjima qilib, yangi faylga saqlash
    input_file = 'input_text.txt'  # O'qish uchun fayl nomi
    output_file = 'translated_text.txt'  # Natijani saqlash uchun fayl nomi
    process_and_save_large_text(input_file, output_file)

    # Yoki terminaldan matn kiritish va tarjima qilish
    # translate_from_input()

from deep_translator import GoogleTranslator

def translate_text(text, lang):
    translated = GoogleTranslator(source='auto', target=lang).translate(text)
    return translated
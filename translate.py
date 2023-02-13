from googletrans import Translator, LANGUAGES

def translate_text_to_english(text):
    try:
        translator = Translator(service_urls=['translate.google.com'])
        result = translator.translate(text, dest='en').text
    except Exception as e:
        result = "Error: " + str(e)
    return result

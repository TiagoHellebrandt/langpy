# Gerencia idiomas em uma aplicação Python.
try:
    import json
    import locale
except ImportError as err:
    print(err)

PATH = "langpy.json" # Caminho do dicionário.

langs = [
    ("Afrikaans", "af"),
    ("Bahasa Melayu", "ms"),
    ("Dansk", "da"),
    ("Deutsch", "de"),
    ("Eesti", "et"),
    ("English", "en"),
    ("Español", "es"),
    ("Esperanto", "eo"),
    ("Euskara", "eu"),
    ("Français", "fr"),
    ("Galego", "gl"),
    ("Hrvatski", "hr"),
    ("Interlingua", "ia"),
    ("Italiano", "it"),
    ("Lenga d'òc", "oc"),
    ("Magyar", "hu"),
    ("Nederlands","nl"),
    ("Norsk","nb"),
    ("Occitan","oc"),
    ("Plattdüütsch", "nds"),
    ("Polski", "pl"),
    ("Português Brasileiro", "pt_BR"),
    ("Português", "pt"),
    ("Româneşte", "ro"),
    ("Slovenčina", "sk"),
    ("Slovenščina", "sl"),
    ("Suomi", "fi"),
    ("Svenska", "sv"),
    ("Tiếng Việt", "vi"),
    ("Türkçe", "tr"),
    ("Čeština", "cs"),
    ("Ελληνικά", "el"),
    ("Ελληνικά", "el"),
    ("босански", "bs"),
    ("Български", "bg"),
    ("Монгол хэл","mn"),
    ("русский язык", "ru"),
    ("Српски", "sr"),
    ("українська мова", "uk"),
    ("עִבְרִית", "he"),
    ("العربية", "ar"),
    ("فارسی", "fa"),
    ("ภาษาไทย", "th"),
    ("日本語", "ja"),
    ("简体中文", "zh_CN"),
    ("繁體中文", "zh_TW"),
    ("한국어", "ko"),
]

def getLang(): # Idioma padrão
    return locale.getdefaultlocale()[0]

def getCharset(): # Codificação padrão
    return locale.getdefaultlocale()[1]

def getMessages(): # Mensagens do dicionário
    messages = False
    try:
        dict = open(PATH, "r")
        messages = json.loads(dict.read())
        dict.close()
    except Exception as err:
        print(err)
    return messages

class msg:

    def __init__(self,key,lang=getLang(),args=None):
        self.key = key
        self.lang = lang
        self.args = args

    def getMessage(self): # Mensagem no idioma definido (self.lang)
        if getMessages()
        return getMessages()[self.key][self.lang]

    def __str__(self):
        return self.getMessage()

    def getLangs(self):
        return list(getMessages()[self.key])

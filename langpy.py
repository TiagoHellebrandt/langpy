# Gerencia idiomas em uma aplicação Python.
try:
    import json
    import locale
except ImportError as err:
    print(err)
class langpy:

    def __init__(self):
        self.path = "langpy.txt" # Caminho do dicionário.
        self.lang = locale.getdefaultlocale()[0]
        self.charset = locale.getdefaultlocale()[1]
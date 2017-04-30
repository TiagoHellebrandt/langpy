# Gerencia idiomas em uma aplicação Python.
try:
    import json
except ImportError as err:
    print(err)
class langpy:

    def __init__(self):
        self.path = "langpy.txt" # Caminho do dicionário.

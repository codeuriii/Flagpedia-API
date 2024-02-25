import requests
import pycountry

class FlagpediaAPI:

    def __init__(self) -> None:
        self.default_url = "https://flagcdn.com/"
        self.name_to_iso = 0
        self.iso_to_name = 1

    def convert(self, code, how):
        if how == self.iso_to_name:
            try:
                language = pycountry.languages.get(alpha_2=code)
                return language.name
            except AttributeError:
                return None
        
        if how == self.name_to_iso:
            try:
                language = pycountry.languages.lookup(code)
                return language.alpha_2
            except LookupError:
                return None

    
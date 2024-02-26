
from bs4 import BeautifulSoup
import requests
import pycountry

class FlagpediaAPI:

    def __init__(self) -> None:
        self.default_url = "https://flagcdn.com"
        self.organizations_url = "https://flagpedia.net/organization"
        self.name_to_iso = 0
        self.iso_to_name = 1

    def convert(self, code: str, how: int) -> (str | None):
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

    def get_flag(self, country_code: str, resolution: tuple[str, str] = (256, 192)) -> (bytes | None):
        url = f"{self.default_url}/{resolution[0]}x{resolution[1]}/{country_code}.png"
        response = requests.get(url)
        if not response.ok:
            return None
        else:
            return response.content
        
    def get_svg_flag(self, country_code: str) -> (str | None):
        url = f"{self.default_url}/{country_code}.svg"
        response = requests.get(url)
        if not response.ok:
            return None
        else:
            return response.content
        
    def get_organizations(self) -> dict[str, str]:
        response = requests.get(self.organizations_url)
        if not response.ok:
            return None
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            data = {}
            for li in soup.select('#content > div > ul')[0].find_all("li")[:-1]:
                data[li.a.span.text] = "https://flagpedia.net" + li.a.img["src"]
            
            return data
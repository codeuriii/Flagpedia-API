
import requests
import pycountry

class FlagpediaAPI:

    def __init__(self) -> None:
        self.default_url = "https://flagcdn.com"
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

    def get_waving_flag(self, country_code: str, resolution: tuple[int, int] = (256, 192)) -> (bytes | None):
        if resolution[0] > 256:
            raise ValueError("X resolution is too high")
        if resolution[1] < 12:
            raise ValueError('Y resolution is too low')
        
        if resolution[0] / 4 * 3 != resolution[1]:
            raise ValueError("The ratio is not 4/3")

        url = f"{self.default_url}/{resolution[0]}x{resolution[1]}/{country_code}.png"
        response = requests.get(url)
        if not response.ok:
            return None
        else:
            return response.content
        
    def get_svg_flag(self, country_code: str) -> (bytes | None):
        url = f"{self.default_url}/{country_code}.svg"
        response = requests.get(url)
        if not response.ok:
            return None
        else:
            return response.content
        
    
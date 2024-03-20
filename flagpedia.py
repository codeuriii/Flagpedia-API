
from bs4 import BeautifulSoup
import requests
import pycountry

class FlagpediaAPI:

    def __init__(self) -> None:
        self.default_url = "https://flagcdn.com"
        self.organizations_url = "https://flagpedia.net/organization"

    def get_name(self, country_iso: str) -> (str | None):
        try:
            language = pycountry.countries.get(alpha_2=country_iso)
            return language.name.lower()
        except AttributeError:
            return None

    def get_iso(self, country_name: str) -> (str | None):
        try:
            language = pycountry.countries.lookup(country_name)
            return language.alpha_2.lower()
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

    def get_flag_by_width(self, country_code: str, width: int = 2560) -> (bytes | None):
        possibles_width = [
            20, 40,
            80, 160,
            320, 640,
            1280, 2560
        ]

        if not width in possibles_width:
            raise ValueError(f"Current width {width} is not in possibles widths {possibles_width}")
        
        url = f"{self.default_url}/w{width}/{country_code}.png"
        response = requests.get(url)
        if response.ok:
            return response.content
        else:
            return None
        
    def get_svg_flag(self, country_code: str) -> (bytes | None):
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
                current_data = {}
                current_data["flag"] = "https://flagpedia.net" + li.a.img["src"].replace("h80", "w2560")
                current_data["iso"] = li.a["href"].split("/")[-1]
                

                current_org_response = requests.get(f"{self.organizations_url}")

                data[li.a.span.text] = current_data
            
            return data
# Flagpedia API

This is a unofficial API for Flagpedia

## Modules
- `requests`, you can install it with `pip install requests`
- `pycountry`, you can install it with `pip install pycountry`
- `BeautifulSoup`, you can install it with `pip install bs4`
- Install all required modules with
```bash
pip install requests pycountry bs4
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/codeuriii/flagpedia-api.git
```

2. Go to the repository
```bash
cd flagpedia-api
```

3. Demo code
```py
# Importing the module
from flagpedia import FlagpediaAPI

flagAPI = FlagpediaAPI()

# Get the country code iso
country_name = "France"
country_code = flagAPI.get_iso(country_name)

# Get bytes of waving flag png image         # Custom resolutions, always in 4:3
country_flag_bytes = flagAPI.get_flag(country_code, (256, 192))

# Write in a image
with open("french_flag.png", "wb") as f:
    f.write(country_flag_bytes)

```

# Questions

If you have **any** questions or ideas for the project, please send it in [issues page](https://github.com/codeuriii/Flagpedia-API/issues)

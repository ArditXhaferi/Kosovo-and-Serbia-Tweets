import pycountry

def get_country_name(country_code):
    country = pycountry.countries.get(alpha_2=country_code)

    if country is not None:
        return country.name
    else:
        return "test"
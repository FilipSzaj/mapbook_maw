import requests
from bs4 import BeautifulSoup
import folium

users: list = [
    {"name": "Filip", "location": "Ciechanów", "posts": 100,
     'picture': 'https://www.wig.wat.edu.pl/images/aktualnosci/2025/sklad_kpn_700.jpg'},
    {"name": "Mateusz", "location": "Węgorzewo", "posts": 94,
     'picture': 'https://www.wig.wat.edu.pl/images/aktualnosci/2025/sklad_kpn_700.jpg'},
    {"name": "Łukasz", "location": "Wrocław", "posts": 765,
     'picture': 'https://www.wig.wat.edu.pl/images/aktualnosci/2025/sklad_kpn_700.jpg'},
    {"name": "Kamil", "location": "Skierniewice", "posts": 93,
     'picture': 'https://www.wig.wat.edu.pl/images/aktualnosci/2025/sklad_kpn_700.jpg'},
    {"name": "Bartosz", "location": "Stalowa Wola", "posts": 50,
     'picture': 'https://www.wig.wat.edu.pl/images/aktualnosci/2025/sklad_kpn_700.jpg'},
]


def get_coordinates(city_name: str) -> list:
    address_url: str = f"https://pl.wikipedia.org/wiki/{city_name}"
    response = requests.get(address_url).text
    response_html = BeautifulSoup(response, "html.parser")
    longitude: float = float(response_html.select(".longitude")[1].text.replace(",", "."))
    # print(longitude)
    latitude: float = float(response_html.select(".latitude")[1].text.replace(",", "."))
    # print(latitude)
    return [latitude, longitude]


def get_map(users_data: list) -> None:
    mapa = folium.Map([52.3, 21.00], zoom_start=6)
    for user in users_data:
        folium.Marker(
            location=get_coordinates(city_name=user["location"]),
            popup=f'{user["name"]} <br/> {user["location"]} <br/> {user["posts"]}<br/>'
                  f'<img src="{user["picture"]}" alt="{user["picture"]}"/>'
        ).add_to(mapa)

    mapa.save("mapa.html")


get_map(users)

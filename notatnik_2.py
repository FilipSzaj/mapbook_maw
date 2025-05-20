class User:
    def __init__(self, name, surname, location, post):
        self.name = name
        self.surname = surname
        self.location = location
        self.post = post
        self.coordinates = self.get_coordinates()

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        address_url: str = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(address_url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude: float = float(response_html.select(".longitude")[1].text.replace(",", "."))
        # print(longitude)
        latitude: float = float(response_html.select(".latitude")[1].text.replace(",", "."))
        # print(latitude)
        return [latitude, longitude]

obiekt_1 = User(name="Hank", surname="Osbourne", location="Melbourne", post="19")

print(obiekt_1.name)
print(obiekt_1.surname)
print(obiekt_1.location)
print(obiekt_1.post)
print(obiekt_1.coordinates)

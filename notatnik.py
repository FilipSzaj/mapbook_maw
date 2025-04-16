users: list = [
    {"name": "Filip", "location": "Ciechanów", "posts": 100},
    {"name": "Kamil", "location": "Kraków", "posts": 83},
]

print(users)


def update_user(users_data: list[dict]) -> None:
    user_name=input("Podaj imię znajomego do aktualizacji: ")
    for user in users_data:
        if user["name"] == user_name:
            user["name"]=input("Podaj nowe imię znajomego: ")
            user["location"]=input("Podaj nową miejscowość: ")
            user["posts"]=int(input("Podaj nową ilość postów: "))


update_user(users)
print(users)
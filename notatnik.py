users: list = [
    {"name": "Filip", "location": "Ciechanów", "posts": 100},
    {"name": "Kamil", "location": "Kraków", "posts": 83},
]

print(users)


def remove_user(user_data:list[dict]) -> None:
    user_name=input("Podaj imię znajomego do usunięcia: ")
    for user in users:
        if user["name"] == user_name:
            users.remove(user)

remove_user(users)
print(users)
users:list=[
    {"name":"Filip","location":"Ciechanów","posts": 100},
    {"name":"Kamil","location":"SKierniewice","posts": 6},
    {"name":"Łukasz","location":"Wrocław","posts": 110},
    {"name":"Bartosz","location":"Stalowa Wola","posts": 300},

]


print(f"Witaj {users[0]["name"]}")

for user in users:
    print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował {user["posts"]} postów.")
def famous_births(scientists_dict):
    """
    Takes a dictionary of historical figures, sorts them by
    their birth date, and prints their details.
    """
    sorted_items = sorted(scientists_dict.items(), key=lambda item: item[1]['date_of_birth'])
   
    for key, info in sorted_items:
        print(f"{info['name']} is a great scientist born in {info['date_of_birth']}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
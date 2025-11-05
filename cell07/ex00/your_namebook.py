
def array_of_names(names_dict):
    """
    Takes a dictionary of {first: last} names and returns a list
    of full, capitalized names.
    """
    
    full_names_list = [f"{first.capitalize()} {last.capitalize()}" for first, last in names_dict.items()]
    
    return full_names_list

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
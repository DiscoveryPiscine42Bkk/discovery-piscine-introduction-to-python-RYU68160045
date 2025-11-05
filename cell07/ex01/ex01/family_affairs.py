
def find_the_redheads(family_dict):
    """
    Takes a dictionary of {name: hair_color} and returns
    a list of names (keys) that have 'red' as their value.
    """
    
    redheads = filter(lambda member: member[1] == 'red', family_dict.items())
    
   
    return [name for name, color in redheads]

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
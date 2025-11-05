def average(grades_dict):
    """
    Takes a dictionary of {student: score} and returns the
    average score for the class.
    """
    all_scores = grades_dict.values()
    total_sum = sum(all_scores)
    number_of_students = len(all_scores)
    
    if number_of_students == 0:
        return 0  
        
    return total_sum / number_of_students

class_3B = {
    "marine": 18,
    "jean": 15,
    "julien": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 10,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}")
print(f"Average for class 3C: {average(class_3C)}")
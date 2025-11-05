
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array_unique = []

seen = set()

for number in original_array:
    
    if number > 5:
        
        processed_number = number + 2
        
        if processed_number not in seen:
            new_array_unique.append(processed_number)
            seen.add(processed_number) 

print(original_array)

print(new_array_unique)
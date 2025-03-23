def count_value_frequency(dictionary, target):
    count = 0 
    for key in dictionary: 
        if dictionary[key] == target: 
            count += 1  
    return count 

test_dict = {
    'a': 2,
    'b': 3,
    'c': 2,
    'd': 4,
    'e': 2
}

target_value = 2

result = count_value_frequency(test_dict, target_value)
print("The number", target_value, "appears", result, "times in the dictionary.")
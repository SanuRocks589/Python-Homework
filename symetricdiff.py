def find_symmetric_difference(set1, set2):
    unique_in_set1 = set1 - set2  
    unique_in_set2 = set2 - set1  
    return unique_in_set1.union(unique_in_set2)  

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

result = find_symmetric_difference(setA, setB)

print("The symmetric difference is:", result)
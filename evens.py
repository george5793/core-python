def even_number_of_evens(numbers):
        
    count = 0
    
    # Spins through the numbers and adds to the count if an even number is found
    for num in numbers:
        if num % 2 == 0:
            count += 1
        else:
            continue
    
    # If no numbers, or all false numbers return False
    if count == 0:
        return False
    
    # If the number of even numbers is odd, return False
    elif count % 2 != 0:
        return False

    # If the number of even numbers is even return True
    elif count % 2 == 0:
        return True
        

even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12])
        
    
    
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")
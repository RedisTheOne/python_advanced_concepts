def is_odd(num):
    if num % 2 == 0:
        return False
    return True

def filter_odd_numbers(list, func):
    filtered_numbers = []
    
    for i in list:
        if func(i):
            filtered_numbers.append(i)
    
    return filtered_numbers

list = [1, 2, 3, 4, 5, 6, 7, 8]

print(filter_odd_numbers(list, is_odd))
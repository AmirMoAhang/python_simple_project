
def is_happy(number:int, seen_number:set = set()) -> bool:
    if number in seen_number:
        return False
    
    seen_number.add(number)
    
    k = sum([int(i) ** 2 for i in str(number)])
        
    if k == 1:
        return True   
    
    return is_happy(k, seen_number)

def addition_int(*args: int) -> int:
    result = 0
    
    for arg in args:
        result += arg
    return result

print(addition_int(1, 2, 3))
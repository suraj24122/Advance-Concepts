def upper_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@upper_decorator
def greet():
    return "good morning"

print(greet())  # Output: GOOD MORNING

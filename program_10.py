class TooSmallError(Exception):
    pass

try:
    age = 3
    if age < 5:
        raise TooSmallError("Too young to play!")
except TooSmallError as e:
    print(e)

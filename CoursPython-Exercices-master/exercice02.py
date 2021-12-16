def square(number):
    # Votre code ici
    number = int(number)
    number = number*number
    print(number)
    return number

def run():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    assert square(23) == 529
    assert square(-23) == 529

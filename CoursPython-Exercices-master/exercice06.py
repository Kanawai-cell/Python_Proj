def factorial(number):
    # Votre code ici  
    
    if number == 1 : 
        return number
    else:
        numbers = 1
        for i in range(2,number+1) :
            numbers = numbers*i
            print(numbers)
        if number <= 0 :
            numbers = -1*numbers
            return numbers
        return numbers

def run():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(-8) == -40320
def is_number_correct(number):
    # Votre code ici
    if number >= 10 or number <= 20 : 
        return True, 0
    elif number <= 10 : 
        number1 = number + 10
        return (False, 10 + number)
    elif number <= 10 : 
        return = (False, 10 - number)
    elif number >= 20 : 
        return  = (False, 20 - number)
    
    

def run():
    assert is_number_correct(0) == (False, 10)
    assert is_number_correct(10) == (True, 0)
    assert is_number_correct(20) == (True, 0)
    assert is_number_correct(21) == (False, -1)
    assert is_number_correct(50) == (False, -30)
    assert is_number_correct(15) == (True, 0)

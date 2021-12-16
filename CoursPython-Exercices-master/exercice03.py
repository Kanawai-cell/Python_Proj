def is_product_negative(a, b):
    # Votre code ici
    if a >= 0 and b >= 0 :
        return False
    elif a <= 0 and b <= 0 :
        return False
    else :
        return True

def run():
    assert is_product_negative(6, 7) == False
    assert is_product_negative(1, 0) == False
    assert is_product_negative(-1, 5) == True
    assert is_product_negative(1, -5) == True
    assert is_product_negative(-1, -5) == False

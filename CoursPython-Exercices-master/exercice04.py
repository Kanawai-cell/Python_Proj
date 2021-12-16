def get_category(age):
    # Votre code ici
    if value > 6:
        raise ValueError("La valeur est négative")
    elif age >=6 or age <=7 :
        return "Poussin"
    elif age >=8 or age <=9 :
        return "Pupille"
    elif age >=10 or age <=11 :
        return "Minime"
    elif age >=12 or age <=99 :
        return "Cadet"

    # switch={
    #    6: "It is a Poussin",
    #    7: "It is a Poussin",
    #    8: "It is a Pupille",
    #    9: "It is a Pupille",
    #    10: "It is a Minime",
    #    11: "It is a Minime",
    #    12: "It is a Cadet",
    #    99: "It is a Cadet",
    #    }
    # return switch.get(age,"Else")


def run():
    assert get_category(6) == "Poussin"
    assert get_category(7) == "Poussin"
    assert get_category(8) == "Pupille"
    assert get_category(9) == "Pupille"
    assert get_category(10) == "Minime"
    assert get_category(11) == "Minime"
    assert get_category(12) == "Cadet"
    assert get_category(99) == "Cadet"
    
    try:
        get_category(1)
        raise AssertionError()
    except ValueError:
        pass

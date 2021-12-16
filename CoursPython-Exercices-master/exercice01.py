a = 1
b = 2

# Votre code ici
# c = 0
# c = a #c=1
# b = c #b=1
# c = a

c = a #c=1
a = b #a=2
b = c #b=1

def run():
    assert a == 2
    assert b == 1

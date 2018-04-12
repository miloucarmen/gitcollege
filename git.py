import random

NAMES = ['Steven', 'Daan', 'Kees']

def get_name():
    return random.choice(NAMES)

print("Hoi, ik ben (naam)".format(naam=get_name()))
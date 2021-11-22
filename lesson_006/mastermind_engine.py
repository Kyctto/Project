from random import randint

def create_number():
    global secret_number
    a = randint(1,9)
    b = randint(0,9)
    while b == a:
        b = randint(0, 9)
    c = randint(0,9)
    while c == a or c == b:
        c = randint(0, 9)
    d = randint(0,9)
    while d == a or d == b or d == c:
        d = randint(0, 9)
    secret_number = [a,b,c,d]


def guess_the_number(client_number):
    client_number = int(client_number)
    cows = secret_number.count(client_number)


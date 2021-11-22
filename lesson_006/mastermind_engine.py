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
    print(secret_number)


def guess_the_number(client_number):
    client_number = list(client_number)
    cows = secret_number.count(int(client_number[0]))
    cows += secret_number.count(int(client_number[1]))
    cows += secret_number.count(int(client_number[2]))
    cows += secret_number.count(int(client_number[3]))
    bulls = 0
    if secret_number[0] == int(client_number[0]):
        bulls +=1
    if secret_number[1] == int(client_number[1]):
        bulls +=1
    if secret_number[2] == int(client_number[2]):
        bulls +=1
    if secret_number[3] == int(client_number[3]):
        bulls +=1
    cows -= bulls
    print(cows, bulls)



create_number()
guess_the_number('1234')





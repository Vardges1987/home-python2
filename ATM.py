collection = ['card', 'take', 'put', 'out']

def insert(card):
    if card == 'card':
        code = input('Enter code: ')
        if len(code) == 4:
            print(collection[1:]) 
            code = input('choose: put, take, out')       
        else:
            print('invalid code')
            exit()   

insert('card')


def card_function(put, take):
    balance = 0
    count = 0
    for money in put:
        print(money)
        if money % 50 == 0:
            balance += money

    for amount in take:
        if amount > 0:
            amount -= amount * 0.015  
            if amount * 0.015 > 600:  
                amount -= 600
        elif amount * 0.015 < 30:  
            amount -= 30
        balance -= amount    


    if sum(take + put) == 3:
        balance = balance + (balance * 0.03)
        sum = 0
        return balance

def function(out):
    exit()
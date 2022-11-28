from secrets import choice as ch
R = range(5)
alpha =  'abcdefghijklmnopqrstuvwxyz'

def oneRound():
    return ''.join([ch(alpha) for i in R])
L = '-'.join(oneRound() for i in R)

import sys

def collatz(number):
    if number != 1:
        if number % 2 == 0:
            num = number // 2
            print num
            return collatz(num)
        elif number % 2 == 1:
            num =  3 * number + 1
            print num
            return collatz(num)
        else:
            sys.exit
    else:
        print 'Collatz sequence complete!'

try:
    collatz(int(input('What\'s your starting number? ')))
except NameError:
    print 'Invalid input, integer values only.'

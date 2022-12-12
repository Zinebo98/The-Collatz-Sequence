def collatz(number):
    if (number % 2 == 0):
        return number // 2
    else:
        return 3 * number + 1

print('Enter a number:')
try:
    userNumber = int(input())
except ValueError:
    print('Please enter an intiger')

collatzNumber = userNumber
counter = 1

while(collatzNumber != 1):
    collatzNumber = collatz(collatzNumber)
    print(collatzNumber)
    counter +=1

print('The sequence reached 1 after ' + str(counter) + ' iterations')


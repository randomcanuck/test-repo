""" weight = float(input('Weight: '))


while True:
    unit = input('(K)g or (L)bs: ')
    if (unit == 'K' or unit == 'k' or unit == 'L' or unit == 'l'):
        break

if (unit == 'K' or unit == 'k'):
    print('Weight in Lbs:', weight*2.205)
else:
    print('Weight in Kgs:', weight/2.205) """

numbers = (1, 2, 3, 3)
print(numbers.count(3))

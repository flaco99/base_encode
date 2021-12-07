# Naomi Weissberg
# Created: Oct. 11, 2021
# converts from weird base number to decimal and or the other way

again = 'yes'
while (again == 'yes'):

    # ask which way the user wants to convert
    toDec_or_toB = ''
    while toDec_or_toB not in ('dec to base', 'base to dec'):
        toDec_or_toB = input('Decimal to base or base to decimal? Enter "dec to base" or "base to dec": ')

    # converts from weird base number to decimal
    if toDec_or_toB == 'base to dec':

    # ask the user for the base and number
        base = 0
        while base not in range(2,17):
            base = int(input('Input a base: '))
            
        valid_or_invalid = 'invalid'
        while valid_or_invalid == 'invalid':
            num_input = input('Input a number: ')
            for char in num_input:
                if (char.isdigit() == False) and (char not in 'ABCDEF'):
                    valid_or_invalid = 'invalid'
                    break
                else:
                    valid_or_invalid = 'valid'

        decimal_output = 0

    # go through each digit, change it to decimal, and add it to the decimal output
        length = len(num_input)
        for i in range (length):
            bit_index = length - 1 - i
            bit = num_input[bit_index]
            if bit.isdigit():
                decimal_output += int(bit)*(base)**i
                
    # change letters to integers if necessary
            elif bit in ('ABCDEF'):
                if bit == 'A':
                    decimal_output += 10*((base)**i)
                elif bit == 'B':
                    decimal_output += 11*((base)**i)
                elif bit == 'C':
                    decimal_output += 12*((base)**i)
                elif bit == 'D':
                    decimal_output += 13*((base)**i)
                elif bit == 'E':
                    decimal_output += 14*((base)**i)
                elif bit == 'F':
                    decimal_output += 15*((base)**i)

    # print the decimal sum output
        print(f'{num_input} in base {str(base)} equals {str(decimal_output)} in base 10.')

    # converts from decimal to weird base number
    else:

    # asks user for the base and number

        base = ''
        while base.isdigit() == False:
            base = input('Input a base: ')
        base = int(base)
            
        valid_or_invalid = 'invalid'
        while valid_or_invalid == 'invalid':
            num_input = input('Input a number: ')
            for char in num_input:
                if (char.isdigit() == False) and (char not in 'ABCDEF'):
                    valid_or_invalid = 'invalid'
                    break
                else:
                    valid_or_invalid = 'valid'
    
        num_input_original = num_input

    # set up a list that will contain the remainders
        Rlist = []

    # repeat dividing the number by the base until the quotient is smaller than the base
        while (int(num_input)) >= (int(base)):
            
            remainder = int(num_input) % base
            Rlist.append(remainder)
            num_input = int(num_input) // base

        Rlist.append(int(num_input))

    # change integers to letters if necessary
        for num in Rlist:
            newnum = num
            if num >= 10:
                if num == 10:
                    newnum = 'A'
                elif num == 11:
                    newnum = 'B'
                elif num == 12:
                    newnum = 'C'
                elif num == 13:
                    newnum = 'D'
                elif num == 14:
                    newnum = 'E'
                elif num == 15:
                    newnum = 'F'
                Rlist[Rlist.index(num)] = newnum
            Rlist[Rlist.index(newnum)] = str(newnum)
                    
    # prepare to print
        Rlist.reverse()
        num_output = ''.join(Rlist)

    # print the output
        print(f'Decimal {num_input_original} is equal to {str(num_output)} in base {str(base)}.')

    again = input('Would you like to try another? Enter "yes" or "no": ')
    while again not in ('yes', 'no'):
            again = input('Would you like to try another? Enter "yes" or "no": ')


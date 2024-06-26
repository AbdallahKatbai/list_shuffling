
import random

additions1 = ['1+1=', '1+2=', '1+3=', '1+4=', '1+5=', '1+6=', '1+7=', '1+8=', '1+9=',
                    '2+1=', '2+2=', '2+3=', '2+4=', '2+5=', '2+6=', '2+7=', '2+8=',
                    '3+1=', '3+2=', '3+3=', '3+4=', '3+5=', '3+6=', '3+7=',
                    '4+1=', '4+2=', '4+3=', '4+4=', '4+5=', '4+6=',
                    '5+1=', '5+2=', '5+3=', '5+4=', '5+5=',
                    '6+1=', '6+2=', '6+3=', '6+4=',
                    '7+1=', '7+2=', '7+3=',
                    '8+1=', '8+2=',
                    '9+1=']

subtractions1 = ['10-1=', '10-2=', '10-3=', '10-4=', '10-5=', '10-6=', '10-7=', '10-8=', '10-9=', '10-10=',
                       '9-1=', '9-2=', '9-3=', '9-4=', '9-5=', '9-6=', '9-7=', '9-8=', '9-9=',
                       '8-1=', '8-2=', '8-3=', '8-4=', '8-5=', '8-6=', '8-7=', '8-8=',
                       '7-1=', '7-2=', '7-3=', '7-4=', '7-5=', '7-6=', '7-7=',
                       '6-1=', '6-2=', '6-3=', '6-4=', '6-5=', '6-6=',
                       '5-1=', '5-2=', '5-3=', '5-4=', '5-5=',
                       '4-1=', '4-2=', '4-3=', '4-4=',
                       '3-1=', '3-2=', '3-3=',
                       '2-1=', '2-2=',
                       '1-1=']

addsub1 = additions1 + subtractions1

additions2 = ['5+5=', '5+6=', '5+7=', '5+8=', '5+9=',
              '6+4=', '6+5=', '6+6=', '6+7=', '6+8=', '6+9=',
              '7+3=', '7+4=', '7+5=', '7+6=', '7+7=', '7+8=', '7+9=',
              '8+2=', '8+3=', '8+4=', '8+5=', '8+6=', '8+7=', '8+8=', '8+9=',
              '9+1=', '9+2=', '9+3=', '9+4=', '9+5=', '9+6=', '9+7=', '9+8=', '9+9=',
              ]

add12 = additions1 + additions2

def inverse_operations(operations_list):
    inverted_list = []
    for i in operations_list:
        inverted_list.append(i[::-1].strip('=') + '=')
    return inverted_list

def print_list(operations_list, r=1):
    for i in range(len(operations_list)//r):
        print(operations_list[i] + '.')


def print_nmbrs(n):
    nmbrs = []
    for i in range(1, n):
        nmbrs.append(i)
    random.shuffle(nmbrs)
    for i in range(len(nmbrs)):
        print(nmbrs[i], '=> ')
    print('___________________')


def solve_list(operations_list):
    for i in range(len(operations_list)):
        print(operations_list[i] + str(eval(operations_list[i].rstrip('='))) + '.')

def add_tens(operations_list):
    new_list = []
    for i in operations_list:
        r = random.choice([0,2])
        new_list.append(i[:r] + str(random.randint(1, 8)) + i[r:len(i)])
    return new_list

def add_tens_first(operations_list):
    new_list = []
    for i in operations_list:
        new_list.append('1' + i)
        # new_list.append(str(random.randint(1, 8)) + i)
    return new_list

def give_examples(operations_list):
    random.shuffle(operations_list)
    print_list(operations_list)
    print('___________________')
    solve_list(operations_list)
    print('___________________')

def tens_additions_examples(operations_list):
    new_list = add_tens(operations_list)
    give_examples(new_list)

def tens_subtractions_examples(operations_list):
    new_list = inverse_operations(operations_list)
    new_list = add_tens_first(new_list)
    give_examples(new_list)

def give_multiple_examples(operations):  #'operations' is list
    for i in operations:
        give_examples(i)

tens_subtractions_examples(subtractions1[11:])
#give_examples(add12)
#give_multiple_examples([subtractions1, additions1])
#print_nmbrs(10)
#give_multiple_examples([additions2])

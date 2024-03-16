
import random

simple_additions = ['1+1=', '1+2=', '1+3=', '1+4=', '1+5=', '1+6=', '1+7=', '1+8=', '1+9=',
                    '2+1=', '2+2=', '2+3=', '2+4=', '2+5=', '2+6=', '2+7=', '2+8=',
                    '3+1=', '3+2=', '3+3=', '3+4=', '3+5=', '3+6=', '3+7=',
                    '4+1=', '4+2=', '4+3=', '4+4=', '4+5=', '4+6=',
                    '5+1=', '5+2=', '5+3=', '5+4=', '5+5=',
                    '6+1=', '6+2=', '6+3=', '6+4=',
                    '7+1=', '7+2=', '7+3=',
                    '8+1=', '8+2=',
                    '9+1=']

simple_subtractions = ['9-1=', '9-2=', '9-3=', '9-4=', '9-5=', '9-6=', '9-7=', '9-8=',
                       '8-1=', '8-2=', '8-3=', '8-4=', '8-5=', '8-6=', '8-7=',
                       '7-1=', '7-2=', '7-3=', '7-4=', '7-5=', '7-6=',
                       '6-1=', '6-2=', '6-3=', '6-4=', '6-5=',
                       '5-1=', '5-2=', '5-3=', '5-4=',
                       '4-1=', '4-2=', '4-3=',
                       '3-1=', '3-2=',
                       '2-1=']


def print_list(operations_list):
    for i in range(len(operations_list)):
        print(operations_list[i] + '.')


def solve_list(operations_list):
    for i in range(len(operations_list)):
        print(operations_list[i] + str(eval(operations_list[i].rstrip('='))) + '.')


def give_examples(operations_list):
    random.shuffle(operations_list)
    print_list(operations_list)
    print('___________________')
    solve_list(operations_list)
    print('___________________')


give_examples(simple_additions)

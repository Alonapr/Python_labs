""" 
This module contains such functions: main(), s(x,eps), _input_float(prompt=None, where=''), _check(x),
_check_1(e) and _input_with_check(prompt=None, check=lambda x: True, *, where='')
"""

print('This program calculates the sum of power series on the interval [-1, 1]')
print('This program is coded by Alona Predkova')

A = -1
B = 1

def s(x, eps):
    """ the function for calculation of the sum of power series
    returns float """
    x0 = 1
    sum = x0
    k = 0
    x3 = x * x * x
    while x0 >= eps or x0 <= -eps:
        x0 *= x3 / (3*k+1) / (3*k + 2) / (3*k + 3)
        sum += x0
        k += 1
    return sum

def _input_float (prompt=None, where=''):
    """ the function that inputs real numbers with thorough error check """
    try:
        x = input(prompt)
    except KeyboardInterrupt:
        raise Exception(where, 'Input was aborted')
    except:
        raise Exception(where, 'There are no input to convert to float')
    try:
        x = float(x)
    except ValueError:
        raise Exception(where, 'Input [',x,'] could not be converted to float')
    return x

def _check(x):
    """ the function for check of belongings of x to domain """
    return A <= x <= B

def _check_1(e):
    """ the function for input check of correct eps """
    return e > 0

def _input_with_check(prompt=None, check=lambda x: True, *, where=''):
    """ the main function that checks input real numbers,
belongings of x to domain and correct eps """
    x = _input_float(prompt, where)
    if not check(x):
        raise ValueError(where, 'Incorrect value')
    return x

def main():
    """ the main function """
    try:
        x = _input_with_check(f'Enter x [{A}; {B}]:\t', _check, where='In first value input - x')
        eps = _input_with_check('Enter eps more than 0:\t', _check_1, where='In second value input - eps')
        print('\n***** do calculations ... ', end='')
        s(x, eps)
        print('done')
        print('for x = ', f'{x:.{5}f}')
        print('for eps = ', f'{eps:.4e}')
        print('result = ', f'{s(x, eps):.{9}f}')

    except Exception as e:
        print('\n***** Error')
        print(e)
    except BaseException as e:
        print('Something went wrong')
main()
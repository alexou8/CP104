"""
-------------------------------------------------------
Lab 11, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-12-02"
-------------------------------------------------------
"""
# Imports
import random
import string
from random import randint


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []

    if value_type == 'int':
        for r in range(rows):
            temp_list = []
            for c in range(cols):
                b = randint(low, high)
                temp_list.append(b)
            matrix.append(temp_list)
    elif value_type == 'float':
        for r in range(rows):
            temp_list = []
            for c in range(cols):
                a = random.uniform(low, high)
                temp_list.append(a)
            matrix.append(temp_list)

    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    print('  ', end='')

    for c in range(0, len(matrix[0])):
        print('{:>7d}'.format(c), end='')

    print('')

    if value_type == 'int':
        for r in range(0, len(matrix)):
            print('{:>2d}'.format(r), end='')
            for c in range(0, len(matrix[r])):
                print('{:>7d}'.format(matrix[r][c]), end='')
            print('')
    else:
        for r in range(0, len(matrix)):
            print('{:>2d}'.format(r), end='')
            for c in range(0, len(matrix[r])):
                print('{:>7.2f}'.format(matrix[r][c]), end='')
            print('')

    return


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []

    for r in range(rows):
        temp_list = []
        for c in range(cols):
            temp_list.append((random.choice(string.ascii_letters)).lower())
        matrix.append(temp_list)

    return matrix


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    print('  ', end='')

    for c in range(0, len(matrix[0])):
        print('{:>7d}'.format(c), end='')
    print('')

    for r in range(0, len(matrix)):
        print('{:>2d}'.format(r), end='')
        for c in range(0, len(matrix[r])):
            print('{:>7.2}'.format(matrix[r][c]), end='')
        print('')

    return


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0

    for r in matrix:
        for c in r:
            smallest = min(smallest, c)
            largest = max(largest, c)
            total = total + c

    average = round(total / (len(matrix) * len(matrix[0])), 2)

    return(smallest, largest, total, average)


def count_frequency(matrix, char):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """
    count = 0

    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[r])):
            if matrix[r][c] == char:
                count += 1

    return count


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] *= num

    return

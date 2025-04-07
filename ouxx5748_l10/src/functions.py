"""
-------------------------------------------------------
Lab 10, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-25"
-------------------------------------------------------
"""
# Imports


def customer_first(fh):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """
    line = fh.readline()
    result = line.strip().split(",")
    first = result[-1]
    line = fh.readline()

    while line != "":
        data1 = line.strip().split(",")
        data2 = data1[-1]

        if first > data2:
            result = data1
            first = data2
        line = fh.readline()

    print("Find customer with earliest sign-in:")

    return result


def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    for i in fields:
        if i == fields[-1]:
            fh.write(str(i))
        else:
            fh.write(str(i) + ',')

    print(f"Data: {fields}")
    print("data appended to file")

    return


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    count = 0

    for i in fh:
        number = int(i.strip())
        if value == number:
            count += 1

    return count


def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    temp = ""

    for line in fh.read().split('/n'):
        for word in line.split():
            if len(word) >= len(temp):
                temp = word

    word = temp

    return word


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    count = 0
    fh_1.seek(0)
    lines = fh_1.readline()

    while lines != "" and count < n:
        print(lines, file=fh_2, end="")
        lines = fh_1.readline()
        count += 1

    return

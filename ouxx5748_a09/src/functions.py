"""
-------------------------------------------------------
Assignment 9, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-12-02"
-------------------------------------------------------
"""
# Imports


def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    count = 0

    while count < linecount:
        print(fh.readline(), end="")
        count += 1

    return


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    numbers = []

    for line in fh:
        lines = line.strip().split(',')
        for num in lines:
            if num.isdigit() and int(num) > 0:
                numbers.append(int(num))

    return numbers


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0

    for lines in fh:
        for char in lines:
            if ord(char) >= ord('A') and ord(char) <= ord('Z'):
                ucount += 1
            elif ord(char) >= ord('a') and ord(char) <= ord('z'):
                lcount += 1
            elif char.isnumeric():
                dcount += 1
            elif char == ' ':
                wcount += 1

    return(ucount, lcount, dcount, wcount)


def number_lines(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line = fh_in.readline()
    line_num = 0
    nums = []

    line_nums = f"[{line_num}] " + line
    nums.append(line_nums)
    line_num += 1

    for line in fh_in:
        line_nums = f"[{line_num}] " + line
        nums.append(line_nums)
        line_num += 1

    for i in nums:
        fh_out.write(i)

    return


def student_info(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_info(students)
    -------------------------------------------------------
    Parameters:
        students - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    l_id = -1
    h_id = -1

    low = float('inf')
    high = float('-inf')

    total = 0
    count = 0

    for line in students:

        info = line.split(",")
        total += float(info[-1])
        count += 1

        if(float(info[-1]) < low):
            low = float(info[-1])
            l_id = info[-2]
        if(float(info[-1]) > high):
            high = float(info[-1])
            h_id = info[-2]

        avg = round(total / count, 2)

        return l_id, h_id, avg

"""Convert to and from Roman numerals"""

import re

# Define exceptions
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

# Roman numerals must be less than 5000
MAX_ROMAN_NUMERAL = 4999

#Define digit mapping
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

#Create tables for fast conversion of roman numerals.
#See fillLookupTables() below.
toRomanTable = [ None ]  # Skip an index since Roman numerals have no zero
fromRomanTable = {}

def toRoman(n):
    """convert integer to Roman numeral"""
    # if not (0 < n < 5000):
    #     raise OutOfRangeError, "number out of range (must be 1..4999)"
    # if int(n) <> n:
    #     raise NotIntegerError, "non-integers can not be converted"

    # result = ""
    # for numeral, integer in romanNumeralMap:
    #     while n >= integer:
    #         result += numeral
    #         n -= integer
    # return result
    if not (0 < n <= MAX_ROMAN_NUMERAL):
        raise OutOfRangeError, "number out of range (must be 1..4999)"
    if int(n) <> n:
        raise NotIntegerError, "non-integers can not be converted"
    return toRomanTable[n]

# Define pattern to detect valid Roman numerals
# romanNumeralPattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
# New pattern, for performance boost using re.compile
#romanNumeralPattern = re.compile('^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$')
# New pattern, for performance boost using {m, n} syntax
#romanNumeralPattern = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
# Refactor again for readibility and maintainability
# romanNumeralPattern = re.compile('''
#     ^                   # beginning of string
#     M{0,4}              # thousands - 0 to 4 M's
#     (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
#                         #            or 500-800 (D, followed by 0 to 3 C's)
#     (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
#                         #        or 50-80 (L, followed by 0 to 3 X's)
#     (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
#                         #        or 5-8 (V, followed by 0 to 3 I's)
#     $                   # end of string
#     ''' ,re.VERBOSE)
# regex removed to use lookup table


def fromRoman(s):
    """ convert Roman numeral to integer """
#     if not s:
#         raise InvalidRomanNumeralError, 'Input can not be blank'
#     if not romanNumeralPattern.search(s):
#         raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % s
        
#     result = 0
#     index = 0
#     for numeral, integer in romanNumeralMap:
#         while s[index:index + len(numeral)] == numeral:
#             result += integer
#             index += len(numeral)
#     return result
    if not s:
        raise InvalidRomanNumeralError, 'Input can not be blank'
    if not fromRomanTable.has_key(s):
        raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s' % s
    return fromRomanTable[s]

def toRomanDynamic(n):
    """convert integer to Roman numeral using dynamic programming"""
    assert(0 < n <= MAX_ROMAN_NUMERAL)
    assert(int(n) == n)
    result = ""
    for numeral, integer in romanNumeralMap:
        if n >= integer:
            result = numeral
            n -= integer
            break  
    if n > 0:
        result += toRomanTable[n]
    return result

def fillLookupTables():
    """compute all the possible roman numerals"""
    #Save the values in two global tables to convert to and from integers.
    for integer in range(1, MAX_ROMAN_NUMERAL + 1):
        romanNumber = toRomanDynamic(integer)
        toRomanTable.append(romanNumber)
        fromRomanTable[romanNumber] = integer
    
fillLookupTables()


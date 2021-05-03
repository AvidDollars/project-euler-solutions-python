"""
Find the maximum total from top to bottom of the triangle

NOTE: vast majority of code is omitted
visit the URL below for full description
https://projecteuler.net/problem=18
"""

from description import problem
import re

### ↓↓↓ EXTRACT ROWS OF NUMBERS ###
NUMBERS_ROW = re.compile("(?:[>|\n])(\d.*\d)(?:<|<br|\s)")

p = problem(18)
result = re.findall(NUMBERS_ROW, p.text)[3:]

# final cleanup → contains list of lists of integers. Each inner list represents row of the triangle
arr_of_rows = [[int(num) for num in string.split(" ")] for string in result]

############# SOLUTION: ############
#TODO: implement solution
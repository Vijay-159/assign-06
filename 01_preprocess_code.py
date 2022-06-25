"""
Remove all one-line comments,
a comment which starts and ends on one line

Example
Input:
# This is a comment
print('remove_comments')

Output:
print('remove_comments')

Assumption (for this program):
All comments start at the beginning of the line
"""


import unittest


# Implement the below function and run this file
# Return the output, No need read input or print the ouput

def remove_comments(lines):
    """ 
    Input: lines of code as a string
    Returns: lines of code as a string after removing the comments.

    hint: 
        Use string methods like split and strip.
        Handle empty lines in code as well.
    """
    # implement your logic here
    pass


# DO NOT TOUCH THE BELOW CODE
class TestRemoveComments(unittest.TestCase):

    def test_01(self):
        code_with_comments = """
# This is a comment
print('remove_comments')
"""
        code_without_comments = """
print('remove_comments')
"""
        self.assertEqual(remove_comments(
            code_with_comments), code_without_comments)

    def test_02(self):
        code_with_comments = """
print('no comments to remove')
"""
        code_without_comments = """
print('no comments to remove')
"""
        self.assertEqual(remove_comments(
            code_with_comments), code_without_comments)

    def test_03(self):
        code_with_comments = """
# This is a comment before method
def sum(a, b):
    # this is a comment in method
    return a + b

sum(3, 4)
"""
        code_without_comments = """
def sum(a, b):
    return a + b

sum(3, 4)
"""
        self.assertEqual(remove_comments(
            code_with_comments), code_without_comments)

    def test_04(self):
        code_with_comments = """
# This is a comment before method
# This is another comment before method
def is_even(n):
    # this is a comment in method
    return n % 2 == 0

# call is_even
print('Is 5 even?: ', is_even(5))

# program ended
"""
        code_without_comments = """
def is_even(n):
    return n % 2 == 0

print('Is 5 even?: ', is_even(5))

"""
        self.assertEqual(remove_comments(
            code_with_comments), code_without_comments)


if __name__ == '__main__':
    unittest.main(verbosity=2)
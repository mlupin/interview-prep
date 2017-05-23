"""
Question 1
Given two strings s and t, determine whether some
anagram of t is a substring of s. For example: if s = "udacity" and t = "ad",
then the function returns True. Your function definition should look like:
question1(s, t) and return a boolean True or False.
"""
def question1(s, t):
    """Compare if t is part of s and return boolean"""

    # check if s and t are strings
    if type(s) != str or type(t) != str:
        return "Error: input params have to be strings"
    # check if strings are empty
    if t is "" or s is "":
        return "Error: strings cannot be empty"

    if t in s:
        return True
    else:
        return False

def test1():
    print "Testing question 1"
    print "Example test case (udacity, ud):", "Pass" if True == question1("udacity", "ud") else "Fail"
    print "Edge case (empty string):", "Pass" if "Error: strings cannot be empty" == question1("udacity", "") else "Fail"
    print "Edge case (not a string):", "Pass" if "Error: input params have to be strings" == question1("udacity", 1234) else "Fail"
    print "Case (not strings but equal params):", "Pass" if "Error: input params have to be strings" == question1(1.23, 1.23) else "Fail"
    print "Case (strings are same size):", "Pass" if True == question1("python", "python") else "Fail"
    print "Case (repeated substrings):", "Pass" if True == question1("rubyjavapythonrubyjavapython", "python") else "Fail"
    print "Case (long string):", "Pass" if True == question1("rubyjavapython2c++perlpython3sql123.45,67!!89--0%&", "python") else "Fail"


"""
Question 2
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
"""
def isPalindrome(s):
    return s == s[::-1]


def question2(s):
    # check if param is empty
    if s is "":
        return "Error: string cannot be empty"

    # check if a is a strings
    if type(s) != str:
        s = str(s)

    longest = 0
    left = 0
    right = 0

    for i in xrange(0, len(s)):
        for j in xrange(i + 1, len(s) + 1):
            substring = s[i:j]
            if isPalindrome(substring) and len(substring) > longest:
                longest = len(substring)
                left = i
                right = j
    # construct longest substring
    result = s[left:right]
    return result

def test2():
    print "\nTesting question 2"
    print "Edge case (empty string):", "Pass" if "Error: string cannot be empty" == question2("") else "Fail"
    print "Edge case (short string):", "Pass" if "1" == question2("1") else "Fail"
    print "Case (param is not a string and is a palindrom):", "Pass" if "121" == question2(121) else "Fail"



test1()
test2()

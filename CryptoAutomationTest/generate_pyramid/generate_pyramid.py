import pytest

#Print isosceles triangle
def isosceles_triangle(n,char):
    if n < 1 or n>20:  #Verify n is from 1 to 20
        return False

    if not isinstance(char, str):
        return False
    elif len(char) != 1: #Verify char is single char
        return False

    triangle =""
    for i in range(1,n+1):   #height for triangle
        spaces = " " * (n - i)
        chars = char * (2 * i - 1)
        triangle += spaces + chars + "\n"
    return triangle

def test_case_Happypath():
    result = isosceles_triangle(5,"*")
    expected = "    *\n   ***\n  *****\n *******\n*********\n"
    assert expected == result

def test_case_chanechar():
    result = isosceles_triangle(5, "#")
    expected = "    #\n   ###\n  #####\n #######\n#########\n"
    assert expected == result

def test_case_zeroheiht():
    result = isosceles_triangle(0,"*")
    expected = False
    assert expected == result

def test_case_heihtmorethan20():
    result = isosceles_triangle(21,"*")
    expected = False
    assert expected == result

def test_case_charisnotsinglechar():
    result = isosceles_triangle(5, "**")
    expected = False
    assert expected == result
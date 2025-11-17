#find the first non repeating character in the string
#swiss
from xml.dom.minidom import ProcessingInstruction


def first_non_element(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_element("swiss"))



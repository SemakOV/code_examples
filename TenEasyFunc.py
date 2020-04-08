"""Написать функцию, которая принимает любое количество позиционных аргументов - строк
и один парматер по-умолчанию glue, который равен ':'.
Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов.
Для соединения между любых двух строк вставлять glue.
Дополнительно: булевый флаг case по-умолчанию равный True.
Если флаг действителен: возвращаем новую строку,
где каждый символ входной приведен к верхнему регистру, иначе - к нижнему"""

# Произвольный набор через пробел в одну строку
# words = input().split(" ")
words = "sadx", "asdfc", "zsdsa"


def func(*args, case=True, glue=':'):
    if case:
        return glue.join([a.upper() for a in args if len(a) > 3])
    else:
        return glue.join([a.lower() for a in args if len(a) > 3])


print(func(*words, case=False))

"""Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon and
appending 1-interesting polygons to its rim,side by side.
You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below."""
from functools import reduce


def shapeArea(n):
    if n == 1:
        return 1
    else:
        a = n + (n - 1)
        b = [a]
        c = a
        for i in range(n):
            if c == 1:
                break
            else:
                d = (c - 2) * 2
                b.append(d)
                c = c - 2
        result = reduce(lambda x, y: x + y, b)
    return result


n = 8999
print(shapeArea(n))

"""Given a sequence of integers as an array,
determine whether it is possible to obtain a strictly increasing sequence
by removing no more than one element from the array.
Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
Sequence containing only one element is also considered to be strictly increasing."""
def almostIncreasingSequence(seq):
    last = seq[0]-1
    for i in range(len(seq)):
        if seq[i] <= last:
            s1 = seq[:i]+seq[i+1:]
            s2 = seq[:i-1]+seq[i:]
            return (sorted(s1) == s1 and len(s1) == len(set(s1))) or (sorted(s2) == s2 and len(s2) == len(set(s2)))
        last = seq[i]
    return True


sequence = [1, 3, 2]
print(almostIncreasingSequence(sequence))

"""After becoming famous,
the CodeBots decided to move into a new building together.
Each of the rooms has a different cost,
and some of them are free, but there's a rumour that all the free rooms are haunted!'
Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms,
or any of the rooms below any of the free rooms.
Given matrix, a rectangular matrix of integers,
where each value represents the cost of the room,
your task is to return the total sum of all rooms that are suitable for the CodeBots
(ie: add up all the values that don't appear below a 0)."""
def matrixElementsSum(matrix):
    zn = []
    a = 0
    for ind in range(len(matrix)):
        for item in range(len(matrix[ind])):
            if ind <= len(matrix) - 2:
                if matrix[ind][item] == 0:
                    matrix[ind + 1][item] = 0
            if matrix[ind][item] != 0:
                zn.append(matrix[ind][item])
    for i in zn:
        a += int(i)
    return a


matrix = [
    [0,1,1,2],
    [0,5,0,0],
    [2,0,3,3]
        ]
print(matrixElementsSum(matrix))
# matrix = [
#     [1,0,3],
#     [0,2,1],
#     [1,2,0]
#         ]
# print(matrixElementsSum(matrix))


"""
Given an array of strings, return another array containing all of its longest strings.

Example
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"]
"""
def allLongestStrings(inputArray):
    a = 0
    k = []
    for i in range(len(inputArray)):
        if len(inputArray[i]) > a:
            a = len(inputArray[i])
    for i in range(len(inputArray)):
        if len(inputArray[i]) == a:
            k.append(inputArray[i])
    return k

inputArray = [
    "aba",
    "aa",
    "ad",
    "vcd",
    "aba"]
print(allLongestStrings(inputArray))
# inputArray = [
#     "a",
#     "abc",
#     "cbd",
#     "zzzzzz",
#     "a",
#     "abcdef",
#     "asasa",
#     "aaaaaa"]
# print(allLongestStrings(inputArray))

"""
Given two strings, find the number of common characters between them.

Example
For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c".
"""
import math


def commonCharacterCount(s1, s2):
    setS1 = set(s1)
    setS2 = set(s2)
    lst = []
    sup_set = setS1.union(setS2)
    for i in sup_set:
        if i in s1 and i in s2:
            lst.append(min(list(s1).count(i),list(s2).count(i)))
    return sum(lst)


s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1, s2))

"""
Some people are standing in a row in a park.
There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
People can be very tall!

Example
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""
def sortByHeight(a):
    lst1 = []
    lst_ind = []
    for i in range(len(a)):
        if a[i] == -1:
            lst_ind.append(i)
            i += 1
        else:
            lst1.append(a[i])
    lst1.sort()
    for i in lst_ind:
        lst1.insert(i, -1)
    return lst1


sp = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
print(sortByHeight(sp))

"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example
For

picture = ["abc",
           "ded"]

the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""
def addBorder(picture):
    a = len(picture[0])
    b = ['*' * (a + 2), ]
    for i in picture:
        b.append(i.center(len(i) + 2, '*'))
    b.append('*' * (a + 2))
    return b


picture = [
        "aa",
        "**",
        "zz"]
print(addBorder(picture))
# picture = ["wzy**"]
# print(addBorder(picture))

"""
Two arrays are called similar if one can be obtained from another by swapping at most
one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.

Example
For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
"""
def areSimilar(a, b):
    if sorted(a) == sorted(b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count == 2 or count == 0
    else:
        return False


a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
print(areSimilar(a, b))
# a: [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
# b: [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
# print(areSimilar(a, b))

"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating
in a computer network that uses the Internet Protocol for communication.
There are two versions of the Internet protocol, and thus two versions of addresses.
One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.
"""
def isIPv4Address(inputString):
    flag = []
    numb = inputString.split('.')
    if len(numb) == 4:
        for i in numb:
            if i.isdigit():
                if i[0] == '0' and len(i) > 1:
                        flag.append(False)
                elif int(i) <= 255 and int(i) >= 0:
                    flag.append(True)
                else:
                    flag.append(False)
            else:
                flag.append(False)
    return flag == [True, True, True, True]

inputString = "0..1.0.0"
print(isIPv4Address(inputString))
inputString = "0.1.1.256"
print(isIPv4Address(inputString))
inputString ="64.00.161.131"
print(isIPv4Address(inputString))

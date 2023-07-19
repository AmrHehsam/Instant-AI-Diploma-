# #1-Write a Python program to calculate the length of a string using 2 ways
#
# #way no.1
# string = input("String: ")
# stringLength = len(string)
# print(stringLength)
#
# #way no.2
# string = input("String: ")
# stringLength = 0
# for char in string:
#     stringLength += 1
# print(stringLength)


# #2-Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2,
# # return the empty string instead ("##Sample String : 'w3resource' Expected Result : 'w3ce' ##Sample String : 'w3' Expected Result : 'w3w3'
# ##Sample String : ' w' Expected Result : Empty String)
#
# string = input("String: ")
# if len(string) < 2:
#     pass
# else:
#     print(string[0:2] + string[-2::])


# #3-Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with
# # 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. (Sample String : 'abc'Expected Result : 'abcing')
#
# string = input("String: ")
# if len(string) < 3:
#     pass
# elif string[-3::] == "ing":
#     string += "ly"
# else:
#     string += "ing"
# print(string)


# #4-Write a Python function that takes a list of words and return the longest word and the length of the longest one
# #(Longest word: Exercises Length of the longest word: 9)
#
# string = input("String: ")
# strings = string.split()
# maxLength = 0
# maxWord = ''
# for str in strings:
#     if len(str) > len(maxWord):
#         maxWord = str
#         maxLength = len(maxWord)
# print(maxWord + ":", maxLength)


# #5-Write a Python program to change a given string to a newly string where the first and last chars have been exchanged
# # using 2 ways (Sample String:abca  Expected Result:ebce)
#
# #way no.1
# string = input("String: ")
# print(string[-1] + string[1:-1] + string[0])
#
# #way no.2
# string = input("String: ")
# firstCh = string[0]
# lastCh = string[-1]
# midStr = string[1:-1]
# string = lastCh + midStr + firstCh
# print(string)


# #6-Write a Python program to remove characters that have odd index values in a given string
# #(Sample String:abca Expected Result:ac)
#
# string = input("String: ")
# print(string[0::2])


# #7-Write a Python program to count the occurrences of each word in a given sentence
# #(Sample String:amr and ahmed are frindes but amr is the tallest Expected Result:2)
#
# string = input("String: ")
# stringSet = set(string.split())
# maxWord = ''
# maxOccurence = 0
# for word in stringSet:
#     if len(word) > 1:
#         occurence = string.count(word)
#         if occurence > maxOccurence:
#             maxOccurence = occurence
#             maxWord = word
# print(maxWord+':', maxOccurence)


# #8-Write a Python script that takes input from the user and displays that input back in upper and lower cases
#
# string = input("String: ")
# upperStr = string.upper()
# lowerStr = string.lower()
# print(upperStr)
# print(lowerStr)


# #9-Write a Python function to reverse a string if its length is a multiple of 4
#
# string = input("String: ")
# if len(string) % 4 == 0:
#     print(string[::-1])


# #10- Write a Python program to remove a newline in Python
#
# string = "\nI \nam \ncoding\n"
# str = ''
# for ch in string:
#     if ch == '\n':
#         pass
#     else:
#         str += ch
# print(str)


# #11-Write a Python program to check whether a string starts with specified characters
#
# string = input("string: ")
# chars = input("characters: ")
# check = True
# chLen = len(chars)
# i = 0
# for ch in chars:
#     if ch == string[i]:
#         i += 1
#     else:
#         check = False
# if(check):
#     print(string + " starts with " + chars)
# else:
#     print(string + " doesn't starts with " + chars)


# #12- Write a Python program to add prefix text to all of the lines in a string
#
# string = "Hello \nInstant \ncomputer Science"
# prefix = input("prefix: ")
# str = prefix
# for ch in string:
#     if ch == '\n':
#         str += ch
#         str += prefix
#     else:
#         str += ch
# print(str)


# #13-Write a Python program to print the following numbers up to 2 decimal places
#
# number = float(input("Number: "))
# print ("{:.2f}".format(number))


# #14-Write a Python program to print the following numbers up to 2 decimal places with a sign
#
# number = float(input("Number: "))
# if number > 0:
#     print ('+' + "{:.2f}".format(number))
# else:
#     print ("{:.2f}".format(number))


# #15-Write a Python program to display a number with a comma separator
#
# number = int(input("Number: "))
# print("{:,}".format(number))


# #16-Write a Python program to reverse a string using 2 ways
#
# #way no.1
# string= input("String: ")
# print(string[::-1])
#
# #way no.1
# string = input("String: ")
# i = len(string) - 1
# while i >= 0:
#     print(string[i], end='')
#     i -= 1


# #17-Write a Python program to count repeated characters in a string (hint:use dictionary)
#
# string = input("String: ")
# repeated = {}
# for ch in string:
#     if ch in repeated:
#         repeated[ch] += 1
#     else:
#         repeated[ch] = 1
# print(repeated)


# #18-Write a Python program to find the first non-repeating character in a given string
# string = input("String: ")
# repeated = {}
# for ch in string:
#     if ch in repeated:
#         repeated[ch] += 1
#     else:
#         repeated[ch] = 1
# found = False
# for ch in repeated:
#     if repeated[ch] == 1:
#         print(ch)
#         found = True
#         break
# if not found:
#     print("All characters are repeated!")


# #19-Write a Python program to remove spaces from a given string
#
# string = input("String: ")
# print(string.replace(' ', ''))


# #20-Write a Python program to count the number of non-empty substrings of a given string
#
# string = input("String: ")
# print((len(string)*(len(string)+1))/2)


# #21-write a Python program to swap first and last element of any list.
#
# size = int(input("List Size: "))
# list = []
# for i in range (0,size):
#     list.append(input(f"Element index {i}: "))
# temp = list[0]
# list[0] = list[size-1]
# list[size-1] = temp
# print(list)


# #22-Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
# # (Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3 Output : [19, 65, 23, 90])
#
# size = int(input("List Size: "))
# list = []
# for i in range (0,size):
#     list.append(input(f"Element index {i}: "))
# pos1 = int(input("pos1: "))
# pos2 = int(input("pos2: "))
# temp = list[pos1]
# list[pos1] = list[pos2]
# list[pos2] = temp
# print(list)


# #23- search for the all ways to know the length of the list
#
# #way no.1
# list = ["Mohamed", "Amr", "Hesham"]
# print(len(list))
#
# #way no.2
# list = ["Mohamed", "Amr", "Hesham"]
# size = 0;
# for elements in list:
#     size+=1
# print(size)
#
# #way no.3
# list = ["Mohamed", "Amr", "Hesham"]
# print(list.__len__())
#
# #way no.4
# from operator import length_hint
# list = ["Mohamed", "Amr", "Hesham"]
# print(length_hint(list))


# #24-write a Python code to find the Maximum number of list of numbers.
#
# size = int(input("List size: "))
# list = []
# for i in range(0,size):
#     list.append(int(input(f"Element index {i}: ")))
# max = list[0]
# for elements in list:
#     if elements > max:
#         max = elements
# print(max)


# #25-write a Python code to find the Minimum number of list of numbers.
#
# size = int(input("List size: "))
# list = []
# for i in range(0,size):
#     list.append(int(input(f"Element index {i}: ")))
# min = list[0]
# for elements in list:
#     if elements < min:
#         min = elements
# print(min)


# #26-search for if an elem is existing in list
#
# size = int(input("List size: "))
# list = []
# for i in range(0,size):
#     list.append(input(f"Element index {i}: "))
# search = input("Element to search for: ")
# found = False
# for elements in list:
#     if elements == search:
#         found = True
# if found:
#     print(f"element {search} is found!")
# else:
#     print(f"element {search} is not found!")


# #27- clear python list using different ways
#
# #way no.1
# list = [1,2,3,4,5,6,7,8,9]
# list.clear()
# print(list)
#
# #way no.2
# list = [1,2,3,4,5,6,7,8,9]
# size = len(list)
# for i in range(0,size):
#     list.remove(list[0])
# print(list)
#
# #way no.3
# list = [1,2,3,4,5,6,7,8,9]
# size = len(list)
# for i in range (0,size):
#     list.pop()
# print(list)


# #28-remove duplicated elements from a list
#
# size = int(input("Size: "))
# lst = []
# for i in range(0,size):
#     lst.append(input(f"Element index {i}: "))
# lst = list(set(lst))
# print(lst)


# # 29-Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.
# # (Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”] Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}])
#
# size1 = int(input("Size of Test list: "))
# testList = []
# for i in range(0,size1):
#     testList.append(input(f"Element index {i}: "))
# size2 = int(input("Size of Key list: "))
# keyList = {}
# for i in range(0,size2):
#     keyList.append(input(f"Element index {i}: "))
# dictionary = []
# for i in range(0,size1,2):
#     dictionary.append({keyList[0] : testList[i],keyList[1] : testList[i+1]})
# print(dictionary)


# # 30-write a python program to count unique values inside a list using different ways
#
# #way no.1
# list = [1,2,3,4,5,6,7,8,9,1,3,2]
# uniqueList = {}
# for item in list:
#     if item in uniqueList:
#         uniqueList[item] += 1
#     else:
#         uniqueList[item] = 1
# count = 0
# for item in uniqueList:
#     if uniqueList[item] == 1:
#         count += 1
# print(count)
#
# #way no.2
# list = [1,2,3,4,5,6,7,8,9,1,3,2]
# count = 0
# for item in list:
#     if list.count(item) == 1:
#         count += 1
# print(count)
#
# #way no.3
# list = [1,2,3,4,5,6,7,8,9,1,3,2]
# lst = []
# count = 0
# for item in list:
#     if item not in lst:
#         lst.append(item)
#         count += 1
#     else:
#         count -= 1
# print(count)


# #31-write a python program Extract all elements with Frequency greater than K (Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 Output : [4, 3])
#
# size = int(input("Size: "))
# lst = []
# for i in range(0,size):
#     lst.append(input(f"Element index {i}: "))
# k = int(input("K: "))
# freqLst = []
# for item in lst:
#     if lst.count(item) > k:
#         if item not in freqLst:
#             freqLst.append(item)
# print(freqLst)


# #32-write a python program to find the Strongest Neighbour (Input: 1 2 2 3 4 5 Output: 2 2 3 4 5)
#
# size = int(input("Size: "))
# lst = []
# for i in range(0,size):
#     lst.append(input(f"Element index {i}: "))
# lst2 = []
# for i in range(1,size):
#     mx = max(lst[i], lst[i-1])
#     lst2.append(mx)
# print(lst2)


# #33-write a Python Program to print all Possible Combinations from the three Digits
# # (Input: [1, 2, 3] Output:1 2 3 ## 1 3 2 ## 2 1 3 ## 2 3 1 ## 3 1 2 ## 3 2 1)
#
# lst = []
# for i in range(0,3):
#     lst.append(input(f"Element index {i}: "))
# for i in range(0,3):
#     for j in range(0, 3):
#         for k in range(0, 3):
#             if i != j and i != k and j != k:
#                 print(lst[i], lst[j], lst[k])


# #34-write a Python program to find all the Combinations in the list with the given condition
# # (Input: test_list = [1,2,3] Output:  [1], [1, 2], [1, 2, 3], [1, 3] [2], [2, 3], [3])
#
# lst = []
# for i in range(0, 3):
#     lst.append(input(f"Element index {i}: "))
# kBool = False
# for i in range(0, 3):
#     print(lst[i])
#     if(i < 2):
#         print(lst[i], lst[i+1])
#     if(i < 1):
#         print(lst[i], lst[i+1], lst[i+2])


# #35-write a Python program to get all unique combinations of two Lists
# # (List_1 = ["a","b"] List_2 = [1,2] Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] )
#
# list1 = []
# for i in range(0, 2):
#     list1.append(input(f"Element index {i} of list1: "))
# list2 = []
# for i in range(0, 2):
#     list2.append(input(f"Element index {i} of list2: "))
# uniqueComb = []
# lst = []
# for i in range(0, 2):
#     tup = (list1[i], list2[i])
#     lst.append(tup)
#     if i == 1:
#         uniqueComb.append(lst)
# lst = []
# for i in range(0, 2):
#     if i == 0:
#         tup = (list1[i], list2[1])
#     else:
#         tup = (list1[i], list2[0])
#     lst.append(tup)
#     if i == 1:
#         uniqueComb.append(lst)
# print(uniqueComb)


# #36-Remove all the occurrences of an element from a list in Python (Input : 1 1 2 3 4 5 1 2 1 Output : 2 3 4 5 2)
#
# size = int(input("Size: "))
# lst = []
# for i in range(0,size):
#     lst.append(input(f"Element index {i}: "))
# element = input("Element to be removed: ")
# for i in range(0,lst.count(element)):
#     lst.remove(element)
# print(lst)


# #37-write a python program to Replace index elements with elements in Other List
# # (The original list 1 is : [‘Gfg’, ‘is’, ‘best’] The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
# # The lists after index elements replacements is : [‘Gfg’, ‘is’, ‘best’, ‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’])
#
# size1 = int(input("List1 size: "))
# list1 = []
# for i in range(0, size1):
#     list1.append(input((f"Element index {i}: ")))
# size2 = int(input("List2 size: "))
# list2 = []
# for i in range(0, size2):
#     list2.append(input((f"Element index {i}: ")))
# for i in range(0, size2):
#     list2[i] = list1[int(list2[i])]
# print(list2)


# # 38-write python program to Retain records with N occurrences of K (Input : test_list = [(4, 5, 5, 4), (5, 4, 3)],
# # K = 5, N = 2 Output : [(4, 5, 5, 4)] Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 3 Output : [] )
#
# lst = [(4,5,5,4),(5,4,3)]
# lst2 = []
# k = 5
# n = 2
# for tup in lst:
#     if tup.count(k) == n:
#         lst2.append(tup)
# print(lst2)


# # 39-write a Python Program to Sort the list according to the column using lambda array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# # Output :Sorted array specific to column 0, [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# # Sorted array specific to column 1, [[2, 1, 2], [3, 2, 1], [1, 3, 3]] Sorted array specific to column 2, [[3, 2, 1], [2, 1, 2], [1, 3, 3]]
#
# lst = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# for i in range(len(lst[0])):
#     sortedCol = sorted(lst, key=lambda x: x[i])
#     print(f"Sorted by Column{i}", sortedCol)


# #40- write a program to Sort Python Dictionaries by Key or Value Input: {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# #Output: {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}
#
# dic = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# lst = list(dic.keys())
# lst.sort()
# sortedDict = {i: dic[i] for i in lst}
# print(sortedDict)

#!/usr/bin/python3

# Questions:
# how long should the bin string be?
# for the binary are we expexcted to remove the spaces if there are some in the document? The instructions are unclear.


import re
import csv


def main():
    # create array, store the function name, string
    yes = 0
    no = 0
    index = 0
    count = 0
    i = 0
    noCall = 0
    rules = ["student,", "password,", "username,", "email,", "previous,", "phone,", "postal,", "address,", "binary,",
             "bio,", "\n"]
    badChars = ["\n"]
    stringList = list()

    with open("/home/caboose/Desktop/ssd/assignment1Regex/sampleFile.csv", "r") as data:
        for ruleCombo in data:
            for i in range(0, len(rules)):
                if rules[i] in ruleCombo:
                    # print(ruleCombo)
                    rule, info = ruleCombo.split(",")
                else:
                    continue
            stringList.append(rule)
            stringList.append(info)
        # read whole file into array,
        # To check each of the functions that are to be called.
        for i in range(0, len(stringList)):
            if "student" in stringList[i]:
                student(stringList[i + 1])
                i = i + 1
            elif "password" in stringList[i]:
                password(stringList[i + 1])
                i = i + 1
            elif "username" in stringList[i]:
                username(stringList[i + 1])
                i = i + 1
            elif "email" in stringList[i]:
                email(stringList[i + 1])
                i = i + 1
            elif "previous" in stringList[i]:
                previous(stringList[i + 1], stringList[i - 1])
                i = i + 1
            elif "phone" in stringList[i]:
                phone(stringList[i + 1])
                i = i + 1
            elif "postal" in stringList[i]:
                postal(stringList[i + 1])
                i = i + 1
            elif "address" in stringList[i]:
                address(stringList[i + 1])
                i = i + 1
            elif "binary" in stringList[i]:
                binary(stringList[i + 1])
                i = i + 1
            elif "bio" in stringList[i]:
                bio(stringList[i + 1])
                i = i + 1
            else:
                noCall = noCall + 1

        print(yes)
        print(no)
        print(noCall)


# This can be used to verify the strings that are being shown as "right"
# print ( re.search("[a-zA-Z0-9]{3,20}@[a-zA-Z]+\\.(ca|com|org|gov|net|int|edu)$", regex) )
def student(string):
    regex = string.strip()
    # Checks for 0-9 for 9 or [0-9]{3}_x3
    print(re.search('([0-9]){9}|[0-9]{3} [0-9]{3} [0-9]{3}', regex))
    if re.search('([0-9]){9}|[0-9]{3} [0-9]{3} [0-9]{3}', regex):
        print("student: " + regex + " yes")
    else:
        print("student: " + regex + " no")


def password(string):
    regex = string.replace('\n', '')
    print(re.search('^[ -~]{12}', regex))
    # [ -~] does all ascii characters minimum of 12
    if re.search('^[ -~]{12}', regex):
        print("password: " + regex + " yes")
    else:
        print("password: " + regex + " no")


def username(string):
    regex = string.replace('\n', '')
    print(re.search('^[a-zA-Z0-9]{3,20}', regex))

    if re.search('^[a-zA-Z0-9]{3,20}', regex):
        print("username: " + regex + " yes")
    else:
        print("username: " + regex + " no")


def email(string):
    # .net, .ca .com . org .gov .int .edu
    # lots of edge cases to look at.
    regex = string.replace('\n', '')

    if re.search("[a-zA-Z0-9]{3,20}@[a-zA-Z]+\\.(ca|com|org|gov|net|int|edu)$", regex):
        print(re.search("[a-zA-Z0-9]{3,20}@[a-zA-Z]+\\.(ca|com|org|gov|net|int|edu)$", regex))
        print("email: " + regex + " yes")
    else:
        print("email: " + regex, " no")


def previous(string, previousString):
    # remove the leading info using regex, save it? then check both
    regex = string.replace('\n', '')
    if string == previousString:
        print("previous: " + regex + " yes")
    else:
        print("previous: " + regex, " no")


def phone(string):
    regex = string.replace('\n', '')
    if re.search('^(\\([0-9]{3}\\)|[0-9]{3}\\.|[0-9]{3}-|[0-9]{10})[0-9]{3}(\\.|-)[0-9]{4}', regex):
        print(re.search('(\\([0-9]{3}\\)|[0-9]{3}\\.|[0-9]{3}-|[0-9]{10})', regex))
        print("phone: " + regex + " Yes")
    else:
        print("phone: " + regex + " no")


def postal(string):
    regex = ''
    regex = string.replace('\n', '')

    if re.search('([A-Za-z][0-9][A-Za-z] |[A-Za-z][0-9][A-Za-z])[0-9][A-Za-z][0-9]', regex):
        print(re.search('([A-Za-z][0-9][A-Za-z] |[A-Za-z][0-9][A-Za-z])[0-9][A-Za-z][0-9]', regex))
        print("postal: " + regex + " yes")
    else:
        print("postal: " + regex, " no")


def address(string):
    regex = string.replace('\n', '')
    if re.search('[0-9]{2,4}( |-[0-9]{1,3}|#[0-9]{1,3})[a-zA-Z]+[A-Za-z]+(\\.|)', regex):
        print("address: " + regex + " yes")
    else:
        print("address: " + regex, " no")


# TODO binary numbers and questions for nick
def binary(string):
    regex = string.replace('\n', '')
    if re.search('[0-1]{2,}', regex):
        print(re.search('[0-1]{2,}', regex))
        print("binary: " + regex + " yes")
    else:
        print("binary: " + regex, " no")


def bio(string):
    regex = string.replace('\n', '')
    if re.search('<([a-zA-Z]+)(>|| )[\\w]+</([a-zA-Z]+)>', regex):
        print(re.search('<([a-zA-Z]+)(>|| )[\\w]+</([a-zA-Z]+)>', regex))
        print("bio: " + regex + " yes")
    else:
        print("bio: " + regex, " no")


if __name__ == "__main__":
    main()

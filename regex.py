#!/usr/bin/python3
from pyfiglet import Figlet
from texttable import Texttable
import re
import csv


# TODO Currently cant do inputs like: bio,bio,bio
# TODO Check really large stuff
def main(location):
    yes = 0
    no = 0
    rules = ["student,", "password,", "username,", "email,", "previous,", "phone,", "postal,", "address,", "binary,",
             "bio,"]
    stringList = list()
    # csv parser
    with open(location, "r") as data:
        for ruleCombo in data:
            for i in range(0, len(rules)):
                if ',' in ruleCombo:
                    rule, info = ruleCombo.split(',', 1)
                    stringList.append(rule)
                    stringList.append(info)
                    break
                else:
                    ruleCombo.replace('\n', '')
                    break
        # To check each of the functions that are to be called.
        for i in range(0, len(stringList)):
            if "student" in stringList[i]:
                result = student(stringList[i + 1])
                i = i + 1
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            elif "password" in stringList[i]:
                result = password(stringList[i + 1])
                i = i + 1
                
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            elif "username" in stringList[i]:
                result = username(stringList[i + 1])
                i = i + 1
                
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            elif "email" in stringList[i]:
                result = email(stringList[i + 1])
                i = i + 1
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            elif "previous" in stringList[i]:
                result = previous(stringList[i + 1], stringList[i - 1])
                i = i + 1
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            elif "phone" in stringList[i]:
                result = phone(stringList[i + 1])
                i = i + 1
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            elif "postal" in stringList[i]:
                result = postal(stringList[i + 1])
                i = i + 1
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            elif "address" in stringList[i]:
                result = address(stringList[i + 1])
                i = i + 1
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            elif "binary" in stringList[i]:
                result = binary(stringList[i + 1])
                i = i + 1
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            elif "bio" in stringList[i]:
                result = bio(stringList[i + 1])
                i = i + 1
                if result == 0:
                    yes = yes + 1
                else:
                    no = no + 1
            else:
                continue

        t = Texttable()
        t.add_rows([["Category", "Totals"], ['Yes', yes], ['No', no]])
        print(t.draw())


# This can be used to verify the strings that are being shown as "right"
# print ( re.search("[a-zA-Z0-9]{3,20}@[a-zA-Z]+\\.(ca|com|org|gov|net|int|edu)$", regex) )
def student(string):
    regex = string.strip()
    # Checks for 0-9 for 9 or [0-9]{3}_x3
    if re.search('([0-9]){9}|[0-9]{3} [0-9]{3} [0-9]{3}', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def password(string):
    regex = string.replace('\n', '')
    if re.search('^[ -~]{12}', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def username(string):
    regex = string.replace('\n', '')

    if re.search('^[a-zA-Z0-9]{3,20}', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def email(string):
    # .net, .ca .com . org .gov .int .edu
    # lots of edge cases to look at.
    regex = string.replace('\n', '')
    if re.search("[a-zA-Z0-9]{3,20}@[a-zA-Z]+\\.(ca|com|org|gov|net|int|edu)$", regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def previous(string, previousString):
    # remove the leading info using regex, save it? then check both
    regex = string.replace('\n', '')
    if string == previousString:
        print("yes")
        return 0
    else:
        print("no")
        return 1


def phone(string):
    regex = string.replace('\n', '')
    if re.search('^(\\([0-9]{3}\\)|[0-9]{3}\\.|[0-9]{3}-|[0-9]{10})[0-9]{3}(\\.|-)[0-9]{4}', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def postal(string):
    regex = ''
    regex = string.replace('\n', '')

    if re.search('([A-Za-z][0-9][A-Za-z] |[A-Za-z][0-9][A-Za-z])[0-9][A-Za-z][0-9]', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def address(string):
    regex = string.replace('\n', '')
    if re.search('[0-9]{2,4}( |-[0-9]{1,3}|#[0-9]{1,3})[a-zA-Z]+[A-Za-z]+(\\.|)', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def binary(string):
    regex = string.replace('\n', '')
    if re.search('[0-1]+', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def bio(string):
    regex = string.replace('\n', ' ')
    if re.search('<([a-zA-Z]+)(>||[ -~]+)[ -~]*(</[a-zA-Z]+|)>', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


if __name__ == "__main__":
    custom_font = Figlet(font='jazmine')
    print(custom_font.renderText("Regex Machine"))

    location = input("Enter the file location (/path/to/file) or 1 for default: ")
    if location == 1:
        location = '/home/caboose/Desktop/ssd/assignment1Regex/sampleFile.csv'
        main(location)
    else:
        main(location)

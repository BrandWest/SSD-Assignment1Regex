#!/usr/bin/python3
from pyfiglet import Figlet
from texttable import Texttable
import re
import csv


# TODO Currently cant do inputs like: bio,bio,bio
# TODO Check really large stuff
def main():
    yes = 0
    no = 0
    oob = 0
    rules = ["student,", "password,", "username,", "email,", "previous,", "phone,", "postal,", "address,", "binary,",
             "bio,"]
    stringList = list()
    # csv parser

    while True:
        location = input("Enter the file location (/path/to/file) or 1 for default: ")
        try:
            if location == '1':
                location = '/home/caboose/Desktop/ssd/assignment1Regex/nicksFile.csv'
                break
            else:
                break
        except FileNotFoundError:
            print("Unable to locate file.")
        except PermissionError:
            print("Invalid permissions, try another file")
    try:
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
    except FileNotFoundError:
        print("Unable to locate file.")
        main()
    except PermissionError:
        print("Invalid permissions, try another file")
        main()
        # To check each of the functions that are to be called.
    for i in range(0, len(stringList)):
        if "student" in stringList[i]:
            try:
                result = student(stringList[i + 1])
            except IndexError as error:
                oob = oob + 1
            i = i + 1

            if result == 0:
                yes = yes + 1
            else:
                no = no + 1
        elif "password" in stringList[i]:
            try:
                result = password(stringList[i + 1])
            except IndexError as error:
                oob = oob + 1
            i = i + 1

            if result == 0:
                yes = yes + 1
            else:
                no = no + 1

        elif "username" in stringList[i]:
            try:
                result = username(stringList[i + 1])
            except IndexError as error:
                oob = oob + 1
            i = i + 1

            if result == 0:
                yes = yes + 1
            else:
                no = no + 1

        elif "email" in stringList[i]:
            try:
                result = email(stringList[i + 1])
            except IndexError as error:
                oob = oob + 1
            i = i + 1

            if result == 0:
                yes = yes + 1
            else:
                no = no + 1

        elif "previous" in stringList[i]:
            try:
                result = previous(stringList[i + 1], stringList[i - 1])
            except IndexError as error:
                oob = oob + 1
            i = i + 1

            if result == 0:
                yes = yes + 1
            else:
                no = no + 1

        elif "phone" in stringList[i]:
            try:
                result = phone(stringList[i + 1])
            except IndexError as error:
                oob = oob + 1
            i = i + 1
            if result == 0:
                yes = yes + 1
            else:
                no = no + 1

        elif "postal" in stringList[i]:
            try:
                result = postal(stringList[i + 1])
            except IndexError as error:
                oob = oob + 1
            i = i + 1
            if result == 0:
                yes = yes + 1
            else:
                no = no + 1

        elif "address" in stringList[i]:
            try:
                result = address(stringList[i + 1])
            except IndexError as error:
                oob = oob + 1
            i = i + 1
            if result == 0:
                yes = yes + 1
            else:
                no = no + 1

        elif "binary" in stringList[i]:
            try:
                result = binary(stringList[i + 1])
            except IndexError as error:
                oob = oob + 1
            i = i + 1
            if result == 0:
                yes = yes + 1
            else:
                no = no + 1

        elif "bio" in stringList[i]:
            try:
                # print("Bio String: " + str(stringList[i] + " " + str(stringList[i+1])))
                result = bio(stringList[i + 1])
            except IndexError as error:
                oob = oob + 1
                print("oob")
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


def student(string):
    # print( "student STring " + string )
    regex = string.strip()
    regex = regex.strip()
    # print( "student reg " + regex )
    # Checks for 0-9 for 9 or [0-9]{3}_x3
    # # print(re.search('([0-9]){9}|[0-9]{3} [0-9]{3} [0-9]{3}', regex))
    if re.search('([0-9]){9}|[0-9]{3} [0-9]{3} [0-9]{3}', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def password(string):
    regex = string.replace('\n', '')
    regex = regex.strip()
    # print(regex)
    # # print(re.search('^[ -~]{12}', regex))
    if re.search('^[ -~]{12}', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def username(string):
    regex = string.replace('\n', '')
    regex = regex.strip()
    # print(regex)
    # # print(re.search('^[a-zA-Z0-9]{3,20}', regex))
    if re.search('^[a-zA-Z0-9]{3,20}', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def email(string):
    # .net, .ca .com . org .gov .int .edu
    regex = string.replace('\n', '')
    regex = regex.strip()
    # print(regex)
    # # print(re.search("[a-zA-Z0-9]{3,20}@[a-zA-Z]+\\.(ca|com|org|gov|net|int|edu)$", regex))
    if re.search("[a-zA-Z0-9]{3,20}@[a-zA-Z]+\\.(ca|com|org|gov|net|int|edu)$", regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def previous(string, previousString):
    # remove the leading info using regex, save it? then check both
    regex = string.replace('\n', '')
    # print(regex)
    if string == previousString:
        print("yes")
        return 0
    else:
        print("no")
        return 1


def phone(string):
    regex = string.replace('\n', '')
    regex = string.strip()
    # print(regex)
    # # print(re.search('(\\([0-9]{3}\\)|[0-9]{3})(-|\\.|)[0-9]{3}(\\.|-|)[0-9]{4}', regex))
    if re.search('^(\\([0-9]{3}\\)|[0-9]{3})(-|\\.|)[0-9]{3}(\\.|-|)[0-9]{4}', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def postal(string):
    regex = ''
    regex = string.replace('\n', '')
    # print(regex)
    # # print(re.search('([A-Za-z][0-9][A-Za-z] |[A-Za-z][0-9][A-Za-z])[0-9][A-Za-z][0-9]', regex))
    if re.search('([A-Za-z][0-9][A-Za-z] |[A-Za-z][0-9][A-Za-z])[0-9][A-Za-z][0-9]', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def address(string):
    regex = string.replace('\n', '')
    regex = regex.strip()
    # print(regex)
    # # print(re.search('[0-9]{2,4}( |-[0-9]{1,3}|#[0-9]{1,3})[a-zA-Z]+[A-Za-z]+(\\.|)', regex))
    if re.search('[0-9]{2,4}( |-[0-9]{1,3}|#[0-9]{1,3})[a-zA-Z]+[A-Za-z]+(\\.|)', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def binary(string):
    regex = string.replace('\n', '')
    regex = regex.strip()
    # print(regex)
    # # print(re.search('[0-1]+', regex))
    if re.search('[0-1]+', regex):
        print("yes")
        return 0
    else:
        print("no")
        return 1


def bio(string):
    # print("string = " + string)
    regex = string.replace('\n', ' ')
    regex = regex.strip()
    # print(regex)
    # print(re.search('<([a-zA-Z]+)(>||[ -~]+)(</[a-zA-Z]+|)>', regex))
    if re.search('<([a-zA-Z]+)(>||[ -~]+)(</[a-zA-Z]+|)>', regex):
        print("no")
        return 1
    else:
        print("yes")
        return 0


if __name__ == "__main__":
    print("Welcome to the......")
    custom_font = Figlet(font='jazmine')
    print(custom_font.renderText("Regex Machine"))
    main()

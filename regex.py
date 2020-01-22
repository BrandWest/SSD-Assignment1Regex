import re


def main():
    # create array, store the function name, string
    stringList = []
    yes = 0
    no = 0
    index = 0
    count = 0
    rules = ["student,", "password,", "username,", "email,", "previous,", "phone,", "postal,", "address,", "binary,",
             "bio,"]
    with open("/home/caboose/Desktop/ssd/assignment1Regex/assignment1Regex.txt", "r") as data:
        for line in data:
            rule = line.replace("\n", '')
            stringList.append(rule)
            # stringList.append(string)
        #
        # for index in range(0, len(stringList)):
        #
        #     if "\n" in stringList[index+1]:
        print ( stringList)

        # To check each of the functions that are to be called.
        for i in range(0, len(stringList)):
            if "student" in stringList[i]:
                student(stringList[i])
            elif "password" in stringList[i]:
                password(stringList[i])
            elif "username" in stringList[i]:
                username(stringList[i])
            elif "email" in stringList[i]:
                email(stringList[i])
            elif "previous" in stringList[i]:
                previous(stringList[i], stringList[i - 1])
            elif "phone" in stringList[i]:
                phone(stringList[i])
            elif "postal" in stringList[i]:
                postal(stringList[i])
            elif "address" in stringList[i]:
                address(stringList[i])
            elif "binary" in stringList[i]:
                binary(stringList[i])
            elif "bio" in stringList[i]:
                bio(stringList[i])
            else:
                print("No function call required " + stringList[i])


def student(string):
    regex = string.strip('student,')
    # Checks for 0-9 for 9 or [0-9]{3}_x3
    if re.search('([0-9]){9}|[0-9]{3} [0-9]{3} [0-9]{3}', regex):
        print(string + " yes")
    else:
        print(string + " no")


def password(string):
    regex = string.strip('password,')
    # [ -~] does all ascii characters minimum of 12
    if re.search('^[ -~]{12}', regex):
        print(string + " yes")
    else:
        print(string + " no")


def username(string):
    regex = string.strip('username,')
    if re.search('^[a-zA-Z0-9]{3,20}', regex):
        print(string + " yes")
    else:
        print(string + " no")


def email(string):
    # .net, .ca .com . org .gov .int .edu
    # lots of edge cases to look at.
    regex = string.replace('email,', '')

    if re.search("^[a-zA-Z0-9]{3,20}@[a-zA-Z]+\\.(ca|com|org|gov|net|int|edu)$", regex):
        print(string + " yes")
    else:
        print(string, " no")


def previous(string, previousString):
    # remove the leading info using regex, save it? then check both
    regex = string.strip('previous,')
    if re.search('^[\\s]+', regex):
        print(string + " yes")
    else:
        print(string, " no")


def phone(string):
    regex = ''
    regex = string.replace('phone,', '')
    if re.search('', regex):
        print(string + " yes")
    else:
        print(string, " no")


def postal(string):
    regex = ''
    regex = string.strip('student,')
    if re.search('', regex):
        print(string + " yes")
    else:
        print(string, " no")


def address(string):
    regex = ''
    regex = string.strip('student,')
    if re.search('', regex):
        print(string + " yes")
    else:
        print(string, " no")


def binary(string):
    regex = ''
    regex = string.strip('student,')
    if re.search('', regex):
        print(string + " yes")
    else:
        print(string, " no")


def bio(string):
    regex = ''
    regex = string.strip('student,')
    if re.search('', regex):
        print(string + " yes")
    else:
        print(string, " no")


if __name__ == "__main__":
    main()

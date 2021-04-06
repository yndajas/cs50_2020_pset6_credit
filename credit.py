from cs50 import get_int


def main():
    number = get_int("Card number: ")
    length = len(str(number))

    # check length and sumcheck are valid
    if length in [13, 15, 16] and sumcheck(number, length):
        # print("reached checkpoint ")
        type(number)
    else:
        print("INVALID")


def sumcheck(number, length):
    sum = 0

    # for loop going backwards (starts at the index of the final number, so length minus one; goes to index 0; goes down one each time)
    for i in range(length - 1, -1, -1):
        # if last/third to/fifth to etc last digit, add it
        if (length - i) % 2 == 1:
            sum += int(str(number)[i])
        # if it's second/fourth/sixth etc to last, multiple by two then add the digits of the result
        else:
            # double it
            doubled = int(str(number)[i]) * 2

            # if the doubled number is two digits
            if doubled > 9:
                # add each of the digits
                sum += (int(str(doubled)[0])) + (int(str(doubled)[1]))
            else:
                # add doubled number if it's just one digit
                sum += doubled

    # number is valid if the last digit of the sum is 0
    if sum % 10 == 0:
        return True
    else:
        return False


def type(number):
    if int(str(number)[0:2]) in [34, 37]:
        print("AMEX")
    elif int(str(number)[0:2]) in [51, 52, 53, 54, 55]:
        print("MASTERCARD")
    elif int(str(number)[0]) == 4:
        print("VISA")
    else:
        print("INVALID")


main()

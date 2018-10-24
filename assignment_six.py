# mark hooks 10/24/2018
# this program is to create a list of prime numbers from the maximum number that the user gives
def user_number():
    """
    this program is to get the user to give the maximum number
    :return: this returns the function
    """
    max_num = int(input("type in the maximum number."))
    return max_num


def main():
    max_num = int(input("type in the maximum number."))
    blank_list = []
    for x in range(2, max_num + 1):
        blank_list.append(x)
    print(blank_list)
    prime_number = []
    # this is to loop through the list
    while len(blank_list) > 0:
        number = blank_list[0]
        prime_number.append(number)
        for z in blank_list:
            if z % number == 0:
                blank_list.remove(z)
    print("your list of prime numbers is", prime_number)


main()

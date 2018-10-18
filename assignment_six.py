def user_number():
    max_num = input("what should the maximum number be?")
    return max_num


def main():
    max_num = int(input("what should the maximum number be?"))
    blank_list = []
    for x in range(2, max_num + 1):
        blank_list.append(x)
    print(blank_list)


main()

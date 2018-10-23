def user_number():
    max_num = input("what should the maximum number be?")
    return max_num


def main():
    max_num = int(input("what should the maximum number be?"))
    blank_list = []
    for x in range(2, max_num + 1):
        blank_list.append(x)
    print(blank_list)
    prime_number = []
    while len(blank_list) > 0:
        number = blank_list[0]
        prime_number.append(number)
        for z in blank_list:
            if z % blank_list[0] == 0:
                blank_list.remove(z)
        # for max_num in range(2, max_num):
        #     for y in range(2, max_num):
        #         if max_num % y == 0:
        #             del blank_list[y]
        #             break
        #         else:
        #             prime_number.append(max_num)

    print(prime_number)


main()

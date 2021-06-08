


def main():
    # How to print stuff
    # print("hi")

    # Numbers
    x = 1 + 2
    z = 1 - 2
    y = 1 * 4
    h = 3 / 2
    # print(h)

    # Mod - gives you remainder
        # Check for even if result is 0
        # good habit to follow naming standards accordingly to each language
    even_num = 4 % 2
    # print(even_num)
    # Check for odd if result is not 0
    odd_num = 3 % 2
    # print(odd_num)

    # Exponents
    cube_num = 2 ** 3
    # print(cube_num)
    square_num = 2 ** 2
    # print(square_num)

    # What datatype am I using?
    a = 5.0
    # print(type(a))

    # String Slicing
    # [start:stop:step]
    test_string = "0123456789"
    # print(test_string[-1:0:-1]) # print in reverse
    # print(test_string[::-1])
    # print(test_string[0:10:2])  # print in steps of 2
    # print(test_string[::2])
    # print(test_string[:4]) # starts from beginning to end (not including end)

    word = "tinker"
    # print(word[1:4])

    # New line : \n
    # print("Hello g\nworld")

    # Length of string includes space
    test_string  = "2347585231356895281491848624"
    length_of_test_string = len(test_string)
    # print(length_of_test_string)

    # STRINGS ARE IMMUTABLE - cannot change from index
    name = "Mich"
    last_letters = name[1:]
    # print('L' + name[1:])
    # or
    dif_name = 'L' + last_letters
    # print(dif_name)

    x = "Hello world"
    # print(x.upper())
    capitalized_x = x.upper()
    # print(capitalized_x)

    # If Else statements
    num = 0
    if (num == 0):
        # execute some code
    elif (num == 1):
        # do something different
    else:
        # do something else

    # Booleans with 0 and 1
    # If 0, it is false.
    # If 1 or any other number, it is true.
    #     if 2:
            # print("This is a true statement")
        # else:
            # print("This is false")

    # For loop
    my_iterable = [1,2,3]
    for item_name in my_iterable:
        print(item_name)


if __name__ == '__main__':
    main()



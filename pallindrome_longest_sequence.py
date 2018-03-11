#!/bin/python3


def isPallindrome(str):
    return str == str[::-1]


def long_sequence(str):
    result = ""
    for i in range((1 << len(str)), -1, -1):
        test_str = ""
        for j in range(len(str)):
            if (i & (1 << j)) > 0:
                test_str += str[j]
        print(test_str)
        if isPallindrome(test_str) and len(test_str) > len(result):
            result = test_str
            #break

    return result


def main():
    print("Longest Pallindrome sequence Problem:")

    test_str = "character"
    result = long_sequence(test_str)
    print("Result: {}".format(result))


if __name__ == "__main__":
    main()

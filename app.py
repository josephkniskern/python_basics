from pprint import pprint


# def fizz_buzz(num):
#     if (num % 3 == 0) and (num % 5 == 0):
#         return "FizzBuzz"
#     if num % 3 == 0:
#         return "Fizz"
#     if num % 5 == 0:
#         return "Buzz"
#     return num


# print(fizz_buzz(15))


######################## most common character #######################

sentence = "This is a common interview question"


def most_common_letter(sentence):
    count = {}

    for char in sentence:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    count_sorted = sorted(
        count.items(),
        key=lambda kv:
        kv[1],
        reverse=True)
    return count_sorted[0]


print(most_common_letter(sentence))

def prime_list(numbers):
    for number in numbers:
        if number % 2 == 1:
            number_list.remove(number)
    return number_list


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number_list)
print(prime_list(number_list))
